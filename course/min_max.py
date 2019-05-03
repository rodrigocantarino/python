"""

Min and Max

max() return the bigger value from a iterable or the bigger value from N elements
min() return the smaller value from a iterable or the smaller value from N elements

The value can be int, float, string, chars

Example: max([1, 2, 3, 4, ..., n]) or max(1, 2, 3, 4, ..., N)



"""

# Works the same way on Lists, Tuples and Sets
numbers_l = [1, 6, 3, 2, 9, 7, 8, 5, 4]
numbers_t = (1, 6, 3, 2, 9, 7, 8, 5, 4)
numbers_s = {1, 6, 3, 2, 9, 7, 8, 5, 4}

# MAX
print(max(numbers_l))
# MIN
print(min(numbers_l))

# On Dictionaries
numbers_d = {'a': 1, 'b': 6, 'c': 3, 'd': 2, 'e': 9, 'f': 7, 'g': 8, 'h': 5, 'i': 4}

# MAX by Key
print(max(numbers_d))
# MAX by value
print(max(numbers_d.values()))

# MIN by Key
print(min(numbers_d))
# MIN by value
print(min(numbers_d.values()))


print('')
print('-------------------------------')
print('')

# Between two values
print(max(3, 55))
print(min(3, 55))

print('')
print('-------------------------------')
print('')

names = ['Rodrigo', 'Pessoa', 'Cantarino', 'De', 'Oliveira']

# Alphabetic order
print(max(names))
print(min(names))

# Size order
print(max(names, key=lambda name: len(name)))
print(min(names, key=lambda name: len(name)))

print('')
print('-------------------------------')
print('')

musics = [
    {'title': "Sa'eed", 'artist': 'Infected Mushroom', 'album': 'Legend Of The Black Shawarma', 'plays': 20},
    {'title': 'Dogs', 'artist': 'Pink Floyd', 'album': 'Animals', 'plays': 17},
    {'title': 'Xxplosive', 'artist': 'Dr. Dre', 'album': 'Chronic 2001', 'plays': 13},
    {'title': 'The Unforgiven II', 'artist': 'Metallica', 'album': 'Reload', 'plays': 7},
    {'title': 'Welcome To The Jungle', 'artist': "Guns 'n Roses ", 'album': "Live Era '87 - '93 - CD 1", 'plays': 5}
]

print(max(musics, key=lambda music: music['plays']))
print(min(musics, key=lambda music: music['plays']))

# Print just the title
print(max(musics, key=lambda music: music['plays'])['title'])
print(min(musics, key=lambda music: music['plays'])['title'])
