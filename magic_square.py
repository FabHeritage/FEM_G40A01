# def check_magic_square():
def estimate_square_size(first_row):
    grid = [first_row]
    size = len(first_row)

    if size < 3:
        print(f"{size} Unit entered, need more to create a magic square.")
        return

    for _ in range(size - 1):
        next_row = input().split()

        if len(next_row) != size:
            if len(next_row) > size:
                print(f"{len(next_row) - size} unit too many")
                return
            else:
                print(f"{size - len(next_row)} unit too little")
                return

        grid.append(next_row)

    for row in grid:
        print(row)

    return grid


def prompt_user():
    print("Please enter the square, separated by spaces")

    first_row = input().split()

    return estimate_square_size(first_row)


def main():
    prompt_user()


if __name__ == "__main__":
    main()