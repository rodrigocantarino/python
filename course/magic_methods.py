"""

OOP - Magic Methods

Magic Methods are all Methods that uses dunder (__)

Example: __init__()

"""


class Books:

    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def __str__(self):
        return f"{ self.__title}."

    def __repr__(self):  # Basically the same as __str__(), but __str__() has the priority.
        return f"{self.__title} by {self.__author}."

    def __len__(self):
        return self.__pages

    def __del__(self):
        print(f"A Book object was deleted from memory!")

    def __add__(self, other):
        return f"{self} - {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += '' + str(self) + '. '
            return msg
        return 'I can multiply only by integer number.'


book1 = Books('Lord of the Rings', 'J.R.R Tolkien', 1200)
book2 = Books("The Hitchhiker's Guide to the Galaxy", 'Douglas Adams', 250)

print(book1)  # = print(str(book1)) and executes the method __str__()
print(book2)

print('--------------------------------------------------------')

print(repr(book1))  # executes the method __repr__()
print(repr(book2))  # executes the method __repr__()

print('--------------------------------------------------------')

print(len(book1))  # executes the method __len__()
print(len(book2))  # executes the method __len__()

print('--------------------------------------------------------')

del book1

print('--------------------------------------------------------')

book1 = Books('Lord of the Rings', 'J.R.R Tolkien', 1200)

print(book1 + book2)

print('--------------------------------------------------------')

print(book1 * 3)
print(book1 * book2)

print('--------------------------------------------------------')
print('Process finished!!!!')
