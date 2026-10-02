# Part B Test Cases

Run the automated scenarios from the project directory with:

```text
python todo_list_test.py
```


| Used data | Expected result | Actual result | Proof | Status |
|---|---|---|---|---|
| `Task(1, "Study", False, "#school")` | Stores all four fields |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171646.png) | Pass |
| `str()` and `repr()` of that Task | String lists all fields; repr is a parseable task dictionary |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171651.png) | Pass |
| Compare tasks with same and different completion values | Equal for same completion; unequal for different completion under current implementation |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171703.png) | Pass |
| Read one record followed by blank lines | Returns record without newline; skips blank lines |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171711.png) | Pass |
| Read empty file | Returns `[]` |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171718.png) | Pass |
| Read missing file | Returns `[]` |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171724.png) | Pass |
| `add Study` with no existing tasks | Writes ID 1, empty project, completed False; confirms addition |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171733.png) | Pass |
| `add Study #school` with existing ID 12 | Writes ID 13 with description Study and project #school |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171738.png) | Pass |
| `add` without description | Raises ValueError |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171751.png) | Pass |
| `upd 1 New description` on completed task with project | Changes only description; prints old and new text |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171800.png) | Pass |
| `upd 1`; prompted input | Prompts once for new description |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171809.png) | Pass |
| `upd 99 New` with no task 99 | Prints not found; does not write |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171820.png) | Pass |
| `rem 1` with tasks 1 and 2 | Keeps task 2 only; confirms removal |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171828.png) | Pass |
| `rem 99` with no task 99 | Prints not found; does not write |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171838.png) | Pass |
| `rem abc` | Raises ValueError |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171845.png) | Pass |
| `done 1` on pending task | Sets completed True; confirms change |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171855.png) | Pass |
| `done 1` on completed task | Prints already complete; does not write |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171901.png) | Pass |
| `done 99` with no task 99 | Prints not found |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171907.png) | Pass |
| `list all` with IDs 12 and 2 | Displays header and all fields in numeric ID order 2 then 12 |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171914.png) | Pass |
| `list all` with empty list | Prints no tasks to display |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171922.png) | Pass |
| `list wrong` | Raises ValueError |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171929.png) | Pass |
| List pending IDs 12 and 2 and completed ID 1 | Displays pending tasks only, in order 2 then 12 |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171943.png) | Pass |
| List uncompleted tasks when all completed | Prints no uncompleted tasks |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171951.png) | Pass |
| `format_all_tasks(file, "todo")` | Calls filtered listing once |  | ![Test proof](partB_images/Screenshot%202026-10-02%20171957.png) | Pass |
| `purge` with completed ID 1 and pending ID 2 | Keeps ID 2 only; confirms purged ID 1 |  | ![Test proof](partB_images/Screenshot%202026-10-02%20172003.png) | Pass |
| `purge` with no completed tasks | Prints no completed tasks; does not write |  | ![Test proof](partB_images/Screenshot%202026-10-02%20172010.png) | Pass |
| `purge` with all tasks completed | Opens replacement file in write mode; writes no records |  | ![Test proof](partB_images/Screenshot%202026-10-02%20172022.png) | Pass |
| CLI input: `add Study`, `end` | Calls add with correct text; displays helper before each input |  | ![Test proof](partB_images/Screenshot%202026-10-02%20172029.png) | Pass |
| CLI input: `unknown`, `rem abc`, `end` | Prints unknown-command message and argument error; continues |  | ![Test proof](partB_images/Screenshot%202026-10-02%20172049.png) | Pass |
| CLI startup file permission error; input EOFError | Prints file error, then Goodbye; exits cleanly |  | ![Test proof](partB_images/Screenshot%202026-10-02%20172058.png) | Pass |
| `main()` | Calls start once; returns None |  | ![Test proof](partB_images/Screenshot%202026-10-02%20172105.png) | Pass |
