"""
Named Tuple - We named the tuple and its parameters
"""

from collections import namedtuple

# Declaration Form 1
dog = namedtuple('dog', 'name age race')

print(dog)

# Declaration Form 2
dog = namedtuple('dog', 'name, age, race')

# Declaration Form 3
dog = namedtuple('dog', ['name', 'age', 'race'])

# Using

ray = dog(name='Ray', age=2, race='German Shepherd')

print(ray)
print(type(ray))

# Accessing the data
# Form 1
print(ray[0])
print(ray[1])
print(ray[2])

# Form 2
print(ray.name)
print(ray.age)
print(ray.race)

# Form 3
print(ray.index('Ray'))
