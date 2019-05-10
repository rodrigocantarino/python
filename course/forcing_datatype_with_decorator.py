"""

Forcing data type with decorator

"""


def force_type(*types):
    def decorator(func):
        def convert(*args, **kwargs):
            new_args = []
            for (value, type) in zip(args, types):
                new_args.append(type(value))
            return func(*new_args, **kwargs)
        return convert
    return decorator


@force_type(str, int)
def repeat_message(msg, times):
    for time in range(times):
        print(msg)


repeat_message('Hello!', '3')

print('------------------------------------')


@force_type(float, float)
def divide(a, b):
    print(a/b)


divide(10, '5')