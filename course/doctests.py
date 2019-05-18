"""

Doctests

To execute the test go to the terminal and type: python3 -m doctest -v <file_name>.py

# Output:

7
Trying:
    summ(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.summ
1 tests in 2 items.
1 passed and 0 failed.
Test passed.


"""


def summ(a, b):
    """Sum the numbers 'a' and 'b'

    >>> summ(1, 2)
    3
    """
    return a + b


# print(summ(3, 4))

# To execute the test on terminal: python3 -m doctest -v doctests.py


def say_hi():
    """

    >>> say_hi()
    'Hi'
    """
    return "Hi"


