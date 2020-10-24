import random
import sys
import time

# Grid = a list.
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


# Turning the user's input into a O, and X or nothing.
def num_to_text(num):
    if (num == 0): return ' '  # If the variable = 0, then it will print out a blank(Empty?)
    if (num == 1): return 'O'  # if the array is labeled(correct term?) as 1, then it will print out a naught
    if (num == 2): return 'X'  # if the array is labeled 2 then it shall print out a crross

# Function for printing the grid.
def print_grid():
    print('┌ ─ ┬ ─ ┬ ─ ┐')
    print('│ ' + num_to_text(grid[0][0]) + ' │ ' + num_to_text(grid[1][0]) + ' │ ' + num_to_text(
        grid[2][0]) + ' │')
    print('├ ─ ┼ ─ ┼ ─ ┤')
    print('│ ' + num_to_text(grid[0][1]) + ' │ ' + num_to_text(grid[1][1]) + ' │ ' + num_to_text(
        grid[2][1]) + ' │')
    print('├ ─ ┼ ─ ┼ ─ ┤')
    print('│ ' + num_to_text(grid[0][2]) + ' │ ' + num_to_text(grid[1][2]) + ' │ ' + num_to_text(
        grid[2][2]) + ' │')
    print('└ ─ ┴ ─ ┴ ─ ┘')


# Function checks for if there's been a victory.
def check_victory():
    # Looks at each box in the grid and checks the three boxes in each specified vector.
    for i in range(0, 3):

        for j in range(0, 3):
            # If that particular spot has nothing in it, continue.
            if (grid[i][j] == 0):
                continue

            # The four ways that the program will check for the 8 possibilities of winning.
            for vector in [[1, 0], [1, 1], [0, 1],
                           [-1, 1]]:
                try:
                    box_to_check = [i, j]
                    character_to_check_for = grid[i][j]
                    for x in range(1, 3):

                        box_to_check[0] += vector[0]
                        box_to_check[1] += vector[1]

                        # Checks for the same symbols in the vectors that form a complete line.
                        # If they do, the end game is run.
                        if grid[box_to_check[0]][box_to_check[1]] != character_to_check_for:
                            break

                        # If last box in loop and still have not broken, then three in a row has been formed.
                        if (x == 2):
                            # Print character
                            return num_to_text(grid[i][j])

                except:
                    continue
    return ' '


def choose_computer_move():
    # A box with nothing in it.
    empty_boxes = []
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[i][j] == 0:
                # Creates a list of possibilities, picks at random from them.
                # (Saves time on coding each and every single possibility)
                empty_boxes += [[i,j]]
    return empty_boxes[random.randint(1, len(empty_boxes) - 1)]


time.sleep(2)

# Start of game prints - how to play.
print("Co-ordinates are in the form 1 1; where 1 1 equals the top left box.")
print("First number: where in the row. Second number: which row.")
input("Welcome to naughts and crosses, press enter to being! ")
# Player's move
while (1):
    # Repeat process until a valid input is detected and processed.
    while (1):
        move = input(" " "Your turn. Make your move:" " ")
        if len(move) == 3:
            # Check for correct input
            if 1 <= int(move[0]) <= 3 and 1 <= int(move[2]) <= 3:
                # Check that box is empty.
                if grid[int(move[0]) - 1][int(move[2]) - 1] == 0:
                    # Put a cross in box.
                    grid[int(move[0]) - 1][int(move[2]) - 1] = 2
                    print_grid()
                    break

            print("Invalid input. Try again with proper co-ordinates.")
            print("Remember, the first number indicates where the x will be in that row.")
            print("The second number dictates which row.")

    # Checks if the player has won.
    victory_result = check_victory()
    if victory_result == 'X':
        print("You've won!") # NOTE: By here, we could change it so it gives the hint for the next mini-game (etc)
        break

    # Makes the computer move.
    computerMove = choose_computer_move()
    grid[computerMove[0]][computerMove[1]] = 1
    print(" " "Computer will now take it's turn")
    print_grid()

    # Checks if the computer has won.
    victory_result = check_victory()
    if victory_result == 'O':
        print("You lost. That's a shame") # NOTE2: By here, we could have a consequence for losing. Perhaps instead of ending the game it just restarts?
        break

time.sleep(5)
sys.exit