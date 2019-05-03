"""

Any and All

all() -> return True if all elements of the iterable are True or if the iterable is empty

any() -> return True if any element of the iterable is True. If the iterable is empty return False

"""

print(all([0, 1, 2, 3, 4, 5]))  # return False

print(all([1, 2, 3, 4, 5]))  # return True

print(all([]))  # return True

names = ['Rodrigo', 'Robert', 'Ronald', 'Richard', 'Rambo']

print(all([name[0] == 'R' for name in names]))  # return True

names = ['Rodrigo', 'Robert', 'Ronald', 'Richard', 'Rambo', 'Daniel']

print(all([name[0] == 'R' for name in names]))  # return False


print('')
print('-------------------------------')
print('')


print(any([0, 1, 2, 3, 4, 5]))  # return True

print(any([0, False, [], (), {}]))  # return False

print(any([0, False, [], (), {}, 1]))  # return True


