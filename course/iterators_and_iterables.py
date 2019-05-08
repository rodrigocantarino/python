"""

Iterators and Iterables

Iterator:
    - Is a object that can be Iterate
    - Returns a object that is a data which is one element when the next() function is called

Iterables:
    - Returns a object which is a iterator when the iter() function is called

"""

name = 'Rodrigo Cantarino'  # Is a iterable, but not a iterator
numbers = [1, 3, 5, 7, 9]  # Is a iterable, but not a iterator

it1 = iter(name)
it2 = iter(numbers)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print('_______________________________')
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
#print(next(it2))  # When the limit is passed, a StopIteration error will be thrown