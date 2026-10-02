import math

def estimate_square_size(first_row):
    size = len(first_row)

    if not determine_max(first_row):
        return
    grid = [first_row]

    if size < 3:
        print(f"{size} Unit entered, need more to create a magic square.")
        return

    for _ in range(size - 1):
        next_row = [int(num) for num in input().split()]

        if len(next_row) != size:
            if len(next_row) > size:
                print(f"{len(next_row) - size} unit too many")
                return
            else:
                print(f"{size - len(next_row)} unit too little")
                return

        grid.append(next_row)

    if not not_same_number(grid):
        return
    
    sum_of_each_row = sum_row(grid)
    sum_of_each_col = sum_column(grid)
    print(sum_of_each_row)
    print(sum_of_each_col)
    print(sum_of_each_col == sum_of_each_row)
    return grid


def determine_max(row):
    max_num = len(row) ** 2
    max_unit = max(row)
    if max_unit > max_num:
        print(f"Entered unit:{max_unit}, biggest number you can have in your square is {max_num} since you entered {len(row)} units")
        return False
    return True


def not_same_number(grid):
    values = [value for row in grid for value in row]
    if len(values) != len(set(values)):
        print("Units should not have the same value.")
        return False
    return True

def sum_row(grid):
    rows = []
    for row in grid:
        rows.append(sum(row))
    return rows 

def sum_column(grid):
    # values = [value for row in grid for value in row]

    cols = []
    # num_of_col = math.sqrt(len(values))
    while len(grid) != 0:
        if len(grid[0]) != 0:
            for index,unit in  enumerate(grid):
                # print(index, unit[0])
                cols.append(unit[0])
                del unit[0]
        else:
            grid.clear()
    size = int(math.sqrt(len(cols)))
    print(size)         
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
    estimate_square_size(first_row)

    return


def main():
    prompt_user()


if __name__ == "__main__":
    main()