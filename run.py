import random 

def create_grid(size):
    """Creates a size x size grid initialized with '~'."""
    return [['~' for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    """Prints the grid."""
    for row in grid:
        print(' '.join(row))
    print()

def get_grid_size():
    """Prompts the user to enter a valid grid size."""
    while True:
        try:
            size = int(input("Enter the grid size (e.g., 10 for a 10x10 grid): "))
            if size <= 0:
                raise ValueError
            return size
        except ValueError:
            print("Invalid input. Please enter a positive integer."