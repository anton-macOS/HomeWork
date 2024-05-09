# Створіть клас Account та приватний атрибут balance. Додайте метод який буде повертати значення
# приватного атрибуту. Створіть протектед атрибут account_holder.
class Account:
    def __init__(self):
        self.__balance = 100
        self._account_holder = 'Anton'

    def account_info(self):
        return  self.__balance


a = Account()
print(a.account_info())
