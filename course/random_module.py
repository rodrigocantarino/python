"""

Random Module

- On Python, modules are nothing more than other Python files.

See: https://docs.python.org/3/library/random.html

- Random — Generate pseudo-random numbers

"""

# Import the complete module. On this way everything of the module will be available.
# Functions, attributes, classe and so on.

# import random

# print(random.random())  # Generate a pseudo-random number between 0 and 1


# If you want to use a specific function from a module, you can just import THAT function

from random import random, uniform, randint, choice, shuffle

# random() -> Generate a pseudo-random number between 0 and 1
for n in range(10):
    print(random())

print('-------------------------------')

# uniform() -> Generate a pseudo-random number between two given numbers
for n in range(10):
    print(uniform(3, 7))  # The second parameter is a limit but is never used. On this case, 7 is not included.

print('-------------------------------')

# randint() -> Generate a pseudo-random integer number between two given numbers
for n in range(7):
    print(randint(1, 70), end=', ')  # The second parameter is a limit but is never used. On this case, 7 is not included.

print('')
print('-------------------------------')

# choice() -> Return a random element from the non-empty iterable
jankenpon_moves = ['Rock', 'Paper', 'Scissors']

print(choice(jankenpon_moves))


print('-------------------------------')

# shuffle() -> Shuffle the sequence(iterable) x in place.

cards = ['K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print(cards)
shuffle(cards)
print(cards)
