"""

Function with return

"""

from random import random


def return_plus_five(param):
    return param + 5


print(return_plus_five(5))

print(return_plus_five(15))

print('------------------------------------')


def square_number(num):
    return num * num


print(square_number(5))
print(square_number(7))


print('------------------------------------')


def return_multiple_values():
    return 1, 3, 5, 7


print(return_multiple_values())  # Return a tuple
print(type(return_multiple_values()))
n1, n3, n5, n7 = return_multiple_values()  # Unpack the returned values
print(n1, n3, n5, n7)

print('------------------------------------')


def play_coin():
    if random() > 0.5:
        return 'heads'
    return 'tails'


print(play_coin())

