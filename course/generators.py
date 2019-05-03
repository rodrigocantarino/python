"""

Generators



print('')
print('-------------------------------')
print('')

print(getsizeof('Rodrigo'))

print(getsizeof(res1))
print(getsizeof(res2))  # Less memory used

print('')
print('-------------------------------')
print('Complete sample about memory use: ')

# List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Dictionary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Generator expression
gen = getsizeof(x * 10 for x in range(1000))

print(f"Memory used by List Comprehension: {list_comp} bytes")
print(f"Memory used by Set Comprehension: {set_comp} bytes")
print(f"Memory used by Dictionary Comprehension: {dict_comp} bytes")
print(f"Memory used by Generator expression: {gen} bytes")  # almost nothing comparing with the other above


"""

# Return the bytes used in memory by a variable
from sys import getsizeof

names = ['Rodrigo', 'Robert', 'Ronald', 'Richard', 'Rambo', 'Daniel']

# This sample use List Comprehension
print(any([name[0] == 'R' for name in names]))

# List Comprehension
res1 = [name[0] == 'R' for name in names]
print(type(res1))

print('')
print('-------------------------------')
print('')

# This sample use Generator
print(name[0] == 'R' for name in names)

print(any(name[0] == 'R' for name in names))

# Generator -> Is faster than List Comprehension
res2 = (name[0] == 'R' for name in names)
print(type(res2))

print('')
print('-------------------------------')
print('')

# The Generator Expression is iterable
gen = (x * 10 for x in range(10))
print(gen)
print(type(gen))

for number in gen:
    print(number)
