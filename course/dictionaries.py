"""

Dictionaries

In other programming languages, Dictionaries are known as Maps

Dictionaries are collections defined by explicit key/value separated by colon (:)

Dictionaries are represented by braces {}

On Dictionaries we can't have repeated KEYS


"""
# Type
print(type({}))

print('------------- Example 1 -------------')
# Example 1
countries = {
    'br': 'Brazil',
    'pt': 'Portugal',
    'usa': 'United States of America',
    'ie': 'Ireland'
}

print(countries)

print('------------- Example 2 -------------')
# Example 2 (less common)
countries2 = dict(br='Brazil', pt='Portugal', usa='United States of America', ie='Ireland')

print(countries2)

print('------------- Accessing Elements -------------')

# Form 1 - By Key
print(countries['br'])
print(countries['usa'])

# If you pass a key that doesn't exists, a KeyError will be displayed
# countries['ru']

# Form 2 - By GET
print(countries.get('pt'))
print(countries.get('ie'))

# Will return as NoneType
print(countries.get('ru'))

# The second parameter set the default value when the KEY is not found. So, will return 'Not Found'.
print(countries.get('ru', 'Not found'))

print('------------- Verify if a element is in the Dictionary -------------')

# Search by Key
print('br' in countries)
print('ru' in countries)
print('Portugal' in countries)

print('------------- We can use any type as a Key of the dictionary, on this case, tuples -------------')
# We can use any type as a Key of the dictionary
locations = {
    (-15.793978, -47.882758): 'Brasília',
    (-23.545026, -46.636704): 'São Paulo',
    (-22.907411, -43.183281): 'Rio de Janeiro',
    (-3.105854, -60.017964): 'Manaus'
}

print(locations)

print('------------- Add elements in the Dictionary -------------')

incoming = {
    'jan': 6000,
    'feb': 6200,
    'mar': 5900
}

print(incoming)

# Form 1 - Most common
incoming['apr'] = 6100
print(incoming)

# Form 2
new_incoming = {'may': 5800}
incoming.update(new_incoming)  # Same as: incoming.update({'may': 5800})
print(incoming)

print('------------- Update specific element in a dictionary -------------')

# Update specific element in a dictionary
# Form 1
incoming['may'] = 5850

# Form 2
incoming.update({'apr': 6150})
print(incoming)

print('------------- Remove specific element in a dictionary -------------')

# Form 1 - Using 'pop' method ALWAYS using the KEY as parameter
# IF the KEY doesn't exists a KeyError will be displayed.
may = incoming.pop('may')  # The pop method will return the value of the informed KEY
print(may)
print(incoming)

# incoming.pop('dec') -> KeyError will be displayed.

# Form 2
# IF the KEY doesn't exists a KeyError will be displayed.
del incoming['apr']  # This form will NOT return the value of the informed KEY
print(incoming)


print('------------- Example: Shopping Cart -------------')
"""
Shopping Cart:
    Product1:
        - Name;
        - Quantity;
        - Price
    Product2:
        - Name;
        - Quantity;
        - Price
"""

cart = []

product1 = {
    'name': 'Playstation 4',
    'quantity': 1,
    'price': 3000.00
}

product2 = {
    'name': 'God of War 4',
    'quantity': 1,
    'price': 150.00
}

cart.append(product1)
cart.append(product2)

print(cart)
print('')
print('')

print('------------- Methods of Dictionaries -------------')
print(dir({}))

print('')
print('------------- Using Methods of Dictionaries -------------')

dictionary = dict(a=1, b=2, c=3)

print(dictionary)

print('------------- Copy a Dictionary to another - Deep copy -------------')
# Copy a Dictionary to another

# Form 1 - Deep copy
new_dictionary = dictionary.copy()
print(new_dictionary)

new_dictionary['d'] = 4

print(dictionary)
print(new_dictionary)

print('------------- Copy a Dictionary to another - Shallow copy -------------')
# Form 2 - Shallow copy
new_dictionary = dictionary
print(new_dictionary)

new_dictionary['d'] = 4

print(dictionary)
print(new_dictionary)

print('------------- Unusual form to create a Dictionary -------------')

# The method fromkeys always receive 2 arguments.
# First: that will became the dictionary key and can be a iterable. Second: a value to be assigned to the key.
# If the first argument is a iterable, the second parameter will be assigned to each key as a default value.

another = {}.fromkeys('a', 'b')  # Maximum of 2 arguments
print(another)
print(type(another))

user = {}.fromkeys(['name', 'email', 'profile'], 'Unknown')
print(user)
print(type(user))

another_example = {}.fromkeys('test', 'value')
print(another_example)

another_one = {}.fromkeys(range(0, 7), 'value')
print(another_one)

