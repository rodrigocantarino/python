"""

File system Manipulation

See:
- https://docs.python.org/3/library/os.html
- https://pypi.org/project/Send2Trash/
- https://docs.python.org/3.7/library/tempfile.html

"""

import os
from send2trash import send2trash
import tempfile

# Files
print(os.path.exists('file.txt'))
print(os.path.exists('mussum_ipsum.txt'))

print('---------------------------------------')

# Directories (Relative path)
print(os.path.exists('geek'))
print(os.path.exists('geek/university'))
print(os.path.exists('another_folder'))

print('---------------------------------------')

# Directories (Absolute path)
print(os.path.exists('/etc'))
print(os.path.exists('/geek'))

print('---------------------------------------')

# Creating file - basic ways
open('mussum_ipsum4.txt', 'w').close()
open('mussum_ipsum5.txt', 'a').close()
with open('mussum_ipsum5.txt', 'w') as file:
    pass

# Creating file - best practice
# Relative path - The same absolute path as the script.
# If the already exists, a FileExistsError will be thrown
# On MAC OS Systems, a PermissionError will be thrown
try:
    os.mknod('mussum_ipsum6.txt')
except PermissionError as err:
    print(err)
# os.mknod('/Application/MAMP/htdocs/python/course/mussum_ipsum6.txt')  # Absolute path

print('---------------------------------------')

# Creating unique directory - best practice
try:
    directory = 'template'
    # directory = 'template/geek'  # If the 'template' directory doesn't exists, a FileNotFoundError will be thrown
    os.mkdir(directory)  # If the directory already exists, a FileExistsError will be thrown
    print(f'Directory: \'{directory}\' successfully created!')
except FileExistsError as err:
    print(err)

print('---------------------------------------')

# Creating a sequence of directories - best practice
try:
    directories = 'template/geek/Rodrigo/me/myself'
    os.makedirs(directories)
    print(f'Directories: \'{directories}\' successfully created!')
except FileExistsError as err:
    print(err)

print('---------------------------------------')

directories = 'template/geek/Rodrigo/me/myself'
# With 'exist_ok=True' parameter, if the directory already exists, the FileExistsError will NOT be thrown.
os.makedirs(directories, exist_ok=True)

print('---------------------------------------')

# Rename files and directories
try:
    os.rename('template', 'tmp')
    os.rename('tmp/geek', 'geek_two')
except OSError as err:
    print(err)

print('---------------------------------------')
try:
    os.rename('mussum_ipsum_test_input.txt', 'mussum_ipsum_test_rename.txt')
except FileNotFoundError as err:
    print(err)

print('---------------------------------------')


###
#  ATTENTION: All deleted resources will NOT been send to the trash!!!
#  To send the deleted resources to the trash, use the 'send2trash' external module!
###

# Remove file - BE VERY CAREFULL!!!!!
try:
    file = 'mussum_ipsum5.txt'
    os.remove(file)
    print(f"File '{file}' successfully deleted!!")
except FileNotFoundError as err:
    print(err)

print('---------------------------------------')

# Remove Directory
try:
    os.remove('tmp')  # Will thrown a IsADirectoryError or a PermissionError
except (IsADirectoryError, PermissionError) as err:
    print(err)

try:
    rmdir = 'template'
    os.rmdir(rmdir)  # If the directory is not empty, a OSError will be thrown
except OSError as err:
    print(f"Error to remove. {err}")
except FileNotFoundError as err2:
    print(f"Error to remove. {err2}")

print('---------------------------------------')

# Remove empty Directories tree
os.removedirs('template/geek/Rodrigo/me/myself')  # Remove all directories

print('---------------------------------------')
print('---------------------------------------')

# Using send2trash module
try:
    rm_file = 'mussum_ipsum4.txt'
    send2trash(rm_file)
except OSError as err:
    print(f"Error to remove. {err}")
except FileNotFoundError as err2:
    print(f"Error to remove. {err2}")


print('---------------------------------------')
print('---------------------------------------')
print('Working with temporary directories and files')
print('')

# Temp Directory
with tempfile.TemporaryDirectory() as tmp_dir:
    print(f"Temp dir created: {tmp_dir}")
    with open(os.path.join(tmp_dir, 'tmp_file.txt'), 'w') as file:
        file.write('Temporary directory and file successfully created!!!')

# Temp file
with tempfile.TemporaryFile() as tmp_file:
    # On temporary files, is necessary to use the binary mode to write the file.
    # If we don't use the binary mode a TypeError: a bytes-like object is required, not 'str', will be thrown
    tmp_file.write(b'Temporary file successfully created!!!\n')
    tmp_file.seek(0)
    print(tmp_file.read())

# Another way
tmp_file = tempfile.NamedTemporaryFile()
tmp_file.write(b'Temporary file successfully created!!!\n')
tmp_file.seek(0)

print(tmp_file.read())
print(tmp_file.name)
input()

tmp_file.close()

