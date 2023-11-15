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

"""
Main function, calls all other functions
"""
def main():
    introduktion = intro()


main()