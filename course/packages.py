"""

Packages -> is a directory(folder) with a modules collection.

On Python 2.x a package must have a __init__.py file
On Python 3.x is not obligatory to have the __init__.py file, but is good to have to maintain the compatibility.

"""

from geek import geek1, geek2

# from geek.geek1 import f1

from geek.university import geek3, geek4

# from geek.university.geek4 import f4

print('------------------------------------')
print('import geek1')
print(geek1.pi)
print(geek1.f1(3, 4))

print('------------------------------------')
print('import geek2')
print(geek2.f2())

print('------------------------------------')
print('import geek3')
print(geek3.f3())

print('------------------------------------')
print('import geek4')
print(geek4.f4())
