"""

OOP - Inheritance

"""


class Person:

    def __init__(self, name, last_name, cpf):
        self.__name = name
        self.__last_name = last_name
        self.__cpf = cpf

    def full_name(self):
        return f"{self.__name} {self.__last_name}"


class Client(Person):
    """Inheritance from class Person"""

    def __init__(self, name, last_name, cpf, income):
        # Person().__init__(self, name, last_name, cpf)  # Works, but is not a good practice
        super().__init__(name, last_name, cpf)  # Usual way to do it.
        self.__income = income


class Employee(Person):
    """Inheritance from class Person"""

    def __init__(self, name, last_name, cpf, registration):
        super().__init__(name, last_name, cpf)
        self.__registration = registration

    def full_name(self):
        """ Overriding method"""
        # return f"Employee: {self._Person__name}, Registration: {self.__registration}"
        return f"Employee: {super().full_name()}, Registration: {self.__registration}"


client1 = Client('Rodrigo', 'Pessoa', '111.222.333-44', 5000)
employee1 = Employee('Rodrigo', 'Cantarino', '111.222.333-44', '77113390')


print("Client: " + client1.full_name())
print(employee1.full_name())

print('--------------------------------------------------------')

print(client1.__dict__)
print(employee1.__dict__)

print('--------------------------------------------------------')

