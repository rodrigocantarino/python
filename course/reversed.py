"""

Reversed

We can use reversed() in any iterable, but always return a object list_reverseiterator with
reversed order of the elements.
Differently from .reverse() function that is used only on Lists.


"""

lis = [1, 2, 3, 4, 5]

print(lis)
print(lis.reverse())

lis = [1, 2, 3, 4, 5]

res = reversed(lis)

print(res)
print(type(res))

print(list(reversed(lis)))
print(tuple(reversed(lis)))
print(set(reversed(lis)))  # On this case, there is no order because of the nature of the SET structure

for letter in reversed('Rodrigo Cantarino'):
    print(letter, end='')

print('')
print('')

# The same but without for
print(''.join(list(reversed('Rodrigo Cantarino'))))
# Or
print('Rodrigo Cantarino'[::-1])
