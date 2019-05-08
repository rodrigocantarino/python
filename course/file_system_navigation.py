"""

File system navigation

To use files we need to import the module OS

"""

import os
import sys

# Return the absolute path
print(os.getcwd())

# To change the directory
os.chdir('..')

print(os.getcwd())

# We can check if the directory is relative or absolute

print(os.path.isabs('/Applications/MAMP/htdocs/python/course'))  # True

print(os.path.isabs('python/course'))  # False

print(os.name)

print(os.uname())

print(sys.platform)

print('---------------------------------------')

print(os.getcwd())

access_dir = os.path.join(os.getcwd(), 'course/geek', 'university')

os.chdir(access_dir)

print(os.getcwd())

os.chdir(access_dir + '/..')  # /Applications/MAMP/htdocs/python/course/geek

# print(os.listdir('/'))
print(os.listdir())

print('---------------------------------------')

print(list(os.scandir()))

print('---------------------------------------')

directory_scanner = os.scandir()

files = list(directory_scanner)

directory_scanner.close()  # We have to close the scandir()

print(files[0].name)
print(files[0].inode())  # Node index in the file directory
print(files[0].is_dir())  # Is directory? False
print(files[0].is_file())  # Is file? True
print(files[0].is_symlink())  # Is symbolic link? False
print(files[0].path)
print(files[0].stat())  # Statistics about the file
