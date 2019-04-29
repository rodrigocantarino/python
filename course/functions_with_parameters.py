"""
Functions with parameters
"""


def square_number(num):
    return num * num


print(square_number(2))
print(square_number(10))
print(square_number(11))

print('------------------------------------')


def powered_number(num, power_to):
    return num**power_to


print(powered_number(2, 10))

# Named arguments or Key word arguments
print(powered_number(power_to=3, num=5))
