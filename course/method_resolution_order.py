"""

OOP - Method Resolution Order - MRO


On Python we can check Method Resolution Order - MRO in three ways:
  - Via class property __mro__
  - Via class method mro()
  - Via help

"""


class Animal:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def greetings(self):
        return f"Hi I am {super().name} !"


class Aquatic(Animal):

    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return f"{super().name} is swimming!"

    def greetings(self):
        return f"Hi I am an Aquatic animal {super().name} !"


class Terrestrial(Animal):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return f"{super().name} is walking!"

    def greetings(self):
        return f"Hi I am a Terrestrial animal {super().name} !"


class Penguin(Aquatic, Terrestrial):

    def __init__(self, name):
        super().__init__(name)


penguin = Penguin('Tux')
print(penguin.greetings())  # Method Resolution Order - The first Inheritance is executed

print('--------------------------------------------------------')

print(Penguin.__mro__)
print(Penguin.mro())

help(Penguin)

"""
class Penguin(Aquatic, Terrestrial)
 |  Penguin(name)
 |  
 |  Method resolution order:
 |      Penguin
 |      Aquatic
 |      Terrestrial
 |      Animal
 |      builtins.object
"""

"""
Penguin(Aquatic, Terrestrial)
penguin.greetings() = Hi I am an Aquatic animal Tux !

Penguin(Terrestrial, Aquatic)
penguin.greetings() = Hi I am a Terrestrial animal Tux !
"""
