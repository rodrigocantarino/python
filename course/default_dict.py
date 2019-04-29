"""

Default Dict

When you create a dictionary we inform a default value, we can use a lambda function for that.
This default value will be used when the key is not found instead of generate a KeyError.


"""

from collections import defaultdict


dictionary = defaultdict(lambda: 0)

dictionary['name'] = 'Rodrigo'

print(dictionary)

# Do not display a key error because of the lambda function and create a new key to the dictionary
print(dictionary['do_not_exists_key'])

print(dictionary)


