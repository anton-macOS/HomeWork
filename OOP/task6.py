# Розробіть клас Counter, який буде мати атрибут класу count.
# Створіть метод get_count який буде повертати атрибут класу count.
# Кожного разу, коли ми створюємо екземпляр класу Counter ми повинні
# збільшувати атрибут класу counter на 1, тим самим зберігаючи там кількість
# екземплярів створених для цього класу. А під час виклику метода get_count ми
# повинні фіксувати кількість викликів даного методу для кожного екземпляру.
#
# Приклад використання:
# c1 = Counter()
# c2 = Counter()
# result = c1.get_count()  # 2
# print(c1.method_called)  #1
class Counter:
    count = 0
    method_called = 0

    def __init__(self):
        Counter.count += 1

    def get_count(self):
        Counter.method_called += 1
        return self.count


c1 = Counter()
c2 = Counter()
result = c1.get_count()
result2 = c1.get_count()
print(c1.method_called)
