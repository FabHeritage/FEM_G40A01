from ast import literal_eval


class Task:
    def __init__(self, id, desc, completed, project):
        self.id = id
        self.desc = desc
        self.completed = completed
        self.project = project

    def __str__(self):
        return f"{self.id} | {self.desc} | {self.project} | {self.completed}"

    def __repr__(self):
        return repr(dict(task_id=self.id, task_description=self.desc,
                         task_project=self.project,
                         task_completed=self.completed))

    def __eq__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return self.completed == other.completed


def read_file(file):
    try:
        with open(file, 'r') as f:
            tasks = []
            for line in f:
                if line.strip():
                    tasks.append(line.rstrip("\r\n"))
            return tasks
    except FileNotFoundError:
        return []


def add_task(file, line):
    if not line.strip():
        raise ValueError("Usage: add <task> [#project]")
    lines = read_file(file)
    indexes = []
    for dic in lines:
        task = literal_eval(dic)
        indexes.append(task['task_id'])
    id = 1 if len(indexes) == 0 else int(max(indexes)) + 1
    project = line.split(" ")[-1]
    desc = line
    completed = False

    if project.startswith("#"):
        desc = line.rsplit(project, 1)[0].strip()
        if not desc or project == "#":
            raise ValueError("Enter a task description and a project word.")
    else:
        project = ""

    format_line = Task(id=id, desc=desc, project=project, completed=completed)
    with open(file, "a") as f:
        f.write(repr(format_line) + "\n")
    print(f"Added task {id}: {desc.strip()}")


def update_task(file, line):
    opt = line.strip().split(" ", 1)
    task_id = int(opt[0])
    tasks = [literal_eval(dic) for dic in read_file(file)]
    found = False

    for task in tasks:
        if task["task_id"] == task_id:
            description = opt[1].strip() if len(opt) > 1 else ""
            if not description:
                description = input("Enter the new task description: ").strip()
            if not description:
                raise ValueError("Description cannot be empty.")
            old_description = task["task_description"]
            task["task_description"] = description
            found = True

    if not found:
        print(f"Task {task_id} not found.")
        return

    with open(file, "w") as f:
        for task in tasks:
            f.write(repr(task) + "\n")
    print(f"Updated task {task_id}: {old_description!r} -> {description!r}")


def remove_task(file, line):
    task_id = int(line.strip())
    tasks = [literal_eval(dic) for dic in read_file(file)]
    remaining_tasks = [task for task in tasks if task["task_id"] != task_id]

    if len(remaining_tasks) == len(tasks):
        print(f"Task {task_id} not found.")
        return

    with open(file, "w") as f:
        for task in remaining_tasks:
            f.write(repr(task) + "\n")
    for task in tasks:
        if task["task_id"] == task_id:
            print(f"Removed task {task_id}: {task['task_description']}")


def mark_task_complete(file, line):
    task_id = int(line.strip())
    tasks = [literal_eval(dic) for dic in read_file(file)]
    found = False

    for task in tasks:
        if task["task_id"] == task_id:
            if task["task_completed"]:
                print(f"Task {task_id} is already complete.")
                return
            task["task_completed"] = True
            description = task["task_description"]
            found = True

    if not found:
        print(f"Task {task_id} not found.")
        return

    with open(file, "w") as f:
        for task in tasks:
            f.write(repr(task) + "\n")
    print(f"Completed task {task_id}: {description}")


def format_all_tasks(file, line="all"):
    if line.strip() == "todo":
        format_uncompleted_task(file)
        return
    if line.strip() != "all":
        raise ValueError("Usage: list all or list todo")
    tasks = [literal_eval(dic) for dic in read_file(file)]
    if not tasks:
        print("No tasks to display.")
        return
    print("ID | Description | Project | Completed")
    for task in sorted(tasks, key=lambda task: task["task_id"]):
        print(f"{task['task_id']} | {task['task_description'].strip()} | "
              f"{task['task_project'] or '-'} | {task['task_completed']}")


def format_uncompleted_task(file):
    tasks = [literal_eval(dic) for dic in read_file(file)]
    tasks = [task for task in tasks if not task["task_completed"]]
    if not tasks:
        print("No uncompleted tasks to display.")
        return
    print("ID | Description | Project | Completed")
    for task in sorted(tasks, key=lambda task: task["task_id"]):
        print(f"{task['task_id']} | {task['task_description'].strip()} | "
              f"{task['task_project'] or '-'} | {task['task_completed']}")


def purge(file, line=""):
    if line.strip():
        raise ValueError("Usage: purge")
    tasks = [literal_eval(dic) for dic in read_file(file)]
    remaining_tasks = [task for task in tasks if not task["task_completed"]]
    if len(tasks) == len(remaining_tasks):
        print("No completed tasks to purge.")
        return
    with open(file, "w") as f:
        for task in remaining_tasks:
            f.write(repr(task) + "\n")
    for task in tasks:
        if task["task_completed"]:
            print(f"Purged task {task['task_id']}: {task['task_description']}")


def start():
    file = "tasks.txt"
    try:
        format_all_tasks(file)
    except (ValueError, SyntaxError, KeyError, TypeError, OSError) as error:
        print(f"Error: {error}")

    while True:
        print("\nCommands: add <task> [#project] | upd <id> <new description>")
        print("rem <id> | done <id> | list all | list todo | purge | end")
        try:
            opt = input("> ").strip().split(" ", 1)
            opts = {
                "end": False,
                "add": add_task,
                "upd": update_task,
                "rem": remove_task,
                "done": mark_task_complete,
                "list": format_all_tasks,
                "purge": purge,
            }
            command = opts.get(opt[0])
            if command is False:
                break
            if command is None:
                print("Unknown command. Use the guide above.")
                continue
            line = opt[1] if len(opt) > 1 else ""
            command(file, line)
        except (ValueError, SyntaxError, KeyError, TypeError, OSError) as error:
            print(f"Error: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break


def main():
    start()
if __name__ == "__main__":
    main()