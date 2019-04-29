"""

Ordered Dict

"""

from collections import OrderedDict

dictionary1 = {
    'e': 5,
    'a': 1,
    'c': 3,
    'b': 2,
    'd': 4,
}

print(dictionary1)

dictionary2 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
}

print(dictionary2)

print(dictionary1 == dictionary2)  # true

dictionary3 = OrderedDict(dictionary1)  # Ensure the insertion order of the elements of a Dictionary
dictionary4 = OrderedDict(dictionary2)

print(dictionary3 == dictionary4)  # false, because the order matters

