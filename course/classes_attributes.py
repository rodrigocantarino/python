"""

Classes attributes

- In Python we have 3 attribute types
  - Instance Attributes -> are declared inside the construct method.
  - Class Attributes
  - Dynamics Attributes


"""
# ################################################################
# ##################### Instance Attributes ######################
# ################################################################

# Classes with PUBLIC Instance Attributes


class Lamp:

    def __init__(self, voltage, colour):
        self.voltage = voltage
        self.colour = colour
        self.switch = False


class BankAccount:

    def __init__(self, number, balance, limit):
        self.number = number
        self.balance = balance
        self.limit = limit


class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


# Classes with PRIVATE Instance Attributes
# Private attributes are defined by double underline (__) before the attribute name. AKA Name Mangling.


class Access:

    def __init__(self, email, password):
        self.email = email
        self.__password = password

    # Good practice
    def print_email(self):
        print(self.email)

    # Good practice
    def print_password(self):
        print(self.__password)


# OBS: This "PRIVATE Attributes" nomenclature is just a convention. On Python, every attribute is public.
# So the language won't forbid the access to the "private attribute" outside the class.


user = Access('user@gmail.com', '12345')

print(user.email)

# print(user.__password)  # AttributeError

# print(dir(user))

# We can access by 'Name Mangling'
print(user._Access__password)  # This way we can access the "private" attribute. But it's not a good practice.

user.print_email()
user.print_password()

# Instance attributes are owned by the specific instances of a class.
# This means for two different instances the instance attributes (values) are usually different.
# But all instances will have those attributes.

print('------------------------------------------------------')
print('------------------------------------------------------')

# ################################################################
# ###################### Class Attributes ########################
# ################################################################


class Product:

    # Class Attribute. All instances of this class will share the same value of this attribute.
    tax = 1.05
    counter = 0

    def __init__(self, name, description, value):
        self.id = Product.counter + 1
        self.name = name
        self.description = description
        self.value = value * Product.tax
        Product.counter = self.id


p1 = Product('PlayStation 4', 'Video Game', 3500)
p2 = Product('XBox', 'Video Game', 4500)

print(p1.tax)
print(p2.tax)

print('------------------------------------------------------')

print(p1.value)
print(p2.value)

print(p1.id)
print(p2.id)

print('------------------------------------------------------')

# OBS: We don't need to create a instance of a class to verify a class attribute
print(Product.tax)


# ################################################################
# ##################### Dynamic Attributes #######################
# ################################################################

# Dynamic Attributes are Instance Attributes that are create at run time.
# They are exclusive of the instance that create it.


p1 = Product('PlayStation 4', 'Video Game', 3500)
p2 = Product('Rice', 'Food', 5.99)

p2.weight = '5kg'  # This is a Dynamic Attributes created at run time.

print(f"Product: {p2.name}. Description: {p2.description}. Value: {p2.value}. Weight: {p2.weight}")

# p1 instance doesn't have 'weight' attribute. So an AttributeError will be thrown.
# print(f"Product: {p1.name}. Description: {p1.description}. Value: {p1.value}. Weight: {p1.weight}")

# ################################################################
# ##################### Deleting Attributes ######################
# ################################################################

print('------------------------------------------------------')

print(p1.__dict__)
print(p2.__dict__)

print('------------------------------------------------------')

del p2.weight
del p2.description
del p2.value

print(p1.__dict__)
print(p2.__dict__)
