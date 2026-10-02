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
    values = [value for row in grid for value in row]
    

# def sum_diagonal():

def prompt_user():
    print("Please enter the square, separated by spaces")

    first_row = [int(num) for num in input().split()]
    estimate_square_size(first_row)

    return


def main():
    prompt_user()


if __name__ == "__main__":
    main()