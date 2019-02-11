"""

PEP 8 - Python Enhancement Proposals ( "Style Guide" )


Zen of Python

import this


Write python code right

[1] - Use camel case on Classes names
[2] - Use lower case names separated by underscore to functions and variables names
[3] - Use 4 spaces for indentation!!!
[4] - Blank lines
    - Use 2 blank lines between functions and classes definitions
    - Use 1 blank line between class methods
[5] - Imports
    - Imports must be always in different lines
    - Unless they are from the same Package
    - Imports must be at top of file after comments or docstrings and before any constant or global variables
[6] - Spaces in expressions and instructions
    # wrong way:
        def fun( something[ 2 ], { another: 2 } )
        def fun ( something[ 2 ], { another: 2 } )
        dict ['key'] = list [index]
        var_1    = 1
        var_10   = 1
        long_var = 5
    # right way:
        def fun(something[2], {another: 2})
        dict['key'] = list[index]
        var_1 = 1
        var_10 = 1
        long_var = 5
[7] - Always finish a instruction with a new blank line
[8] - Use 1 blank line at the end of the file
[9] - Comments
    - Multiple lines use triple "
    - Single line use triple #

"""

# import this

# wrong way:
# [5]
# import sys, os
# right way
import sys
import os

# Other use:
# from types import StringType, ListType

# If you have many imports from the same package is recommended to code like:
# from types import(
#    StringType,
#    ListType,
#    SetType
# )


# Imports must be at top of file after comments or docstrings and before any constant or global variables

# [1]


class Calculator:
    pass

# [2]


def sum():
    pass


def sum_two():
    pass


number = 4
odd_number = 5


# [3]
if 'a' in 'banana':
    print('Has the letter a')

# [4]
# See how is code in [1]

# [6] - Spaces in expressions and instructions

