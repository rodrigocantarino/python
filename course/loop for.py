"""
Loop structure FOR

Iterable variables:
- Strings
- Arrays/Lists
- Collections
- Tuples
- Ranges
"""

iterable = [1, 3, 5, 7, 9, 11, 13]

for item in iterable:
    print(item)

print("____________________________________________")

name = "Rodrigo Pessoa Cantarino de Oliveira"
for char in name:
    print(char)

for char in name:
    print(char, end=' ')

print('\n')

for char_array in enumerate(name):
    print(f"CHAR_Array: {char_array} ")

for index, char in enumerate(name):
    print(f"index = {index} || CHAR: " + char)

# Ignoring the index using '_'
for _, char in enumerate(name):
    print(f"CHAR: {char}")

print("____________________________________________")

for n in range(1, 10): # 1 to 9, 10 not included
    print(n)

# U+1F60A = U0001F60A
for n in range(1, 10):
    print('\U0001F60A' * n)

# U+1F341 = U0001F341
for _ in range(0, 3):
    for n in range(1, 10):
        print('\U0001F341' * n)

