"""

Pickle:
The pickle module implements binary protocols for serializing and de-serializing a Python object structure.
“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the
inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object
hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” [1] or “flattening”;
however, to avoid confusion, the terms used here are “pickling” and “unpickling”.

See: https://docs.python.org/3/library/pickle.html

"""

import pickle


class Animal:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def eat(self):
        print(f"{self.__name} is eating!")


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print('Meeeeooowww!')


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def woof(self):
        print('Woof Woof!!!')


felix = Cat('Felix')
pluto = Dog('Pluto')

# Writing Pickle file
# with open('animals.pickle', 'wb') as file:
#     pickle.dump((felix, pluto), file)


# Reading Pickle file

with open('animals.pickle', 'rb') as file:
    cat, dog = pickle.load(file)

    print(f"The cat's name is: {cat.name}")
    cat.meow()
    print(type(cat))

    print(f"The dog's name is: {dog.name}")
    dog.woof()
    print(type(dog))