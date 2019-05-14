"""

OOP - Super method

"""


class Animal:

    def __init__(self, name, species):
        self.__name = name
        self.__species = species

    def make_sound(self, sound):
        print(f"{self.__name} makes: {sound}")


class Cat(Animal):

    def __init__(self, name, breed, species):
        # Animal.__init__(self, name, species)  # Works, but is not a good practice. Use super() instead.
        super().__init__(name, species)
        self.__breed = breed  # race


felix = Cat('Felix the Cat', 'Tuxedo cat', 'Felis catus')
felix.make_sound('Meow')

