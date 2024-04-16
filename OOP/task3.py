# Створіть клас Circle зі змінною класу pi, рівною 3.14.
# Додайте змінну екземпляру radius, ініціалізовану через конструктор.
# Додайте метод area, який обчислює і повертає площу круга.
#
# Приклад використання:
# circle = Circle(10)
# area = circle.area()
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2


circle = Circle(30)
area = circle.area()
print(f'Circle area is {round(area, 2)}')
