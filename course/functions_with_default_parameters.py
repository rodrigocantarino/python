"""

Functions with default parameters

The parameters of a function can be any data type inclusive other functions


"""


def squared_number(num=2):
    return num * num


print(squared_number())
print(squared_number(23))
print('------------------------------------')


def powered_number(num=2, power_to=2):
    return num**power_to


print(powered_number())
print(powered_number(5))
print(powered_number(2, 10))
print('------------------------------------')


def subtraction(n1, n2):
    return n1 - n2


def summ(n1, n2):
    return n1 + n2


def mat(n1, n2, operation=summ):
    return operation(n1, n2)


print(mat(1, 2))
print(mat(1, 2, subtraction))
