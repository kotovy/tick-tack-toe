Tic-Tac-Toe Game Readme
Introduction
This is a simple implementation of the classic Tic-Tac-Toe game using the Pygame library in Python. The game features a graphical user interface with a grid of cells, where two players take turns to place their symbol (either a cross or a nought) in an attempt to align three of their symbols either horizontally, vertically, or diagonally.

Requirements
Python 3.x
Pygame library
Installation
Install Python: Download Python
Install Pygame: Open a terminal and run the following command
pip install pygame

How to Play
Run the game by executing the provided script in a Python environment.

python tic_tac_toe.py
The game window will appear with a 3x3 grid.

Click on any cell to place your symbol. The game alternates between 'Cross' and 'Nought' players.

The game continues until one player wins by forming a line of three symbols horizontally, vertically, or diagonally, or until the board is filled, resulting in a draw.

If the game ends, a message will be displayed announcing the winner or a draw.

Close the game window to exit.

Code Overview
The game uses the Pygame library to create a graphical user interface.
The board is represented as a 3x3 matrix, and players take turns updating the board.
The game checks for a winner after each move and updates the display accordingly.
The game loop continues until the player closes the window.
Customization
You can customize the size of the grid and cells by modifying the GRID_SIZE and CELL_SIZE constants.
To change the symbols used in the game, modify the CROSS and NOUGHT constants.
Feel free to modify the game's appearance and messages to suit your preferences.
Acknowledgments
This game was created using the Pygame library. Special thanks to the Pygame development team for providing a simple and effective framework for creating 2D games in Python.

Have fun playing Tic-Tac-Toe!





