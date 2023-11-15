"""
Tic Tac Toe
"""


"""
Introduktion with the rules of Tic Tac Toe
"""
def intro():
    print("welcome to Tic Tac Toe!\n")
    print("The game is played on a grid that's 3 squares by 3 squares. "
          "You are X, your friend (or the computer in this case) is O. "
          "Players take turns putting their marks in empty squares. "
          "The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
    print("\n")
    input("Press enter to continue!")
    print("\n")


"""
This creates a empty grid
"""
def new_grid():
    print("The new board:")
    grid = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    return grid


"""
This change look on the grid and makes it nicer
"""
def lookGreat(grid):
    rows = len(grid)
    cols = len(grid)
    print("-----------")
    for r in range(rows):
        print(grid[r][0], " |", grid[r][1], "|", grid[r][2])
        print("-----------")
    return grid


"""
Main function, calls all other functions
"""
def main():
    introduktion = intro()
    grid = new_grid()
    nicer = lookGreat(grid)


"""
Call main function
"""
main()