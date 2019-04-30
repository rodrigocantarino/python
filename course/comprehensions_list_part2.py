"""

Comprehensions - List part 2

We can add conditional logical structures to our list comprehension

"""

numbers = [1, 2, 3, 4, 5, 6, 7]

even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 == 1]

print(even_numbers)
print(odd_numbers)

# Another way
even_numbers = [number for number in numbers if not number % 2]
odd_numbers = [number for number in numbers if number % 2]

print(even_numbers)
print(odd_numbers)

res = [number * 2 if not number % 2 else number / 2 for number in numbers]

print(res)
