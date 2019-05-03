"""

Lambda expressions are functions without a name or anonymous functions


"""

# Normal function


def func(x):
    return 3 * x + 1


print(func(5))

# Lambda expression of the function above
lambda x: 3 * x + 1

# Use 1
calc = lambda x: 3 * x + 1

print(calc(5))


print('')
print('-------------------------------')
print('')


full_name = lambda first_name, surname: first_name.strip().title() + ' ' + surname.strip().title()


print(full_name(' rodrigo   ', 'cAnTaRiNo '))

print('')
print('-------------------------------')
print('')

# "True" use of lambda expressions

authors = [
    'Isaac Asimov', 'J. R. R. Tolkien', 'Douglas Adams', 'Jim Butcher', 'Walter Scott', 'George R. R. Martin',
    'H. G. Wells', 'N. K. Jemisin', 'Neil Gaiman', 'J. K. Rowling'
]

print(authors)

# Sort by surname
authors.sort(key=lambda surname: surname.split(' ')[-1].lower())

print(authors)

print('')
print('-------------------------------')
print('')

# Quadratic function
# f(x) = a * x**2 + b * x + c


def generate_quadratic_function(a, b, c):
    """ Return f(x) = a * x**2 + b * x + c """
    return lambda x: a * x**2 + b * x + c


test = generate_quadratic_function(2, 4, -7)

print(type(test))

# x = 0
print(test(0))
# x = 3
print(test(3))
# x = 5
print(test(5))

# x = 2, a = 7, b = -9, c = 1
print(generate_quadratic_function(7, -9, 1)(2))
