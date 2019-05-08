"""

Memory test with generator

"""


def fibonacci_seq_list(max):
    numbers = []
    a, b = 0, 1
    while len(numbers) < max:
        numbers.append(b)
        a, b = b, a + b
    return numbers


# print(fibonacci_seq_list(100000))  # Uses 1.3 GB of memory


def fibonacci_seq_gen(max):
    a, b, counter = 0, 1, 0
    while counter < max:
        a, b = b, a + b
        yield a
        counter = counter +1


for n in fibonacci_seq_gen(100000):   # Uses 4.3 MB of memory
    print(n)


