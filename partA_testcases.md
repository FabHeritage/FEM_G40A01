# Part A Test Cases

Run the automated scenarios from the project directory with:

```text
python magic_square_test.py
```

| Used data | Expected result | Actual result | Proof | Status |
|---|---|---|---|---|
| `determine_max([1, 9, 2])` | `True` |  | Add screenshot here |  |
| `determine_max([1, 10, 2])` | `False`; prints number out of range |  | Add screenshot here |  |
| `determine_max([-1, 2, 3])` | `True` under the current upper-bound-only check |  | Add screenshot here |  |
| `not_same_number([[1, 2], [3, 4]])` | `True` |  | Add screenshot here |  |
| `not_same_number([[1, 2], [2, 3]])` | `False`; prints repeated number |  | Add screenshot here |  |
| First row `[2, 9, 6]`; input rows `4 1 8`, `3 5 7` | Returns `[[2, 9, 6], [4, 1, 8], [3, 5, 7]]` |  | Add screenshot here |  |
| First row `[1, 10, 2]` | Returns `None`, prints number out of range, reads no more input |  | Add screenshot here |  |
| First row `[1, 2]` | Returns `None`; prints not a square (minimum size is 3) |  | Add screenshot here |  |
| First row `[1, 2, 3]`; next row `1 2 3 4` | Returns `None`; prints number out of range (row too long) |  | Add screenshot here |  |
| First row `[1, 2, 3]`; next row `1 2` | Returns `None`; prints not a square (row too short) |  | Add screenshot here |  |
| First row `[1, 2, 3]`; next rows `4 5 6`, `7 2 9` | Returns `None`; prints repeated number |  | Add screenshot here |  |
| `sum_row([[8,1,6],[3,5,7],[4,9,2]])` | `[15, 15, 15]` |  | Add screenshot here |  |
| `sum_column([[8,1,6],[3,5,7],[4,9,2]])` | Returns `[15, 15, 15]`; current implementation clears the supplied grid |  | Add screenshot here |  |
| `sum_diagonal([[8,1,6],[3,5,7],[4,9,2]])` | `[15, 15]` |  | Add screenshot here |  |
| `determine_magic_square([[8,1,6],[3,5,7],[4,9,2]])` | `Is a magic square (sum is {15})`; preserves input grid |  | Add screenshot here |  |
| `determine_magic_square([[1,2,3],[4,5,6],[7,8,9]])` | `Is not a magic square (not all the same sum)` |  | Add screenshot here |  |
| `prompt_user()` with input rows `8 1 6`, `3 5 7`, `4 9 2` | Returns `None`; prints prompt and magic-square result |  | Add screenshot here |  |
| `main()` | Calls `prompt_user()` once; returns `None` |  | Add screenshot here |  |


