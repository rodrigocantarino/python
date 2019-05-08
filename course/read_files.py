"""

Read files

To read a file content we use the builtin function open() -> return a _io.TextIOWrapper object

See: https://docs.python.org/3/library/functions.html#open


open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised.


<_io.TextIOWrapper name='mussum_ipsum.txt' mode='r' encoding='UTF-8'>

mode='r' => Read mode only

"""


file = open('mussum_ipsum.txt')

print(file)
print(type(file))

print("____________________________________________")
print("")

# To read the file content we have to use the function read()

print(file.read(50))  # read the first 50 characters from the file

print(file.read())

# The function read() uses a cursor. After read() function is used, the cursor will be at the end of the file.
