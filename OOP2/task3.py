# Створи абстрактний клас Shape та додай метод area, успадкуйся від цього класу
# та створи два класи Rectangle та Circle реалізувавши метод area.
# Створи інстанси класів Circle та Rectangle та виклич метод area.
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


r = Rectangle(2, 3)
c = Circle(20)
print(r.area())
print(round(c.area(), 2))
