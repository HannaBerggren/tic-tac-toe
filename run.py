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

