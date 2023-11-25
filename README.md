# Tic-Tac-Toe

Tic-Tac-Toe is a Python terminal game, which runs in the Code institute mock terminal on Heroku

Users can play 1v1 against each other in this classic version of Tic Tac Toe.

[Here is the live version](https://fekadon-tictactoe-31e8140a6902.herokuapp.com/)

## How to play

Tic-Tac-Toe is based on the classic game that was first played in the Roman Empire, around the first century BC. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe)

In this version, player 1 chooses X or O and player 2 get the other. You then face of against each other to try and get 3 in a row.

The rules are as follow. They are also listed at the start of the game.

- The game is played on a grid that's 3 squares by 3 squares
- You are X or O, your friend is the other one
- Players take turns putting their marks in empty squares
- The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner

## Features

### Existing Features

- Board generation
    - Creates a new playground at the start of the game

![Board generation](https://fekadon.github.io/tictactoe/media/features_first.png)

- Play 1v1 against each other
    - X or O options for players to choose

![Play against each other](https://fekadon.github.io/tictactoe/media/features_second.png)

- Input validation and error checking
    - You can not enter coordinates outside the size of the grid
    - You can not enter the same coordinates twice

![Input validation](https://fekadon.github.io/tictactoe/media/features_third.png)

### Future Features

- Allow players to play against a random AI, and not just each other
- Check if letters are used instead of numbers. Right now it crashes the game.

## Testing

I have manuelly tested this project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
- Tested in my local terminal and the Code Institute Heroku terminal

## Bugs

### Solved Bugs

- No solved bugs

### Remaining Bugs

- Writing letters instead of numbers in the console crashes the game
- Leaving the row empty and not entering anything crashes the game

### Validator Testing

- PEP8
    - Error was found in 5 places of the code using the PEP8online.com validator
    - Ignored the suggested changes because the game won't work with them

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on Deploy

## Credits

- Code Institute for the deployment terminal
- Wikipedia for the details of the Tic-Tac-Toe game