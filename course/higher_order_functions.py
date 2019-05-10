"""

Higher Order Functions - HOF

When a programming language support HOF, we can have functions that returns functions or we can pass functions as
parameter to the function or even we can create variables that is a function type.

"""

from random import choice

def sum_numbers(a, b):
    return a + b


def subtraction_numbers(a, b):
    return a - b


def times_numbers(a, b):
    return a * b


def division_numbers(a, b):
    return a / b


def calculation(n1, n2, func):
    return func(n1, n2)


print(calculation(3, 2, sum_numbers))
print(calculation(3, 2, subtraction_numbers))
print(calculation(3, 2, times_numbers))
print(calculation(3, 2, division_numbers))


print('------------------------------------')
print('------------------------------------')

# Nested Functions or Inner Functions


def greetings(person):
    def humor():
        return choice(('Whatzup!?', 'Fuck off!!!!', 'Hey! I like you!!!', 'Yo Bro!!!'))
    return humor() + ' ' +person


print(greetings('Rodrigo'))
print(greetings('Pessoa'))
print(greetings('Cantarino'))


print('------------------------------------')
print('------------------------------------')


def make_me_laugh():
    def laugh():
        return choice(('kkkkkk', 'lol', 'auhauhauhauhauhauhauhauha'))
    return laugh


laughing = make_me_laugh()

print(laughing())


print('------------------------------------')
print('------------------------------------')

# Inner functions can access the external functions scope


def make_me_laugh_again(person):
    def laughing():
        l = choice(('zauhahzauhzuahuzazhahzauzauhza', 'lololololololololo', 'jajajajajajajajajaja'))
        return f'{l} {person} '
    return laughing

laughing_hard = make_me_laugh_again('Rodrigo')

print(laughing_hard())
print(laughing_hard())
print(laughing_hard())
