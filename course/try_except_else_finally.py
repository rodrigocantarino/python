"""

Try / Except / Else / Finally

All data entry MUST BE treated

# On this case, if the user type a string a error will be displayed
# num = int(input('Type a number: '))
# print(f'You type the number: {num}')

# So

try:
    num = int(input('Type a number: '))
except ValueError:
    print('You MUST type a integer Number! Execute again!')
else:
    print(f'You type the number: {num}')
finally:
    # Why use this?
    # Is normally used to close or deallocate resources.
    # "Clear" the memory like, for example, close a database connection.
    print('Went good or wrong. IE, this block is always executed!!!')

"""

print('-------------------------------')


def divide(n1, n2):
    try:
        return int(n1) / int(n2)
    except ValueError:
        return 'The informed numbers must be integer.'
    except ZeroDivisionError:
        return "Can't divide by zero!"
    # except (ValueError, ZeroDivisionError) as err:
        # return f'A problem occur! {err}'


num1 = input('Type the first number: ')
num2 = input('Type the second number: ')

print(divide(num1, num2))
