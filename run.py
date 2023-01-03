"""
tic tac toe gameboard
[
    [-, -, -],
    [-, -, -],
    [-, -, -],
]

user_choice - user choose a number between 1-9
if the player chooses something else, ask them to choose again
check if the player's choice is already taken
add it to the gameboard
check if the player won, check rows, columns and diagonals
switch between users on successful moves
"""

gameboard = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def print_board(gameboard):
    for row in gameboard:
        for slot in row:
            print(f"{slot} ", end="")
        print()
print_board(gameboard)

"""
choose a number from 1-9 or press q to end the game
"""
def quit(user_choice):
    if user_choice == "q":
        print("Thanx for playing, hope to see you again soon!")
        return True
    else: return False

def check_choise(user_choice):
    if not isnum(user_choice): return False
    user_choice = int(user_choice)
    if not bounds(user_choice): return False

    return True

def isnum(user_choice):
    if not user_choice.isnumeric():
        print("This is not a valid number")
        return False
    else: return True

def bounds(user_choice):
    if user_choice > 9 or user_choice < 1:
        print("This number is out of bounds")
        return False
    else: return True

def istaken(coords, gameboard):
    row = coords[0]
    col = coords[1]
    if gameboard[row][col] != "-":
        print("This position is already taken, please choose another one.")
        return True
    else: return False

def coordinates(user_choice):
    row = int(user_choice / 3)
    col = user_choice
    if col > 2: col = int(col % 3)
    return (row,col)

while True:
    print_board(gameboard)
    user_choice = input("Please enter a position 1-9 or enter \"q\" to quit:")
    if quit(user_choice): break
    if not check_choise(user_choice):
        print("Please try one more time.")
        continue
    user_choice = int(user_choice) -1
    coords = coordinates(user_choice)
    gameboard[0][0] = "x"
    if istaken(coords, gameboard):
        print("Please try one more time.")
        continue

