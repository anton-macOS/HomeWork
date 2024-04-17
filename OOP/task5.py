# Розробіть клас Vehicle для представлення транспортного засобу.
# Додайте атрибути, такі як назва, швидкість і вартість.
# Реалізуйте метод __gt__, який порівнює два транспортних засоби за швидкістю.
# Створіть список транспортних засобів і відсортуйте його за швидкістю за допомогою функції sorted()
#
# Приклад використання:
# v1 = Vehicle("Name1", 100, 10000)
# v2 = Vehicle("Name2", 110, 9000)
# result = sorted([v1, v2])
# print(v1 > v2)
class Vehicle:
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        return self.speed > other.speed

    def __repr__(self):
        return f'{self.speed}'

    def __str__(self):
        return self.speed


v1 = Vehicle("Name1", 100, 10000)
v2 = Vehicle("Name2", 110, 9000)
result = sorted([v1, v2])
print(result)
print(v1 > v2)
