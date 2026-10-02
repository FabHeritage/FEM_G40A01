# Part A Test Cases

Run the automated scenarios from the project directory with:

```text
python magic_square_test.py
```

| Used data | Expected result | Actual result | Proof | Status |
|---|---|---|---|---|
| `determine_max([1, 9, 2])` | `True` |  | ![Test proof 8](partA_images/Screenshot%202026-10-02%20172804.png) | Pass |
| `determine_max([1, 10, 2])` | `False`; prints number out of range |  | ![Test proof 9](partA_images/Screenshot%202026-10-02%20172808.png) | Pass |
| `determine_max([-1, 2, 3])` | `True` under the current upper-bound-only check |  | ![Test proof 10](partA_images/Screenshot%202026-10-02%20172812.png) | Pass |
| `not_same_number([[1, 2], [3, 4]])` | `True` |  | ![Test proof 11](partA_images/Screenshot%202026-10-02%20172816.png) | Pass |
| `not_same_number([[1, 2], [2, 3]])` | `False`; prints repeated number |  | ![Test proof 12](partA_images/Screenshot%202026-10-02%20172828.png) | Pass |
| First row `[2, 9, 6]`; input rows `4 1 8`, `3 5 7` | Returns `[[2, 9, 6], [4, 1, 8], [3, 5, 7]]` |  | ![Test proof 1](partA_images/Screenshot%202026-10-02%20172721.png) | Pass |
| First row `[1, 10, 2]` | Returns `None`, prints number out of range, reads no more input |  | ![Test proof 2](partA_images/Screenshot%202026-10-02%20172728.png)<br>![Test proof 3](partA_images/Screenshot%202026-10-02%20172733.png) | Pass |
| First row `[1, 2]` | Returns `None`; prints not a square (minimum size is 3) |  | ![Test proof 4](partA_images/Screenshot%202026-10-02%20172738.png) | Pass |
| First row `[1, 2, 3]`; next row `1 2 3 4` | Returns `None`; prints number out of range (row too long) |  | ![Test proof 5](partA_images/Screenshot%202026-10-02%20172744.png) | Pass |
| First row `[1, 2, 3]`; next row `1 2` | Returns `None`; prints not a square (row too short) |  | ![Test proof 6](partA_images/Screenshot%202026-10-02%20172749.png) | Pass |
| First row `[1, 2, 3]`; next rows `4 5 6`, `7 2 9` | Returns `None`; prints repeated number |  | ![Test proof 7](partA_images/Screenshot%202026-10-02%20172757.png) | Pass |
| `sum_row([[8,1,6],[3,5,7],[4,9,2]])` | `[15, 15, 15]` |  | ![Test proof 13](partA_images/Screenshot%202026-10-02%20172833.png) | Pass |
| `sum_column([[8,1,6],[3,5,7],[4,9,2]])` | Returns `[15, 15, 15]`; current implementation clears the supplied grid |  | ![Test proof 14](partA_images/Screenshot%202026-10-02%20172840.png)<br>![Test proof 15](partA_images/Screenshot%202026-10-02%20172848.png) | Pass |
| `sum_diagonal([[8,1,6],[3,5,7],[4,9,2]])` | `[15, 15]` |  | ![Test proof 16](partA_images/Screenshot%202026-10-02%20172854.png) | Pass |
| `determine_magic_square([[8,1,6],[3,5,7],[4,9,2]])` | `Is a magic square (sum is {15})`; preserves input grid |  | ![Test proof 17](partA_images/Screenshot%202026-10-02%20172900.png)<br>![Test proof 18](partA_images/Screenshot%202026-10-02%20172904.png) | Pass |
| `determine_magic_square([[1,2,3],[4,5,6],[7,8,9]])` | `Is not a magic square (not all the same sum)` |  | ![Test proof 19](partA_images/Screenshot%202026-10-02%20172909.png) | Pass |
| `prompt_user()` with input rows `8 1 6`, `3 5 7`, `4 9 2` | Returns `None`; prints prompt and magic-square result |  | ![Test proof 20](partA_images/Screenshot%202026-10-02%20172915.png)<br>![Test proof 21](partA_images/Screenshot%202026-10-02%20172921.png)<br>![Test proof 22](partA_images/Screenshot%202026-10-02%20172925.png) | Pass |
| `main()` | Calls `prompt_user()` once; returns `None` |  | ![Test proof 23](partA_images/Screenshot%202026-10-02%20172930.png)<br>![Test proof 24](partA_images/Screenshot%202026-10-02%20172933.png) | Pass |


