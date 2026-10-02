import contextlib
import io
from ast import literal_eval
from unittest.mock import mock_open, patch

import todo_list as todo


TOTAL_PASSED = 0
TOTAL_TESTS = 0


def check(name, condition):
    global TOTAL_PASSED, TOTAL_TESTS
    TOTAL_TESTS += 1
    if condition:
        TOTAL_PASSED += 1
        print(f"PASS: {name}")
    else:
        print(f"FAIL: {name}")


def safe_test(name, test_function):
    """Run a test without stopping the rest of the test file on an error."""
    try:
        test_function()
    except Exception as error:
        global TOTAL_TESTS
        TOTAL_TESTS += 1
        print(f"ERROR: {name} -> {type(error).__name__}: {error}")


def task(task_id, completed=False):
    return dict(task_id=task_id, task_description="Study",
                task_completed=completed, task_project="#school")


def capture(function, *args):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        function(*args)
    return output.getvalue()


def test_task():
    item = todo.Task(1, "Study", False, "#school")
    check("Task stores all fields", vars(item) == dict(
        id=1, desc="Study", completed=False, project="#school"))
    check("Task string and repr include all fields",
          str(item) == "1 | Study | #school | False"
          and literal_eval(repr(item)) == task(1))
    check("Task equality compares completion",
          item == todo.Task(2, "Other", False, "")
          and item != todo.Task(1, "Study", True, "#school"))


def test_read_file():
    with patch("builtins.open", mock_open(read_data=repr(task(1)) + "\n\n")):
        check("read removes newlines and blank lines",
              todo.read_file("test.txt") == [repr(task(1))])
    with patch("builtins.open", mock_open(read_data="")):
        check("empty file returns empty list", todo.read_file("test.txt") == [])
    with patch("builtins.open", side_effect=FileNotFoundError):
        check("missing file returns empty list", todo.read_file("test.txt") == [])


def test_add_task():
    writer = mock_open()
    with patch.object(todo, "read_file", return_value=[]), patch("builtins.open", writer):
        output = capture(todo.add_task, "test.txt", "Study")
    check("first task gets ID 1 and confirmation",
          literal_eval(writer().write.call_args.args[0]) == dict(
              task_id=1, task_description="Study", task_completed=False,
              task_project="") and "Added task 1" in output)
    writer = mock_open()
    with patch.object(todo, "read_file", return_value=[repr(task(12))]), patch("builtins.open", writer):
        capture(todo.add_task, "test.txt", "Study #school")
    check("add uses largest ID and separates project",
          literal_eval(writer().write.call_args.args[0]) == task(13))
    try:
        todo.add_task("test.txt", "")
    except ValueError:
        check("empty add is rejected", True)
    else:
        check("empty add is rejected", False)


def test_update_task():
    writer = mock_open()
    with patch.object(todo, "read_file", return_value=[repr(task(1, True))]), patch("builtins.open", writer):
        output = capture(todo.update_task, "test.txt", "1 New description")
    expected = task(1, True)
    expected["task_description"] = "New description"
    check("update changes only description and confirms change",
          literal_eval(writer().write.call_args.args[0]) == expected
          and "'Study' -> 'New description'" in output)
    with patch.object(todo, "read_file", return_value=[repr(task(1))]), patch("builtins.open", mock_open()), patch("builtins.input", return_value="Prompted") as prompt:
        capture(todo.update_task, "test.txt", "1")
    check("missing description prompts", prompt.call_count == 1)
    with patch.object(todo, "read_file", return_value=[]), patch("builtins.open") as writer:
        output = capture(todo.update_task, "test.txt", "99 New")
    check("missing update task is reported without writing",
          "not found" in output and writer.call_count == 0)


def test_remove_task():
    writer = mock_open()
    with patch.object(todo, "read_file", return_value=[repr(task(1)), repr(task(2))]), patch("builtins.open", writer):
        output = capture(todo.remove_task, "test.txt", "1")
    check("remove preserves other task and confirms removal",
          writer().write.call_count == 1
          and literal_eval(writer().write.call_args.args[0]) == task(2)
          and "Removed task 1" in output)
    with patch.object(todo, "read_file", return_value=[]), patch("builtins.open") as writer:
        output = capture(todo.remove_task, "test.txt", "99")
    check("missing remove task is reported without writing",
          "not found" in output and writer.call_count == 0)
    try:
        todo.remove_task("test.txt", "abc")
    except ValueError:
        check("nonnumeric remove ID is rejected", True)
    else:
        check("nonnumeric remove ID is rejected", False)


