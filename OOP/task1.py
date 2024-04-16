# Розробіть клас BankAccount для представлення банківського рахунку.
# Додайте методи для зняття та поповнення коштів на рахунку.
# Використовуйте магічний метод __str__ для виведення інформації про рахунок.
#
# Приклад використання:
# account = BankAccount(100)
# account.withdraw(50)
# account.topup(200)
# print(account)  # You account balance is: 250
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def topup(self, amount):
        self.balance += amount

    def __repr__(self):
        return f'Your account balance is {self.balance}'

    def __str__(self):
        return self.__repr__()


account = BankAccount(100)
account.withdraw(50)
account.topup(200)
print(account)
