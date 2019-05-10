"""

Decorators signatures

"""


def scream(func):  # This is a Decorator Function
    def to_raise(name):
        return func(name).upper()
    return to_raise


@scream  # This is a Decorator
def greetings(name):
    return f"Hi! I am {name}."


@scream
def order(main, side_dish):
    return f"I would like {main} and {side_dish} please!"


# Test 1
print(greetings('Rodrigo'))

print('------------------------------------')

# Test 2
# print(order('Fish', 'Chips'))  # In this case, a TypeError will be thrown.
# So we have to refactor using a Decorator Pattern

print('------------------------------------')
print('------------------------------------')


def scream2(func):  # This is a Decorator Function
    def to_raise(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return to_raise


@scream2  # This is a Decorator
def greetings(name):
    return f"Hi! I am {name}."


@scream2
def order(main, side_dish):
    return f"I would like {main} and {side_dish} please!"


print(greetings('Rodrigo'))
print(order('Fish', 'Chips'))

# A function signature is represented by its name, parameter and return


print('------------------------------------')
print('------------------------------------')


# Decorators with arguments


def verify_first_argument(value):
    def internal(func):
        def anotherone(*args, **kwargs):
            if args and args[0] != value:
                return f"Invalid value! The first argument must be equal {value}"
            return func(*args, **kwargs)
        return anotherone
    return internal


@verify_first_argument('pizza')
def favorite_food(*args):
    print(args)


@verify_first_argument(10)
def sum_10(num1, num2):
    return num1 + num2


# Test Decorators with arguments

print(sum_10(10, 12))
print(sum_10(1, 16))

print('------------------------------------')

print(favorite_food('pizza', 'barbecue'))
print(favorite_food('sandwich', 'pizza'))
