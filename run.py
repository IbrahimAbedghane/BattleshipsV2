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

def place_ship(grid, size, ship_size):
    """Randomly places a ship of ship_size on the grid."""
    while True:
        orientation = random.choice(['H', 'V'])
        if orientation == 'H':
            row = random.randint(0, size - 1)
            col = random.randint(0, size - ship_size)
            if all(grid[row][c] == '~' for c in range(col, col + ship_size)):
                for c in range(col, col + ship_size):
                    grid[row][c] = 'S'
                break
        else:
            row = random.randint(0, size - ship_size)
            col = random.randint(0, size - 1)
            if all(grid[r][col] == '~' for r in range(row, row + ship_size)):
                for r in range(row, row + ship_size):
                    grid[r][col] = 'S'
                break  

def make_guess(grid, size):
    """Prompts the user to make a valid guess."""
    while True:
        try:
            guess = input(f"Enter your guess (row,col) between 0 and {size-1}: ")
            row, col = map(int, guess.split(','))
            if row < 0 or row >= size or col < 0 or col >= size:
                raise ValueError("Guess out of grid bounds.")
            if grid[row][col] in ('X', 'O'):
                raise ValueError("You've already guessed that position.")
            return row, col
        except ValueError as e:
            print(f"Invalid guess: {e}. Please enter row and column as two integers separated by a comma.")

        def check_guess(grid, row, col):
    """Checks if the guess is a hit or miss."""
    if grid[row][col] == 'S':
        grid[row][col] = 'X'
        return True
    elif grid[row][col] == '~':
        grid[row][col] = 'O'
    return False

def all_ships_sunk(grid):
    """Checks if all ships on the grid have been sunk."""
    return all(cell != 'S' for row in grid for cell in row)

def main():
    """Main function to run the Battleships game."""
    print("Welcome to Battleships!")
    grid_size = get_grid_size()
    player_grid = create_grid(grid_size)
    computer_grid = create_grid(grid_size)

    # Place ships for player and computer
    for _ in range(5):  # Example: Place 5 ships of size 3
        place_ship(player_grid, grid_size, 3)
        place_ship(computer_grid, grid_size, 3)

    print("Your grid:")
    print_grid(player_grid)

    while True:
        # Player's turn
        print("Your turn:")
        row, col = make_guess(computer_grid, grid_size)
        hit = check_guess(computer_grid, row, col)
        print(f"{'Hit!' if hit else 'Miss!'}")
        print("Computer's grid:")
        print_grid([['~' if cell == 'S' else cell for cell in row] for row in computer_grid])

        if all_ships_sunk(computer_grid):
            print("Congratulations! You sank all the computer's ships!")
            break

        # Computer's turn (random guess)
        print("Computer's turn:")
        while True:
            row, col = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
            if player_grid[row][col] not in ('X', 'O'):
                break
        hit = check_guess(player_grid, row, col)
        print(f"Computer guessed ({row}, {col}) and it was a {'Hit!' if hit else 'Miss!'}")
        print("Your grid:")
        print_grid(player_grid)

        if all_ships_sunk(player_grid):
            print("Game over! The computer sank all your ships.")
            break

if _name_ == "_main_":
    main()