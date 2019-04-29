"""
SETS

- Sets don't have duplicated values
- Sets don't have ordered values
- Values are not accessed via Index

We use SETS to store data when the values order, keys/index, values or duplicated values doesn't mater.

SETS are represented by braces {}

Difference between Sets and Maps/Dictionaries:
 - A Map/Dictionary has key:value
 - A Set has only the value

Inside a SET we can have any type of data. Int, Float, bool and tuple. But we can't have a list

A SET is iterable.
"""

print('------------- Defining a Set -------------')
# Form 1
# Even if it has on its definition repeated values, the repeated values will be ignored
s = set({1, 2, 3, 4, 5, 6, 7, 5, 3, 2, 1})

print(s)
print(type(s))

# Form 2 - Most common
s2 = {1, 2, 3, 4, 5, 3, 2}

print(s2)
print(type(s2))


print('------------- Other data types can be transformed into a SET -------------')
# Other data types can be transformed into a SET using a Python builtin function set()
strings = 'Rodrigo Cantarino'
lists = [1, 2, 3, 4, 5, 3, 2, 1]
tuples = (7, 8, 9, 10, 7, 6, 8)

print(type(strings))
print(type(lists))
print(type(tuples))

print(set(strings))
print(set(lists))
print(set(tuples))

# We can verify if a element is inside the SET

if 3 in s:
    print('s have the value 3')
else:
    print('s don\'t have the value 3')

if 55 in s:
    print('s have the value 55')
else:
    print('s don\'t have the value 55')

print('------------- Defining a Set with different data type -------------')

s = {2, 'z', True, 3.14, (7, 8, 9)}
print(s)
print(type(s))

for value in s:
    print(value)

print('------------- Interesting ways to use Sets -------------')
# Interesting ways to use Sets
# For example if we have visitors of a museum from various cities (some repeated)
# and we want to know how many cities we have.

cities = ['Brasília', 'São Paulo', 'Rio de Janeiro', 'Manaus', 'Brasília', 'Rio de Janeiro', 'Manaus']
print(f'Total of visitors: {len(cities)}')
print(f'Total of cites: {len(set(cities))}')

print('------------- Add elements on a Sets -------------')

s3 = {20, 1, 2, 3, 4, 5, 3, 2, 7, 9}

print(s3)
print(type(s3))

s3.add(10)
s3.add(17)

print(s3)

print('------------- Remove elements of a Sets -------------')

# Form 1
s3.remove(20)  # If the value is not found, a KeyError will be displayed
print(s3)

# Form 2
s3.discard(2)  # In this case, If the value is not found, no error will be displayed
print(s3)

print('------------- Copy a Set to another -------------')
s4 = s3.copy()  # Deep copy
s5 = s4  # Shallow copy
s5.add(33)

print(s4)
print(s5)

print('------------- Remove all elements of a Set -------------')
s3.clear()
print(s3)

print('------------- Mathematical Methods of a Set -------------')

prime_numbers = {1, 2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29}
odd_numbers = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21}
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22}

print('------------- Union -------------')
# Union 1 - Using union() method
uniques = prime_numbers.union(odd_numbers, even_numbers)
print(uniques)

# Union 2 - Using pipe '|'
uniques = prime_numbers | odd_numbers | even_numbers
print(uniques)

print('------------- Intersection -------------')
# Union 1 - Using intersection() method
prime_and_even = prime_numbers.intersection(even_numbers)
prime_and_odd = prime_numbers.intersection(odd_numbers)

print(prime_and_even)
print(prime_and_odd)

# Union 2 - Using &
prime_and_even = prime_numbers & even_numbers
prime_and_odd = prime_numbers & odd_numbers

print(prime_and_even)
print(prime_and_odd)

print('------------- Difference -------------')
just_even = even_numbers.difference(prime_numbers)
just_odd = odd_numbers.difference(prime_numbers)

print(just_even)
print(just_odd)

print('------------- Using Methods: Sum, Max value, Min Value, Length of a SET -------------')

# Methods: Sum, Max value, Min Value
# Works ONLY if all values are int or float
print('Even numbers')
print(sum(even_numbers.values()))
print(max(even_numbers.values()))
print(min(even_numbers.values()))

# Method: Size (length)
# Works anytime
print(len(even_numbers.values()))

print('Odd numbers')
print(sum(odd_numbers.values()))
print(max(odd_numbers.values()))
print(min(odd_numbers.values()))

# Method: Size (length)
# Works anytime
print(len(odd_numbers.values()))
