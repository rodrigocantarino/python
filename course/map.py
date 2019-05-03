"""

Map

Used to mapping values to functions.

"""

import math


def area(r):
    """ Calculate the area of a circle """
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

print('')
print('-------------------------------')
print('')

radius = [1, 2, 3, 5, 7, 11]

# Simple codding, without map
areas = []
for r in radius:
    areas.append(area(r))

print(areas)

print('')
print('-------------------------------')
print('')

# Using map.
# map(function, iterable)
areas = map(area, radius)

print(areas)  # Map object
print(type(areas))  # Map Class
print(list(areas))  # Set to list

print('')
print('-------------------------------')
print('')

print('Using map with lambda expression:')

# Using map with lambda expression
print(list(map(lambda r: math.pi * (r ** 2), radius)))

# map(function, iterable)
# Function: f(x); Can be a common function or a lambda expression
# Iterable data: [a1, a2, a..., an]
# Return a iterable map object: f(a1), f(a2), f(a...), f(an)
# that can be cast to a list: list(map(function, iterable))

print('')
print('-------------------------------')
print('')

# Cities with temperatures in Celsius
cities = [
    ('Brasília', 22),
    ('Rio de Janeiro', 25),
    ('São Paulo', 19),
    ('Geneve', 7),
    ('New York', 7),
    ('Dublin', 11),
    ('Berlin', 5),
    ('Edinburgh', 8)
]

# Transform to Fahrenheit
# f = (9/5 * c) + 32

print(cities)

celsius_to_fahrenheit = lambda data: (data[0], (data[1] * 9/5) + 32)

cities_in_fahrenheit = list(map(celsius_to_fahrenheit, cities))

print(cities_in_fahrenheit)

