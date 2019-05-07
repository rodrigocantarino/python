"""

Try / Except

Handle with errors that can occur on our code. Prevent that the program stop the execution and
the user receive "Strange" messages.

Form:

try:
    // Code
except:
    // Code Handle the error

"""

# Generic Error
try:
    rodrigo_func()
except:
    print('Something went wrong!')

try:
    len(5)
except:
    print('Something went wrong again!')

print('-------------------------------')

# Specific Error
try:
    rodrigo_func()
except NameError:
    print('You are trying to use an undefined function!')

try:
    len(5)
except TypeError as err:
    print('You are using a different variable type to len() function!')
    print(f'Returned error: {err}')

print('-------------------------------')

# Handle more than one error

try:
    # len(5)
    # rodrigo_func()
    print('Rodrigo'[10])
except TypeError as err_a:
    print(f'Returned TypeError: {err_a}')
except NameError as err_b:
    print(f'Returned NameError: {err_b}')
except:
    print('Unexpected error')

print('-------------------------------')


def print_dict_value(dictionary, key):
    try:
        print(dictionary[key])
    except KeyError:
        print(f"There is no '{key}' on the dictionary!!!")


dictionary = {'name': 'Rodrigo Cantarino'}

print_dict_value(dictionary, 'name')

print_dict_value(dictionary, 'last_name')
