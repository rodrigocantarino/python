"""

Generators advanced

- Generators are iterators
- But not all iterator is a generator
- Generators can be created by functions
- Generator functions uses the reserved word yield
- Generators can be created by expressions


Differences between Functions and Generator Functions:
--------------------------------------------------------------------------
|         Functions                |        Generator Functions          |
--------------------------------------------------------------------------
| Uses return                      | Uses yield                          |
--------------------------------------------------------------------------
| Only one return                  | Can yield more than once            |
--------------------------------------------------------------------------
| When executed, returns one value | When executed, returns a generator  |
--------------------------------------------------------------------------


"""

# Generator Function Sample


def count_until(max_value):
    counter = 1
    while counter <= max_value:
        yield counter
        counter = counter + 1


gen = count_until(10)

print(type(gen))
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

print(list(gen))
print(tuple(gen))
