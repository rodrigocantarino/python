"""
Tuples

They are like lists, but there are two basic differences:

1 - They are represented by parentheses
2 - They are immutable, in other words, they can't change after it's creation. Every operation
    with a tuple generate another tuple.

"""
print('------------- Tuple -------------')
print(type(()))

print('------------- Tuple1 -------------')
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))

print('------------- Tuple2 -------------')
tuple2 = 6, 7, 8, 9, 10
print(tuple2)
print(type(tuple2))

# Be careful with tuples with one element

print('------------- Tuple3 -------------')
tuple3 = (11)  # this isn't a tuple
print(tuple3)
print(type(tuple3))

print('------------- Tuple4 -------------')
tuple4 = (12,)  # this is a tuple
print(tuple4)
print(type(tuple4))

print('------------- Tuple5 -------------')
tuple5 = 13,
print(tuple5)
print(type(tuple5))

# Conclusion: tuples are defined by comma and not by parentheses

# We can generate a tuple with range(begin, end, step)
print('------------- Tuple6 -------------')
tuple6 = tuple(range(11))
print(tuple6)
print(type(tuple6))

# Tuple unpack
print('------------- Tuple7 -------------')
tuple7 = ('Rodrigo', 'Pessoa Cantarino de Oliveira')
name, surname = tuple7
print(name)
print(surname)
print(type(name))
print(type(surname))

# This will generate a ValueError if the number of elements in the tuple is different of the number of variables

# Methods to add or remove elements doesn't exist because tuples are immutable

# Methods: Sum, Max value, Min Value
# Works ONLY if all values are int or float
print('------------- Tuple8 -------------')
tuple8 = (1, 2, 3, 4, 5)
print(tuple8)
print(sum(tuple8))
print(max(tuple8))
print(min(tuple8))

# Method: Size (length)
# Works anytime
print(len(tuple8))

# Concatenation generates another tuple because tuples are immutable
print('------------- Tuple Concatenation -------------')
tuple9 = (1, 2, 3)
tuple10 = (4, 5, 6)

print(tuple9 + tuple10)
print(tuple9)
print(tuple10)

# To change a tuple value you have to overwrite the tuple
tuple9 = tuple9 + tuple10
print(tuple9)

print('------------- Tuple value Verification -------------')
# Verify if a element is inside the tuple
print(3 in tuple9)
print(3 in tuple10)

print('------------- Tuple Iteration -------------')
for n in tuple9:
    print(n)

print('-------------')

for index, value in enumerate(tuple9):
    print(index, value)

print('------------- Count elements inside a Tuple  -------------')
tuple11 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tuple11.count('a'))
print(tuple11.count('b'))
print(tuple11.count('c'))

print('-------------')

full_name = tuple('Rodrigo Pessoa Cantarino de Oliveira')
print(full_name)
print(full_name.count('a'))

print('------------- Hints on Tuple  -------------')
# We should use Tuples ALWAYS when we don't need to change the data collection

# Example 1

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# How to access elements
print(months)
print(months[3])

print('-------------')

i = 0
while i < len(months):
    print(months[i])
    i = i + 1

print('-------------')

# Verify in which index a element is
print(months.index('December'))

# If the element isn't in the tuple, a ValueError will be displayed

print('------------- Slicing -------------')
# Slicing
# tuple[begin, end, step]
print(months[5:])
print(months[2:6])
print(months[1:9:3])

'''

Why use tuples?

1 - Performance. They are faster than lists
2 - Tuples make the code more safe. Because is an immutable set of data.

'''

print('------------- Copy -------------')

months2 = months  # Here we don't have the problem of 'Shallow copy'

print(months)
print(months2)

more_months = ('Jan', 'Feb', 'Mar')

new_months = months + more_months

print(new_months)

print(months)
print(months2)
print(more_months)
print(new_months)
