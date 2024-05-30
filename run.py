import random 

def create_grid(size):
    """Creates a size x size grid initialized with '~'."""
    return [['~' for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    """Prints the grid."""
    for row in grid:
        print(' '.join(row))
    print()
