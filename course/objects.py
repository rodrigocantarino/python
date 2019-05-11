"""

OOP -> Objects

Objects are instances of the defined classes.

"""


class Lamp:

    def __init__(self, colour, voltage, luminosity):
        self.__colour = colour
        self.__voltage = voltage
        self.__luminosity = luminosity
        self.__switch = False

    def check_lamp(self):
        return self.__switch

    def switch_on_off(self):
        if self.check_lamp():
            self.__switch = False
        else:
            self.__switch = True


class Client:

    def __init__(self, name, cpf):
        self.__name = name
        self.__cpf = cpf

    def get_client_name(self):
        return self.__name


class BankAccount:

    counter = 4999

    def __init__(self, balance, limit, client):
        self.__number = BankAccount.counter + 1
        self.__balance = balance
        self.__limit = limit
        self.__client = client
        BankAccount.counter = self.__number

    def show_client(self):
        print(f'The client is: {self.__client.get_client_name()}')


class User:

    counter = 0

    def __init__(self, name, last_name, email, password):
        self.__id = User.counter + 1
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        User.counter = self.__id


# ################################################################
# #################### Objects/Instances #########################
# ################################################################

lamp1 = Lamp('Yellow', 220, 1000)

lamp1.switch_on_off()
print(f"The lamp is on? {lamp1.check_lamp()}")
lamp1.switch_on_off()
print(f"The lamp is on? {lamp1.check_lamp()}")

# bank_acc = BankAccount(200, 5000)

user1 = User('Rodrigo', 'Cantarino', 'rcantarino@gmail.com', '12345')

print('------------------------------------------------------')
print('------------------------------------------------------')

client1 = Client('Rodrigo', '001002003-99')

bank_acc = BankAccount(200, 5000, client1)

bank_acc.show_client()

print(bank_acc.__dict__)
