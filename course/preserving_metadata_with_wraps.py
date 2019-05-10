"""

Preserving Metadata with Wraps


Metadata -> is a set of data that describes and gives information about other data.

Wraps -> A wrapper function is a subroutine in a software library or a computer program whose main purpose is to call a
second subroutine or a system call with little or no additional computation. Wrapper functions can be used as an
interface to adapt to the existing codes, so as to save you from modifying your codes back and forth.
For example, a Decorator is a Wrap.


"""

from functools import wraps

# Problem 1


def see_log(func):
    def login(*args, **kwargs):
        """
        I'm a function inside another one.
        :param args:
        :param kwargs:
        :return:
        """
        print(f"You are calling the function {func.__name__}")
        print(f"Function Documentation: {func.__doc__}")
        return func(*args, **kwargs)
    return login


@see_log
def summ(a, b):
    """
    Sum two numbers
    :param a:
    :param b:
    :return: a + b
    """
    return a + b


print(summ(10, 15))

print('------------------------------------')

# On this case, the metadata from the summ() function is been altered by its decorator
print(summ.__name__)
print(summ.__doc__)


print('------------------------------------')

# Solving the problem above
# We have to import the wraps -> from functools import wraps


def see_log2(func):
    @wraps(func)  # This single line solve our problem
    def login(*args, **kwargs):
        """
        I'm a function inside another one.
        :param args:
        :param kwargs:
        :return:
        """
        print(f"You are calling the function {func.__name__}")
        print(f"Function Documentation: {func.__doc__}")
        return func(*args, **kwargs)
    return login


@see_log2
def summ2(a, b):
    """
    Sum two numbers
    :param a:
    :param b:
    :return: a + b
    """
    return a + b


print(summ2(10, 25))

print('------------------------------------')

print(summ2.__name__)
print(summ2.__doc__)

print('------------------------------------')
print('------------------------------------')

print(help(summ2))
