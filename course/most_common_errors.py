"""

Most common errors in Python

See more on: https://docs.python.org/3/library/exceptions.html

Most common errors:

- Name error
- Syntax error
- Type error
- Index error
- Value error
- Key error
- Attribute error
- Indentation error

"""

print('-------------------------------')

# printf('Rodrigo')  # NameError: name 'printf' is not defined
# variable # NameError: name 'variable' is not defined
print('Rodrigo')  # Correct form

print('-------------------------------')

# SyntaxError
# def func:
#    print('Hello Universe')
# Correct Form
def func():
    print('Hello Universe')


func()

# None = 1  # SyntaxError: can't assign to keyword

print('-------------------------------')

# print(len(5))  # TypeError: object of type 'int' has no len()
# Correct use of len()
print(len([1, 2, 3, 5, 7, 11]))

# print('Rodrigo' + [])  # TypeError: can only concatenate str (not "list") to str
print('Rodrigo' + ' ' + 'Cantarino')

print('-------------------------------')

lis = [1, 2, 3]

# print(lis[10])  # IndexError: list index out of range
print(lis[1])

print('-------------------------------')

# print(int('Rodrigo'))  # ValueError: invalid literal for int() with base 10: 'Rodrigo'
# print(float('Rodrigo'))  # ValueError: could not convert string to float: 'Rodrigo'
print(int('42'))
print(float('42'))

print('-------------------------------')

dic = {}
# print(dic['k1'])  # KeyError: 'k1'

dic = {'k1': 'Hello Universe'}
print(dic['k1'])

print('-------------------------------')

tp = (1, 3, 5, 7, 2, 4, 6, 8)

# print(tp.len()) # AttributeError: 'tuple' object has no attribute 'len'
# print(tp.sort()) # AttributeError: 'tuple' object has no attribute 'sort'

print(tp.__len__())
print(sorted(tp))

print('-------------------------------')

'''
# IndentationError: expected an indented block
def hi():
print('Hello Universe')
'''


def hi():
    print('Hello Universe')


hi()
