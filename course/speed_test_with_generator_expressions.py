"""

Speed test with generator expressions

"""

import time


def nums():
    for num in range(10):
        yield num


gen1 = nums()
print(gen1)  # Generator

print(next(gen1))
print(next(gen1))


gen2 = (num for num in range(10))

print(gen2)  # Generator expression

# print(next(gen2))
# print(next(gen2))

print('')
print('_______________________________')
print('_______________________________')
print('_______________________________')
print('')

# Speed Test
gen_beggin_time = time.time()
print(sum(num for num in range(100000000)))  # 100 millions
total_time_gen_exp = time.time() - gen_beggin_time

list_beggin_time = time.time()
print(sum([num for num in range(100000000)]))  # 100 millions
total_time_list_exp = time.time() - list_beggin_time

print(f"Total time from generator expression: {total_time_gen_exp}")
print(f"Total time from list comprehension: {total_time_list_exp}")

