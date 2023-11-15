"""
Tic Tac Toe
"""


def intro():
    """
    Introduktion with the rules of Tic Tac Toe
    """
    print("The game is played on a grid that's 3 squares by 3 squares. "
          "You are X, your friend (or the computer in this case) is O. "
          "Players take turns putting their marks in empty squares. "
          "The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
    print("\n")
    input("Press enter to continue!")
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
    symbol_1 = input("Player 1, do you want to be X or O? ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Player 2, you are O. ")
    else:
        symbol_2 = "X"
        print("Player 2, you are X. ")
    input("Press enter to continue!")
    print("\n")
    return (symbol_1, symbol_2)


def main():
    """
    Run all program functions
    """
    introduktion = intro()
    grid = new_grid()
    nicer = lookGreat(grid)
    symbol_1, symbol_2 = sym()



print("Welcome to Tic Tac Toe!\n")
main()