def test_mark_task_complete():
    writer = mock_open()
    with patch.object(todo, "read_file", return_value=[repr(task(1))]), patch("builtins.open", writer):
        output = capture(todo.mark_task_complete, "test.txt", "1")
    check("done sets completion and confirms change",
          literal_eval(writer().write.call_args.args[0]) == task(1, True)
          and "Completed task 1" in output)
    with patch.object(todo, "read_file", return_value=[repr(task(1, True))]), patch("builtins.open") as writer:
        output = capture(todo.mark_task_complete, "test.txt", "1")
    check("already complete task is not rewritten",
          "already complete" in output and writer.call_count == 0)
    with patch.object(todo, "read_file", return_value=[]):
        output = capture(todo.mark_task_complete, "test.txt", "99")
    check("missing done task is reported", "not found" in output)


def test_format_all_tasks():
    with patch.object(todo, "read_file", return_value=[repr(task(12)), repr(task(2, True))]):
        output = capture(todo.format_all_tasks, "test.txt")
    check("all list displays all fields in ID order",
          "ID | Description | Project | Completed" in output
          and "2 | Study | #school | True" in output
          and output.index("2 |") < output.index("12 |"))
    with patch.object(todo, "read_file", return_value=[]):
        output = capture(todo.format_all_tasks, "test.txt")
    check("empty all list prints message", "No tasks to display" in output)
    try:
        todo.format_all_tasks("test.txt", "wrong")
    except ValueError:
        check("invalid list option is rejected", True)
    else:
        check("invalid list option is rejected", False)


def test_format_uncompleted_task():
    with patch.object(todo, "read_file", return_value=[repr(task(12)), repr(task(2)), repr(task(1, True))]):
        output = capture(todo.format_uncompleted_task, "test.txt")
    check("todo lists only pending tasks in ID order",
          "1 |" not in output and output.index("2 |") < output.index("12 |"))
    with patch.object(todo, "read_file", return_value=[repr(task(1, True))]):
        output = capture(todo.format_uncompleted_task, "test.txt")
    check("all completed prints no pending tasks", "No uncompleted tasks" in output)
    with patch.object(todo, "format_uncompleted_task") as listing:
        todo.format_all_tasks("test.txt", "todo")
    check("list todo calls filtered listing", listing.call_count == 1)


def test_purge():
    writer = mock_open()
    with patch.object(todo, "read_file", return_value=[repr(task(1, True)), repr(task(2))]), patch("builtins.open", writer):
        output = capture(todo.purge, "test.txt")
    check("purge removes completed tasks and confirms removal",
          writer().write.call_count == 1
          and literal_eval(writer().write.call_args.args[0]) == task(2)
          and "Purged task 1" in output)
    with patch.object(todo, "read_file", return_value=[repr(task(1))]), patch("builtins.open") as writer:
        output = capture(todo.purge, "test.txt")
    check("no completed tasks means no rewrite",
          "No completed tasks" in output and writer.call_count == 0)
    writer = mock_open()
    with patch.object(todo, "read_file", return_value=[repr(task(1, True))]), patch("builtins.open", writer):
        capture(todo.purge, "test.txt")
    check("purging all tasks opens empty replacement file",
          writer.call_args.args == ("test.txt", "w")
          and writer().write.call_count == 0)


def test_start():
    with patch.object(todo, "format_all_tasks"), patch.object(todo, "add_task") as add, patch("builtins.input", side_effect=["add Study", "end"]):
        output = capture(todo.start)
    check("CLI dispatches add and prints helper each time",
          add.call_args.args == ("tasks.txt", "Study")
          and output.count("Commands:") == 2)
    with patch.object(todo, "format_all_tasks"), patch("builtins.input", side_effect=["unknown", "rem abc", "end"]):
        output = capture(todo.start)
    check("CLI handles unknown command and argument error",
          "Unknown command" in output and "Error:" in output)
    with patch.object(todo, "format_all_tasks", side_effect=PermissionError("denied")), patch("builtins.input", side_effect=EOFError):
        output = capture(todo.start)
    check("CLI handles file error and EOF exit",
          "Error: denied" in output and "Goodbye" in output)


def test_main():
    with patch.object(todo, "start") as mocked_start:
        result = todo.main()
    check("main starts CLI once and returns None",
          mocked_start.call_count == 1 and result is None)


print("\nTO DO LIST TESTS")
print("=" * 40)

safe_test("Task", test_task)
safe_test("read_file", test_read_file)
safe_test("add_task", test_add_task)
safe_test("update_task", test_update_task)
safe_test("remove_task", test_remove_task)
safe_test("mark_task_complete", test_mark_task_complete)
safe_test("format_all_tasks", test_format_all_tasks)
safe_test("format_uncompleted_task", test_format_uncompleted_task)
safe_test("purge", test_purge)
safe_test("start", test_start)
safe_test("main", test_main)

print("\n" + "=" * 40)
print(f"Passed {TOTAL_PASSED} of {TOTAL_TESTS} tests")
if TOTAL_TESTS > 0:
    percent = TOTAL_PASSED / TOTAL_TESTS * 100
    print(f"Test pass rate: {percent:.1f}%")
print("=" * 40)
