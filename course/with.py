"""

With

Steps to work with files:

1 - Open the file
2 - Process the data of the file
3 - Close the file

"""

# Using with, the file will be closed automatically. file.close() is not necessary.
with open('mussum_ipsum.txt') as file:
    print(file.readlines())
    print(file.closed)

print(file.closed)

