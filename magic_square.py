import math

def estimate_square_size(first_row):
    size = len(first_row)

    if not determine_max(first_row):
        return
    grid = [first_row]

    if size < 3:
        print("Not a magic square (not a square)")
        return

    for _ in range(size - 1):
        next_row = [int(num) for num in input().split()]

        if len(next_row) != size:
            if len(next_row) > size:
                print("Not a magic square (number out of range)")
                return
            else:
                print("Not a magic square (not a square)")
                return

        grid.append(next_row)

    if not not_same_number(grid):
        return
    
    
    return grid


def determine_max(row):
    max_num = len(row) ** 2
    max_unit = max(row)
    if max_unit > max_num:
        print("Not a magic square (number out of range)")
        return False
    return True


def not_same_number(grid):
    values = [value for row in grid for value in row]
    if len(values) != len(set(values)):
        print("Not a magic square (repeated a number)")
        return False
    return True

def sum_row(grid):
    rows = []
    for row in grid:
        rows.append(sum(row))
    return rows 

def sum_column(grid):

    cols = []
    while len(grid) != 0:
        if len(grid[0]) != 0:
            for unit in grid:
                cols.append(unit[0])
                del unit[0]
        else:
            grid.clear()
    size = int(math.sqrt(len(cols)))
    org_cols = [sum(cols[i:i + size]) for i in range(0, len(cols), size)]
    return org_cols

    

def sum_diagonal(grid):
    values = [(row_index, value_index, value) for row_index, row in enumerate(grid) for value_index, value in enumerate(row)]
    values2 = [(row_index, value_index, value) for row_index, row in enumerate(grid) for value_index, value in enumerate(reversed(row))]
    diags = []
    for unit in values:
        if unit[0] == unit[1]:
            diags.append(unit[2])
    for unit in values2:
        if unit[0] == unit[1]:
            diags.append(unit[2])

    size = int(len(diags)/2)
    org_diags = [sum(diags[i:i + size]) for i in range(0, len(diags), size)]
    return org_diags

def determine_magic_square(grid):
    diag_sqr = [row.copy() for row in grid]
    row_sqr = [row.copy() for row in grid]
    col_sqr = [row.copy() for row in grid]

    sum_of_each_row = sum_row(row_sqr)
    sum_of_each_col = sum_column(col_sqr)
    sum_of_each_diag = sum_diagonal(diag_sqr)

    if set(sum_of_each_row) == set(sum_of_each_col) == set(sum_of_each_diag):
        return f"Is a magic square (sum is {set(sum_of_each_row)})"
    else:
        return "Is not a magic square (not all the same sum)"

def prompt_user():
    print("Please enter the square, separated by spaces")

    first_row = [int(num) for num in input().split()]
    sqr = estimate_square_size(first_row)
    print(determine_magic_square(sqr))

    return


def main():
    prompt_user()


if __name__ == "__main__":
    main()