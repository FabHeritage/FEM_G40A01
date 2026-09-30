# def check_magic_square():
def estimate_square_size(first_row):
    grid = []

    for index, _ in enumerate(first_row):
        pass
    if index < 2:
        print (f"{index} Unit entered, need more to create a magic square.")
        return
    grid.append(first_row)
    
    for _ in range(index):
        next_row = input().split()
        row_size = len(next_row)-1 
        if not row_size == index:
            if row_size > index:
                print(f"{row_size-index} unit too many")
                return
            else:
                print(f"{index-row_size} unit too little")
                return
            
        else:
            grid.append(input().split())
            print("row added")
            
            
    for row in grid: print(row)

def prompt_user():
    print("Please enter the square, separated by spaces")
    
    first_row = input().split(" ")
    
    return estimate_square_size(first_row)
    





def main():
    prompt_user()

if __name__ == "__main__":
    main()