'''

*args

The *args is a parameter, as any other one.
This means that you can call it with any name beginning with (*)

Ex.: *param, *you

The *args parameter used in a function, put all passed values inside a tuple

'''


def sum_all(n1, n2, n3):
    return n1 + n2 + n3


print(sum_all(4, 6, 11))

# print(sum_all(4, 6)) # TypeError

# print(sum_all(4, 6, 11, 2)) # TypeError


def sum_all_args(*args):
    return sum(args)


print(sum_all_args())
print(sum_all_args(1))
print(sum_all_args(1, 2))
print(sum_all_args(1, 2, 3))
print(sum_all_args(1, 2, 3, 4))


def verify_info(*args):
    if 'Rodrigo' in args and 'Cantarino' in args:
        return 'Welcome Boss!'
    return 'Who are you ?'


print(verify_info(''))
print(verify_info('Rodrigo', 1, 2, 3, 'Pessoa'))
print(verify_info('Rodrigo', 3, 'Cantarino'))


def sum_all_args2(*args):
    return sum(args)


numbers = [1, 2, 3, 4, 5, 6, 7]

# print(sum_all_args2(numbers)) # TypeError

print(sum_all_args2(*numbers))  # The (*) works as sign to inform to python to unpack the data collection
