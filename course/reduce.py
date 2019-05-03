"""

Reduce

Since Python 3+, Reduce is not a bultin function

We have to import from functools.

reduce(<function>, iterable)


How it works:

data_set = [a1, a2, a3, ..., an]

def func(x, y):
    return x * y

reduce(func, data_set)

Step 1:
    result_1 = f(a1, a2)
Step 2:
    result_2 = f(result_1, a3)
Step 3:
    result_3 = f(result_3, a4)
...
Step N:
    result_n = f(result_n-1, an)


"""

from functools import reduce


data_set = [1, 2, 5, 7, 11, 13, 17, 23, 29]

# The function used on reduce, has always to have 2 parameters
times = lambda x, y: x * y

result = reduce(times, data_set)

print(result)

# Another way to do the same task but using the loop structure for

res = 1

for n in data_set:
    res = res * n

print(res)
