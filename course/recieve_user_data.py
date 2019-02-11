"""

Receive data from user

All data received via input() is a string type

"""
from datetime import datetime

# print("What is your name?")
# name = input()
name = input("What is your name? ")

# print("What is your age?")
# age = input()
age = int(input("What is your age? "))

# print('Welcome %s, you are %s old!' % (name.title(), age))
# print('Welcome {0}, you are {1} old!'.format(name.title(), age))
print(f'Welcome {name.title()} ({datetime.now().year - age}), you are {age} old!')

age = int(age)

if age < 21:
    print('You are very young!')

if 21 <= age <= 50:
    print('The best age!!!')

if age > 50:
    print('Hello Nanny!!!')
