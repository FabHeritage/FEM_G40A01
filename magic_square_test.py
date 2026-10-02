import contextlib
import io
from unittest.mock import patch

import magic_square as square


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


def test_estimate_square_size():
    with patch("builtins.input", side_effect=["4 1 8", "3 5 7"]):
        grid = square.estimate_square_size([2, 9, 6])
    check("valid rows are read and returned", grid == [[2, 9, 6], [4, 1, 8], [3, 5, 7]])

    output = io.StringIO()
    with contextlib.redirect_stdout(output), patch("builtins.input") as mocked_input:
        result = square.estimate_square_size([1, 10, 2])
    check("out-of-range first row is rejected", result is None and "number out of range" in output.getvalue())
    check("out-of-range first row stops before reading more", mocked_input.call_count == 0)

    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        result = square.estimate_square_size([1, 2])
    check("first row smaller than three numbers is rejected", result is None and "not a square" in output.getvalue())

    output = io.StringIO()
    with contextlib.redirect_stdout(output), patch("builtins.input", return_value="1 2 3 4"):
        result = square.estimate_square_size([1, 2, 3])
    check("row with too many numbers is rejected", result is None and "number out of range" in output.getvalue())

    output = io.StringIO()
    with contextlib.redirect_stdout(output), patch("builtins.input", return_value="1 2"):
        result = square.estimate_square_size([1, 2, 3])
    check("row with too few numbers is rejected", result is None and "not a square" in output.getvalue())

    output = io.StringIO()
    with contextlib.redirect_stdout(output), patch("builtins.input", side_effect=["4 5 6", "7 2 9"]):
        result = square.estimate_square_size([1, 2, 3])
    check("repeated number in a later row is rejected", result is None and "repeated a number" in output.getvalue())


def test_determine_max():
    check("number within range is accepted", square.determine_max([1, 9, 2]) is True)

    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        result = square.determine_max([1, 10, 2])
    check("number above range is rejected", result is False and "number out of range" in output.getvalue())
    check("negative number passes current upper-bound check", square.determine_max([-1, 2, 3]) is True)


def test_not_same_number():
    check("grid with unique numbers passes", square.not_same_number([[1, 2], [3, 4]]) is True)

    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        result = square.not_same_number([[1, 2], [2, 3]])
    check("grid with duplicate number is rejected", result is False and "repeated a number" in output.getvalue())


def test_sum_row():
    check(
        "row totals are calculated",
        square.sum_row([[8, 1, 6], [3, 5, 7], [4, 9, 2]]) == [15, 15, 15],
    )


def test_sum_column():
    grid = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    result = square.sum_column(grid)
    check("column totals are calculated", result == [15, 15, 15])
    check("column sum clears the supplied grid", grid == [])


def test_sum_diagonal():
    check(
        "both diagonal totals are calculated",
        square.sum_diagonal([[8, 1, 6], [3, 5, 7], [4, 9, 2]]) == [15, 15],
    )


def test_determine_magic_square():
    grid = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    result = square.determine_magic_square(grid)
    check("classic magic square is recognized", result == "Is a magic square (sum is {15})")
    check("checking a grid preserves its data", grid == [[8, 1, 6], [3, 5, 7], [4, 9, 2]])

    result = square.determine_magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    check("square with different totals is rejected", result == "Is not a magic square (not all the same sum)")


def test_prompt_user():
    output = io.StringIO()
    with contextlib.redirect_stdout(output), patch("builtins.input", side_effect=["8 1 6", "3 5 7", "4 9 2"]):
        result = square.prompt_user()
    check("prompt returns without a value", result is None)
    check("prompt displays instructions", "Please enter the square, separated by spaces" in output.getvalue())
    check("prompt displays the magic-square result", "Is a magic square (sum is {15})" in output.getvalue())


def test_main():
    with patch.object(square, "prompt_user") as mocked_prompt:
        result = square.main()
    check("main returns without a value", result is None)
    check("main starts the prompt", mocked_prompt.call_count == 1)


print("\nMAGIC SQUARE TESTS")
print("=" * 40)

safe_test("estimate_square_size", test_estimate_square_size)
safe_test("determine_max", test_determine_max)
safe_test("not_same_number", test_not_same_number)
safe_test("sum_row", test_sum_row)
safe_test("sum_column", test_sum_column)
safe_test("sum_diagonal", test_sum_diagonal)
safe_test("determine_magic_square", test_determine_magic_square)
safe_test("prompt_user", test_prompt_user)
safe_test("main", test_main)

print("\n" + "=" * 40)
print(f"Passed {TOTAL_PASSED} of {TOTAL_TESTS} tests")

if TOTAL_TESTS > 0:
    percent = TOTAL_PASSED / TOTAL_TESTS * 100
    print(f"Test pass rate: {percent:.1f}%")

print("=" * 40)
