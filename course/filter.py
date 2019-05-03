"""

Filter

filter() -> filter data from a data collection and return a data set with the data according to the function condition.


"""

import statistics

"""
values = 1, 2, 3, 4, 5, 6, 7
average = (sum(values) / len(values))
print(average)
"""

data_set = [1.3, 2.2, 5.3, 7.1, -1.9, 6.6, 4.9]

average_value = statistics.mean(data_set)

print('')
print(f'Average value: {average_value}')

# Using filter.
# filter(function, iterable)

above_average = filter(lambda x: x > average_value, data_set)
below_average = filter(lambda x: x < average_value, data_set)

print('Above average: ')
print(list(above_average))
print('Below average: ')
print(list(below_average))

print('')
print('-------------------------------')
print('')

countries = ['', 'Brazil', '', 'England', '', 'Germany', '', 'Ireland', '', 'Scotland', '', 'USA', 'Switzerland', 0]

print(countries)

# Best way to do it
res = filter(None, countries)

print('')
print(list(res))

countries = ['', 'Brazil', '', 'England', '', 'Germany', '', 'Ireland', '', 'Scotland', '', 'USA', 'Switzerland', '']

res2 = filter(lambda country: len(country) > 0, countries)

print('')
print(list(res2))

countries = ['', 'Brazil', '', 'England', '', 'Germany', '', 'Ireland', '', 'Scotland', '', 'USA', 'Switzerland', 0]

res3 = filter(lambda country: country != '' and country != 0, countries)

print('')
print(list(res3))

print('')
print('-------------------------------')
print('-------------------------------')
print('')

users = [
    {'username': 'Rodrigo', 'posts': ['Astronomy', 'Science', 'Programming', 'Memes']},
    {'username': 'Pessoa', 'posts': ['Astro Physics', 'Data Science', 'PHP', 'Memes']},
    {'username': 'Cantarino', 'posts': ['Nature', 'Dogs']},
    {'username': 'Oliveira', 'posts': ['Politics', 'Philosophy', 'Authors']},
    {'username': 'Me', 'posts': ['Nothingness']},
    {'username': 'You', 'posts': []}
]

print(users)

# Filter inactive users

print('')
print('-------------------------------')
print('inactive users')
print('')

# inactive = list(filter(lambda u: len(u['posts']) == 0, users))
inactive = list(filter(lambda u: not u['posts'], users))  # the same
print(inactive)

# Filter users with less than 3 posts
print('')
print('-------------------------------')
print('users with less than 3 posts')
print('')

less_than_3 = list(filter(lambda u: len(u['posts']) < 3, users))
print(less_than_3)

print('')
print('-------------------------------')
print('-------------------------------')
print('')

# Match filter() and map()

print('')
print('-------------------------------')
print('Match filter() and map():')
print('')

names = ['Rodrigo', 'Pessoa', 'Cantarino', 'Oliveira']
print('Names: ')
print(names)

# Create a list with names equal or less than 7 characters
print('List with names equal or less than 7 characters: ')
lis = list(map(lambda name: f'Your instructor is {name}. ', filter(lambda name: len(name) <= 7, names)))
print(lis)

# Create a list with names more than 7 characters
print('List with names more than 7 characters: ')
lis2 = list(map(lambda name: f'Your instructor is {name}. ', filter(lambda name: len(name) > 7, names)))
print(lis2)

