# Створіть клас Rectangle для представлення прямокутника.
# Додайте методи для обчислення площі та периметра прямокутника.
# Створіть об'єкт Rectangle і викличте ці методи.
#
# Приклад використання:
# rect = Rectangle(2, 4)
# square = rect.square()
# perimeter = rect.perimeter()
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def __repr__(self):
        return (f'Square of rectangle is {Rectangle.square(self)} '
                f'\nPerimeter of rectangle is {Rectangle.perimeter(self)}')

    def __str__(self):
        return self.__repr__()


rect = Rectangle(2, 4)
square = rect.square()
perimeter = rect.perimeter()
print(rect)
