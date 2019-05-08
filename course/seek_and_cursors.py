"""

Seek and Cursors

seek() -> is used to move the cursor around the read file

When we use the open() function a streaming connection is created between the file and the program.
After use the file on the program execution, we have to close the file.

"""

file = open('mussum_ipsum.txt')

print(file.read())

print(" ")
print("____________________________________________")
print(" ")

# seek() is used to move the cursor around the file.
# The passed parameter is used to put the cursor on the desired position.
file.seek(14)

print(file.read())
file.close()

print(" ")
print("____________________________________________")
print("____________________________________________")
print("____________________________________________")
print(" ")


file2 = open('mussum_ipsum.txt')
print(file2.readline())  # Will automatically the first line. Move the cursor to the next line.
print(" ")
print(file2.readline())  # Will automatically the second line. Move the cursor to the next line.
print(file2.readline())  # Will automatically the second line. Move the cursor to the next line.

file2.close()


print(" ")
print("____________________________________________")
print("____________________________________________")
print("____________________________________________")
print(" ")


file3 = open('mussum_ipsum.txt')
ret = file3.readlines()  # Return a list with the file lines
print(ret)
print(len(ret))

print(file3.closed)

file3.close()

print(file3.closed)