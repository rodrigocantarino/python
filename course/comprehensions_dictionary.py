"""

Dictionary comprehension


Syntax:

{key: value for value in iterable}

"""
# Using a dictionary
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

power_2 = {key: value ** 2 for key, value in numbers.items()}
print(power_2)

print('')
print('-------------------------------')
print('')

# Using a list. Works the same way with tuples and sets
numbers = [1, 2, 3, 4, 5]
numbers = (1, 2, 3, 4, 5)
numbers = {1, 2, 3, 4, 5}

power_2 = {value: value ** 2 for value in numbers}
print(power_2)

print('')
print('-------------------------------')
print('')

keys = 'abcde'
values = 1, 2, 3, 4, 5

mix = {keys[i]: values[i] for i in range(0, len(keys))}
print(mix)

print('')
print('-------------------------------')
print('')

numbers = [1, 2, 3, 4, 5]
res = {num: ('even' if not num % 2 else 'odd') for num in numbers}
print(res)
