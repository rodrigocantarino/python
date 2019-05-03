"""

Sorted

We can use sorted() in any iterable, but always return a List with ordered elements.
Differently from .sort() function that is used only on Lists.

Using sorted with a dictionary we have to say which key will be used and the returned data will be a dictionary ordered
by the passed key.

sorted() function returns a NEW iterable sorted, in other words,
it doesn't change the original iterable order of elements.

Differently of sort() function that changes the List iterable permanently.

"""


numbers = [1, 6, 3, 2, 9, 7, 8, 5, 4]

print('Using sorted(): ')
print(numbers)
print(sorted(numbers))
print(numbers)

print('')
print('-------------------------------')
print('')
print('Using numbers.sort(): ')
numbers.sort()
print(numbers)

print('')
print('-------------------------------')
print('')

numbers_tuple = (1, 6, 3, 2, 9, 7, 8, 5, 4)
print(numbers_tuple)
print(sorted(numbers_tuple))

numbers_set = {1, 6, 3, 2, 9, 7, 8, 5, 4}
print(numbers_set)
print(sorted(numbers_set))


print('')
print('-------------------------------')
print('')
print('Using other parameters: ')

# Using other parameters

numbers = [1, 6, 3, 2, 9, 7, 8, 5, 4]

print(numbers)
print(sorted(numbers, reverse=True))

print('')
print('-------------------------------')
print('')

# More complex use of sorted()

users = [
    {'username': 'Rodrigo', 'posts': ['Astronomy', 'Science', 'Programming', 'Memes'], 'colour': 'black'},
    {'username': 'Pessoa', 'posts': ['Astro Physics', 'Data Science', 'PHP', 'Memes']},
    {'username': 'You', 'posts': [], 'colour': 'green'},
    {'username': 'Oliveira', 'posts': ['Politics', 'Philosophy', 'Authors']},
    {'username': 'Cantarino', 'posts': ['Nature', 'Dogs'], 'colour': 'blue'},
    {'username': 'Me', 'posts': ['Nothingness']}

]

print(users)

print(sorted(users, key=len))

print(sorted(users, key=lambda user: user['username']))

print(sorted(users, key=lambda user: len(user['posts'])))

print(sorted(users, key=lambda user: user['username'], reverse=True))

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

# Order by Plays
# Less played to most played
print(sorted(musics, key=lambda music: music['plays']))

# Most played to less played
print(sorted(musics, key=lambda music: music['plays'], reverse=True))

