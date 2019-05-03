"""

Len, Abs, Sum and Round

len() -> return the length of an iterable or the number of elements.
abs() -> return the absolute value of a int or float. In other word without a sign. (-1 -> 1, -55.1 -> 55.1). AKA module
sum() -> return the sum of the elements of an iterable. This function can have a initial value.
round() -> return a round number from a float with N precision decimal digits. By default, there is no decimal digits.
Round UP when >= 0.6
Round DOWN when <= 0.6


"""

print(len('Rodrigo Cantarino'))  # Size of the string
print('Rodrigo Cantarino'.__len__())  # The same as above
print(len([1, 2, 3, 4, 5, 6, 7]))  # Quantity of elements of the list/tuple/set/dictionary
print([1, 2, 3, 4, 5, 6, 7].__len__())  # The same as above

print('')
print('-------------------------------')
print('')

print(abs(55.1))
print(abs(-55.1))

print('')
print('-------------------------------')
print('')

print(sum([1, 2, 3, 4, 5, 6, 7]))  # This works with list/tuple/set
print(sum([1, 2, 3, 4, 5, 6, 7], 5))
print(sum([1, 2, 3, 4, 5, 6, 7], -8))  # For example this initial value can be a TAX.

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}.values()))  # Dictionary

print('')
print('-------------------------------')
print('')

pi = 3.14159265359

print(round(pi))
print(round(pi, 2))
print(round(pi, 3))
print(round(pi, 4))