"""

OOP - Properties

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

    @property
    def account_number(self):
        return self.__number

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit

    @property
    def client_name(self):
        return self.__client.get_client_name()

    @property
    def current(self):
        return round(float(self.__balance) + float(self.__limit), 2)

    def show_client(self):
        print(f'The client is: {self.get_client_name()}')

    def show_account_number(self):
        print(f'Account: {self.get_account_number()}')

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

client2 = Client('Cantarino', '001002003-99')
bank_acc2 = BankAccount(2000, 5000, client2)

print(bank_acc.__dict__)
print(bank_acc2.__dict__)

print(bank_acc.limit)
print(bank_acc2.limit)

print('--------------------------------------------------------')

bank_acc.limit = 7000  # Using @limit.setter property
bank_acc2.limit = 9000  # Using @limit.setter property

print(bank_acc.__dict__)
print(bank_acc2.__dict__)

print('--------------------------------------------------------')

print(bank_acc.current)
print(bank_acc2.current)
