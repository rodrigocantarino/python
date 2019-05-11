"""

OOP - Abstraction and encapsulation

Encapsulation: Wrapping code and data together into a single unit. Class is an example of encapsulation, because it
wraps the method and property.

Abstraction: Hiding internal details and showing functionality only. Abstraction focus on what the object does instead
of how it does.

"""


class Client:

    def __init__(self, name, cpf):
        self.__name = name
        self.__cpf = cpf

    def get_client_name(self):
        return self.__name


class BankAccount:

    counter = 7999

    def __init__(self, balance, limit, client):
        self.__number = BankAccount.counter + 1
        self.__balance = balance
        self.__limit = limit
        self.__client = client
        BankAccount.counter = self.__number

    def show_client(self):
        print(f'The client is: {self.__client.get_client_name()}')

    def show_account_number(self):
        print(f'Account: {self.__number}')

    def current(self):
        client = f'{self.__client.get_client_name()} you have a balance of'
        desc = f'{client} ${round(float(self.__balance), 2)} and ${round(float(self.__limit), 2)} of limit.\n'
        total = f'Total: ${round(float(self.__balance) + float(self.__limit), 2)}'
        print(desc + total)

    def deposit(self, value):
        if value > 0:
            self.__balance += value

    def withdraw(self, value):
        if value > 0:
            if (self.__balance - value) >= 0:
                self.__balance -= value
            else:
                print(f"You don't have enough money to withdraw. Your balance is: ${self.__balance}")

    def transfer(self, value, bank_acc_destiny):
        self.withdraw(value)
        bank_acc_destiny.deposit(value)


client1 = Client('Rodrigo', '001002003-99')

bank_acc = BankAccount(2000, 5000, client1)


bank_acc.show_client()
bank_acc.show_account_number()
bank_acc.current()

print('------------------------------------------------------')
'''
bank_acc.deposit(2000)
bank_acc.withdraw(500)

bank_acc.show_client()
bank_acc.show_account_number()
bank_acc.current()
'''
print('------------------------------------------------------')
'''
bank_acc.deposit(200)
bank_acc.withdraw(50000)

bank_acc.show_client()
bank_acc.show_account_number()
bank_acc.current()
'''
print('------------------------------------------------------')
print('------------------------------------------------------')

client2 = Client('Cantarino', '011022033-00')

bank_acc2 = BankAccount(4000, 7000, client2)

bank_acc2.show_client()
bank_acc2.show_account_number()
bank_acc2.current()

print('------------------------------------------------------')
print('------------------------------------------------------')

bank_acc2.transfer(1500, bank_acc)

bank_acc.show_client()
bank_acc.show_account_number()
bank_acc.current()
print('------------------------------------------------------')
bank_acc2.show_client()
bank_acc2.show_account_number()
bank_acc2.current()

