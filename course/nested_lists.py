"""

Nested Lists

"""

from random import random


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested_list)
print(type(nested_list))

# "Array" 3 x 3
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(nested_list[2][1])  # 8

# List comprehension
[[print(value) for value in lis] for lis in nested_list]

print('')
print('-------------------------------')
print('')

# Generate a chessboard


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


chessboard_numbered = [[number for number in range(0, 8)] for value in char_range('a', 'h')]
print(chessboard_numbered)
print('')
print('-------------------------------')
print('')
chessboard_letters = [[position for position in char_range('a', 'h')] for value in range(0, 8)]
print(chessboard_letters)

print('')
print('-------------------------------')
print('')

# Generate a empty Tic-tac-toe board
tic_tac_toe_board = [[' ' for number in range(1, 4)] for value in range(1, 4)]
print(tic_tac_toe_board)

# Generate a basic Tic-tac-toe board
tic_tac_toe_board = [['X' if not number % 2 else 'O' for number in range(1, 4)] for value in range(1, 4)]
print(tic_tac_toe_board)

# Generate a simple random Tic-tac-toe board
tic_tac_toe_board = [['X' if not random() >= 0.5 else 'O' for number in range(1, 4)] for value in range(1, 4)]
print(tic_tac_toe_board)