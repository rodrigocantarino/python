"""

Custom iterator

To create a Custom iterator, we have to create a class with the __iter__ and __next__ methods.

"""

class Counter:

    '''
        Custom iterator similar to range() function
    '''

    def __init__(self, smaller, bigger):
        self.smaller = smaller
        self.bigger = bigger

    def __iter__(self):
        return self

    def __next__(self):
        if self.smaller < self.bigger:
            sm = self.smaller
            self.smaller = self.smaller + 1
            return sm
        raise StopIteration


con = Counter(1, 3)

print(con)

it = iter(con)

print(next(it))
print(next(it))
# print(next(it))  # Will throw a StopIteration

print('_______________________________')

for c in Counter(0, 5):
    print(c)


