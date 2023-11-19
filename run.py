import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

"""
Tic Tac Toe
"""

def intro():
    """
    Introduktion with the rules of Tic Tac Toe
    """
    print("The game is played on a grid that's 3 squares by 3 squares. \n"
          "You are X or O, your friend is the other one. \n"
          "Players take turns putting their marks in empty squares. \n"
          "The first player to get 3 of her marks in a row (up, down, \n"
          "across, or diagonally) is the winner.")
    print("\n")
    input("Press enter to continue!\n")
    print("\n")


def new_grid():
    """
    This creates a empty grid
    """
    print("The new board:")
    grid = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    return grid


def lookGreat(grid):
    """
    This change look on the grid and makes it nicer
    """
    rows = len(grid)
    cols = len(grid)
    print("-----------")
    for r in range(rows):
        print(grid[r][0], " |", grid[r][1], "|", grid[r][2])
        print("-----------")
    return grid


def sym():
    """
    This decides the players symbols
    """
    symbol_1 = input("Player 1, do you want to be X or O? \n")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Player 2, you are O.")
    else:
        symbol_2 = "X"
        print("Player 2, you are X.")
    input("Press enter to continue!\n")
    print("\n")
    return (symbol_1, symbol_2)


def start(grid, symbol_1, symbol_2, count):
    """
    This starts the game
    """
    """
    Decides the turn
    """
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Player"+player+", it is your turn. ")
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, "
                    "bottom row: enter 2]:\n"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, "
                       "right column enter 2]\n"))

    """
    Checks if players' selection is out of range
    """
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, "
                        "bottom row: enter 2]:\n"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: "
                           "enter 1, right column enter 2]\n"))

    """
    Checks if the square is already filled
    """
    while (grid[row][column] == symbol_1) or (grid[row][column] == symbol_2):
        filled = illegal(grid, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, "
                        "bottom row: enter 2]:\n"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, "
                           "right column enter 2]\n"))

    """
    Locates the player's symbol on the grid
    """
    if player == symbol_1:
        grid[row][column] = symbol_1

    else:
        grid[row][column] = symbol_2

    return (grid)


def isFull(grid, symbol_1, symbol_2):
    count = 1
    winner = True
    """
    This checks if the grid is full
    """
    while count < 10 and winner == True:
        gaming = start(grid, symbol_1, symbol_2, count)
        nicer = lookGreat(grid)

        if count == 9:
            print("The playground is full. Game over!")
            if winner == True:
                print("There is a tie!")

        """
        Check if here is a winner
        """
        winner = isWinner(grid, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Game over!")

    """
    This gives a report
    """
    report(count, winner, symbol_1, symbol_2)


def outOfBoard(row, column):
    """
    This tells the players that their selection is out of range
    """
    print("Out of boarder. Pick another one.")


def isWinner(grid, symbol_1, symbol_2, count):
    """
    This checks if any one is winning
    """
    winner = True
    """
    Checks the rows
    """
    for row in range(0, 3):
        if (grid[row][0] == grid[row][1] == grid[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")

        elif (grid[row][0] == grid[row][1] == grid[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")

    """
    Checks the columns
    """
    for col in range(0, 3):
        if (grid[0][col] == grid[1][col] == grid[2][col] == symbol_1):
            winner = False
            print("Player" + symbol_1 + ", you won!")
        elif (grid[0][col] == grid[1][col] == grid[2][col] == symbol_2):
            winner = False
            print("Player" + symbol_2 + ", you won!")

    """
    Checks the diagnoals
    """
    if grid[0][0] == grid[1][1] == grid[2][2] == symbol_1:
        winner = False
        print("Player" + symbol_1 + ", you won!")

    elif grid[0][0] == grid[1][1] == grid[2][2] == symbol_2:
        winner = False
        print("Player" + symbol_2 + ", you won!")

    elif grid[0][2] == grid[1][1] == grid[2][0] == symbol_1:
        winner = False
        print("Player" + symbol_1 + ", you won!")

    elif grid[0][2] == grid[1][1] == grid[2][0] == symbol_2:
        winner = False
        print("Player" + symbol_2 + ", you won!")

    return winner


def illegal(grid, symbol_1, symbol_2, row, column):
    print("The square you picked is already filled. Pick another one.")


def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Press enter to see the game summary.\n")
    if (winner == False) and (count % 2 == 1):
        print("Winner: Player " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0):
        print("Winner: Player " + symbol_2 + ".")
    else:
        print("There is a tie.")


def main():
    """
    Run all program functions
    """
    introduktion = intro()
    grid = new_grid()
    nicer = lookGreat(grid)
    symbol_1, symbol_2 = sym()
    full = isFull(grid, symbol_1, symbol_2)


print("Welcome to Tic Tac Toe!\n")
main()
