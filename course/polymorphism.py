"""

OOP - Polymorphism

Polymorphism is the ability of an object to take on many forms.
The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class
object. Any Java object that can pass more than one IS-A test is considered to be polymorphic.

Overriding is the essence of Polymorphism!!!

"""


class Animal(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def make_sound(self):
        raise NotImplementedError('The child class must implement this method!')

    def eat(self):
        print(f'{self.name} is eating!')


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('Woof Woof!!!')


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('Meeeooowww!!!')


class Rat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('Squeak squeak!')


pluto = Dog('Pluto')
pluto.eat()
pluto.make_sound()

felix = Cat('Felix')
felix.eat()
felix.make_sound()

mickey = Rat('Mickey')
mickey.eat()
mickey.make_sound()
