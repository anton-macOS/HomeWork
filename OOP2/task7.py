# Використовуючи всі набуті знання у успадкуванні та інкапсуляції спроектуй просту банківську систему.
# Створи клас Customer та BankAccount. Ти можеш створювати базові класи,
# абстрактні класи, на твій розсуд. Customer повинен мати такі атрибути як name,
# email, customer_id. BankAccount повинен мати balance, owner, account_number.
# У кастомера повинні бути методи для отримання інфи про атрибути.
# У BankAccount повинні бути методи поповнення та виведення коштів з усіма валідаціями,
# а також метод для отримання account_number
class Customer:
    def __init__(self, name, email, customer_id):
        self.__name = name
        self.__email = email
        self.__customer_id = customer_id

    def get_customer_info(self):
        return f'Name - {self.__name}, email - {self.__email}, customer ID - {self.__customer_id}'


class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return f'Your balance is {self.__balance}'

    def withdraw(self, value):
        if self.__balance == 0 or self.__balance - value < 0:
            raise 'Not enought money! Deposit you balance'
        else:
            self.__balance -= value
            return f'Withwraw - {value} completed'

    def deposit(self, value):
        if value < 0:
            return 'Enter correct value'
        else:
            self.__balance += value
            return 'Completed!'

    def get_account_number(self):
        return f'Your account number is {self.__account_number}'


anton = Customer('Anton', 'anton@gmail.com', 1)
print(anton.get_customer_info())
wallet = BankAccount('Anton', 1234567)
print(wallet.get_balance())
wallet.deposit(100)
print(wallet.get_balance())
wallet.withdraw(50)
print(wallet.get_balance())
print(wallet.get_account_number())
