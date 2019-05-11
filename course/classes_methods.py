"""

Classes methods - A method defines the behavior of the objects that are created from the class.
Another way to say this is that a method is an action that an object is able to perform.

On Python we have two types of methods.
 - Instance Methods
 - Class Methods

The __init__() method is a special method use as class constructor.

All dunder methods on Python are called Magic Methods.

Is not recommended to create a dunder methods because it can conflict with some builtin Python methods.

# pip3 install passlib


"""

from passlib.hash import pbkdf2_sha256 as cryp


class Lamp:

    def __init__(self, colour, voltage, luminosity):
        self.__colour = colour
        self.__voltage = voltage
        self.__luminosity = luminosity
        self.__switch = False


class BankAccount:

    counter = 4999

    def __init__(self, balance, limit):
        self.__number = BankAccount.counter + 1
        self.__balance = balance
        self.__limit = limit
        BankAccount.counter = self.__number


class Product:

    counter = 0

    def __init__(self, name, description, value):
        self.__id = Product.counter + 1
        self.__name = name
        self.__description = description
        self.__value = value
        Product.counter = self.__id

    def discount(self, percentage):
        """Return the product value with a discount"""
        return self.__value * ((100 - percentage) / 100)


class User:

    counter = 0

    @classmethod
    def users_counter(cls):
        print(f"We have {cls.counter} user(s) on the system. ")

    @classmethod
    def see(cls):
        print('Test Yo! ')

    @staticmethod
    def definition():
        return 'PAXUSR357'

    def __init__(self, name, last_name, email, password):
        self.__id = User.counter + 1
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__password = cryp.hash(password, rounds=200000, salt_size=16 )  # password
        User.counter = self.__id
        print(f"Created user: {self.__create_user()}")

    def full_name(self):
        return f"{self.__name} {self.__last_name}"

    def verify_password(self, password):
        if cryp.verify(password, self.__password):
            return True
        return False

    def __create_user(self):
        return self.__email.split('@')[0]



'''

# Example 1 - Using Instance Methods

p1 = Product('PlayStation 4', 'Video Game', 3500)
print(p1.discount(50))

print('------------------------------------------------------')

u1 = User('Rodrigo', 'Cantarino', 'user_rc@gmail.com', '12345')
print(u1.full_name())

u2 = User('Rodrigo', 'Pessoa', 'user_rp@gmail.com', '54321')
print(u2.full_name())

print(u1._User__password)  # Just for checking! Is not recommended to access private attributes this way. Don't use it!
print(u2._User__password)  # Just for checking! Is not recommended to access private attributes this way. Don't use it!

print('------------------------------------------------------')
print('------------------------------------------------------')
print('Lets create a new user!')

name = input('Inform the user name: ')
last_name = input('Inform the user last name: ')
email = input('Inform the user e-mail: ')
password = input('Inform the user password: ')
confirm_password = input('Confirm the user password: ')

if password == confirm_password:
    u3 = User(name, last_name, email, password)
else:
    print("The password confirmation doesn't match! Try again!")
    exit(42)

print('User successfully created!')
print('')

pass_w = input('Inform the password to access: ')
print('')

if u3.verify_password(pass_w):
    print('Access granted! Welcome!!!!!')
else:
    print('Access denied!')

# Just for checking! Is not recommended to access private attributes this way. Don't use it!
print(f'U3 encrypted password: {u3._User__password}')

print('------------------------------------------------------')
print('------------------------------------------------------')

'''


# ################################################################
# ################# Class Methods AND Static #####################
# ################################################################

# u1.users_counter()  # Wrong way. Works, but is wrong.
User.users_counter()  # Correct way.

u1 = User('Rodrigo', 'Cantarino', 'rcantarino@gmail.com', '12345')
u2 = User('Rodrigo', 'Pessoa', 'rpessoa@gmail.com', '54321')

User.users_counter()  # Correct way.

print(User.definition())
print(u2.definition())
