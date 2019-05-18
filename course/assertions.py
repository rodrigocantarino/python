"""

Assertions

BE CAREFUL: If the script Python is executed with the flag -O, all 'assert' statements will be ignored.

"""


def sum_positives_numbers(a, b):
    assert a > 0 and b > 0, 'Both numbers must be positive.'
    return a + b


print(sum_positives_numbers(5, 6))
# print(sum_positives_numbers(5, -6))  # AssertionError: Both numbers must be positive

print('---------------------------------------')


def eat_fast_food(food):
    assert food in [
        'pizza',
        'hamburger'
        'chips',
        'ice cream',
        'hot dog',
        'candy'
    ], 'The food must be fast food!!!'
    return f"I'm eating {food}!!! :p"


print(eat_fast_food('pizza'))  # eat_fast_food(input('What am I eating? '))
# print(eat_fast_food('lasanha'))  # AssertionError: The food must be fast food!!!
