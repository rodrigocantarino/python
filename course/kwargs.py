'''

**kwargs

Ex.: **param

This is just another parameter, but different from *args which puts the values inside a tuple,
the **kwargs requires named parameters and transform them in a dictionary data type.

Obligatory order of parameters on functions:

- Required parameters
- *args
- default parameters
- **kwargs

'''


def favorite_colours(**kwargs):
    # basic use
    print(kwargs)


favorite_colours(rodrigo='black', pessoa='blue', cantarino='white', oliveira='green')
print('')


def favorite_colours2(**kwargs):
    for people, colour in kwargs.items():
        print(f'{people.title()}\'s favorite colour is {colour}.')


favorite_colours2(rodrigo='black', pessoa='blue', cantarino='white', oliveira='green')


# Obs.: The *args and **kwargs are not obligatory

def special_hello(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Rodrigo':
        return 'Hello Geek Master!'
    elif 'geek' in kwargs:
        return f"Hello Geek {kwargs['geek']}."
    return "Aren't you a geek?"


print(special_hello())
print(special_hello(geek='Rodrigo'))
print(special_hello(geek='Cantarino'))

'''

Obligatory order of parameters on functions:

- Required parameters
- *args
- default parameters
- **kwargs

'''
print('')
print('-------------------------------')
print('')
print('-------------------------------')
print('')


def my_function(age, name, *args, civil_status='single', **kwargs):
    print(f"{name.title()} is {age} years old.")
    print(args)
    print(civil_status)
    print(kwargs)


my_function(33, 'Rodrigo')
print('')
print('-------------------------------')
print('')
my_function(34, 'Rodrigo Pessoa', 1, 2, 3, 4, 5, civil_status='maried')
print('')
print('-------------------------------')
print('')
my_function(35, 'Rodrigo Cantarino', 4, 5, php=True)
print('')
print('-------------------------------')
print('')
my_function(36, 'Rodrigo Oliveira', 7, 9, I='Go', You="Don't")
print('')
print('-------------------------------')
print('')
my_function(37, 'Cantarino', 10, 12, job='programmer', hoby="hiking", civil_status='Lost')

print('')
print('-------------------------------')
print('')
print('-------------------------------')
print('')


def show_names(**kwargs):
    return f"Hello {kwargs['name']} {kwargs['surname']}!"


names = {'name': 'Rodrigo', 'surname': 'Cantarino'}

# print(show_names())  # Error
# print(show_names(names))  # KeyError

# The (**) works as sign to inform to python to unpack the data collection
print(show_names(**names))

print('')
print('-------------------------------')
print('')
print('-------------------------------')
print('')

# Unpack samples with (*) and (**)


def sum_numbers(a, b, c):
    print(a + b + c)


numb_list = [1, 2, 3]
numb_tuple = (1, 2, 3)
numb_set = {1, 2, 3}

sum_numbers(*numb_list)
sum_numbers(*numb_tuple)
sum_numbers(*numb_set)

# The keys names on the dictionary must be the same as defined in the function
numb_dict = dict(a=1, b=2, c=3)
sum_numbers(**numb_dict)
