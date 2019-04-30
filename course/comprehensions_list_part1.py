"""

Comprehensions - List part 1

- Using list comprehension we can generate new lists with processed data from another iterable.

# list comprehension syntax:

[ data for data in iterable ]

"""


numbers = [1, 2, 3, 4, 5]

res = [number * 10 for number in numbers]

print(res)

res2 = [number / 2 for number in numbers]

print(res2)


def power_2(value):
    return value * value


res3 = [power_2(number) for number in numbers]

print(res3)

name = 'Rodrigo Cantarino'
print([letter.upper() for letter in name])


names = ['rodrigo', 'pessoa', 'cantarino']
print([name.title() for name in names])

print([num * 3.14 for num in range(1, 11)])




