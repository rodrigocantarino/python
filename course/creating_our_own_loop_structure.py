"""

Creating our own loop structure

"""


def my_for(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


my_for('Rodrigo')

print('')

numbers = [1, 3, 5, 7, 9]
my_for(numbers)
