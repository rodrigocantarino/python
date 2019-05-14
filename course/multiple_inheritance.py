"""

OOP - Multiple Inheritance


"""

# Direct Inheritance


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class DirectInheritance(Base1, Base2, Base3):
    pass


# Indirect Inheritance


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class IndirectInheritance(Base3):
    pass


print('--------------------------------------------------------')


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


wale = Aquatic('Wally')
print(wale.swim())
print(wale.greetings())
print('--------------------------------------------------------')
dog = Terrestrial('Scoob Doo')
print(dog.walk())
print(dog.greetings())
print('--------------------------------------------------------')
penguin = Penguin('Tux')
print(penguin.walk())
print(penguin.swim())
print(penguin.greetings())  # Method Resolution Order - The first Inheritance is executed
print('--------------------------------------------------------')

print(isinstance(penguin, Animal))
print(isinstance(penguin, Aquatic))
print(isinstance(penguin, Terrestrial))
print(isinstance(penguin, Penguin))
print(isinstance(penguin, object))