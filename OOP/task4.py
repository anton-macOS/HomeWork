# До класу Circle створеного у попередньому завданні додайте два метода,
# класметод from_diameter, який буде приймати діаметр та повертати екземпляр
# класу з радіусом розрахованим з переданого у метод діаметру.
# Додайте статикметод check_radius, який буде отримувати радіус,
# та перевіряти його на валідність (радіус повинен бути більший за 0)
#
# Приклад використання:
# circle = Circle.from_diameter(10)
# area = circle.area()
# valid = Circle.check_radius(17)
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    @staticmethod
    def check_radius(radius):
        return radius > 0

    def __repr__(self):
        return (f'Radius id {self.radius}'
                f'\nArea is {self.area()}'
                f'\nValid - {Circle.check_radius(self.radius)}')

    def __str__(self):
        return self.__repr__()


circle = Circle.from_diameter(10)
area = circle.area()
valid = Circle.check_radius(17)
print(circle)
