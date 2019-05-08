"""

StringIO

To write/read a file, the user that executes the script MUST HAVE permission.

StringIO -> used to write/read a file only in memory.

"""


# to use StringIO we have to import
from io import StringIO

message = 'This is only a dummy string to test!'

# We can create a file in memory with a existing string or an empty file

file = StringIO(message)

# After this step, we can use normal functions to handle the file

print(file.read())

file.write('\nThis is only another line to a dummy string to test!')

file.seek(0)

print(file.read())
