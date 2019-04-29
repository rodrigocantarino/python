"""

Conditionals structures:
- if
- else
- elif = else if


"""


condition = False
even = 22
odd = 33


if condition:
    print('Condition = True')
else:
    print('Condition = False')


if even % 11 == 0:
    print(f'Even = {even} and is 11 multiple')
elif even % 2 == 0:
    print(f'Even = {even}')
else:
    print(f'Even = {even} and is odd')

if odd % 11 == 0:
    print(f'odd = {odd} and is 11 multiple')
elif odd % 2 == 1:
    print(f'Odd = {odd}')
else:
    print(f'odd = {odd} and is even')
