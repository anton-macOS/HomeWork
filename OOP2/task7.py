# Використовуючи всі набуті знання у успадкуванні та інкапсуляції спроектуй просту банківську систему.
# Створи клас Customer та BankAccount. Ти можеш створювати базові класи,
# абстрактні класи, на твій розсуд. Customer повинен мати такі атрибути як name,
# email, customer_id. BankAccount повинен мати balance, owner, account_number.
# У кастомера повинні бути методи для отримання інфи про атрибути.
# У BankAccount повинні бути методи поповнення та виведення коштів з усіма валідаціями,
# а також метод для отримання account_number
from abc import ABC, abstractmethod


class UserInfo(ABC):

    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

    @abstractmethod
    def greetings(self):
        pass


class Customer(UserInfo):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)

    def greetings(self):
        return f'Hello my name is {self.name}.'

    def get_customer_info(self):
        return f'Name - {self.name}, email - {self.email}, customer ID - {self.user_id}'


class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return f'Your balance is {self.__balance}'

    def withdraw(self, value):
        if self.__balance - value < 0:
            raise 'Not enought money! Deposit you balance'
        self.__balance -= value
        return f'Withwraw - {value} completed'

    def deposit(self, value):
        if value < 0:
            return 'Enter correct value'
        self.__balance += value
        return 'Completed!'

    def get_account_number(self):
        return f'Your account number is {self.account_number}'


anton = Customer('Anton', 'anton@gmail.com', 1)
print(anton.greetings())
# print(anton.get_customer_info())
wallet = BankAccount('Anton', 1234567)
print(wallet.get_balance())
wallet.deposit(100)
print(wallet.get_balance())
wallet.withdraw(50)
print(wallet.get_balance())
print(wallet.get_account_number())
