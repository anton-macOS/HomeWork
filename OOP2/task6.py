# До класу Account додайте за допомогою декоратора @property гетер та сетер для приватного
# атрибуту balance. При встановлені цього параметру зробіть перевірку у сетері,
# щоб це значення було більшим за 0.
class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def get_balance(self):
        return self.__balance

    @get_balance.setter
    def get_balance(self, value):
        if value < 0:
            raise 'Value must be more that 0'
        else:
            self.__balance = value


a = Account(100)
print(a.get_balance)
a.get_balance = 1000
print(a.get_balance)



