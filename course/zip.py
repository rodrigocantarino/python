"""

ZIP - create an iterable zip object and take iterables (can be zero or more),
makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.

We can use all types of iterators mixed on zip()

"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]

zip1 = zip(list1, list2)

print(zip1)
print(type(zip1))
print(list(zip1))

zip2 = zip(list1, list2, 'abc')
print(tuple(zip2))

print('')
print('-------------------------------')
print('')

zip3 = zip(list1, list2, (7, 8, 9))
print(set(zip3))

print('')
print('-------------------------------')
print('')

zip4 = zip('abc', list2)
print(dict(zip4))

print('')
print('-------------------------------')
print('')

list3 = [7, 8, 9, 10, 11]

# The zip func uses as parameter the smaller length between the iterables. It will not use the "extra" values.
zip5 = zip(list1, list2, list3)
print(list(zip5))

print('')
print('-------------------------------')
print('')

# Mixing Types
t1 = [1, 2, 3]
t2 = (4, 5, 6)
t3 = {7, 8, 9}
t4 = {'a': 10, 'b': 11, 'c': 12}

res_mix = zip(t1, t2, t3, t4.values())
print(list(res_mix))

print('')
print('-------------------------------')
print('')

# List of tuples
print(list(zip(*[(1, 2), (3, 4), (5, 6)])))  # Using the unpacker sign (*)

print('')
print('-------------------------------')
print('')

# More complex sample

test1 = [98, 85, 77]
test2 = [92, 78, 87]
students = ['Rodrigo', 'Pessoa', 'Cantarino']

final = {data[0]: max(data[1], data[2]) for data in zip(students, test1, test2)}

print(final)

# Using map()

final2 = zip(students, map(lambda score: max(score), zip(test1, test2)))

# print(list(final2))
print(dict(final2))
