# Створіть ітератор, який буде фільтрувати значення.
# Ітератор приймає ітеровану послідовність та функцію.
# Якщо функція на елементі поверне True то ми повертаємо цей елемент.
# Важливо, працювати з цим ітератором за допомогою циклу while проходячись
#     по ньому за допомогою методів ітератора.
#
# Приклад використання:
# f_iter = FilterIterator([1, 2, 3, 4], lambda x: x % 2 == 0)
# while True:
#     try:
#         next(f_iter)
#     except StopIteration:
#         break
#
# # 2 4
class FilterIterator:
    index = 0

    def __init__(self, info, rule):
        self.info = info
        self.rule = rule

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.info):
            value = self.info[self.index]
            if self.rule(value):
                print(value)
            self.index += 1
        raise StopIteration


f_iter = FilterIterator([1, 2, 3, 4], lambda x: x % 2 == 0)
while True:
    try:
        next(f_iter)
    except StopIteration:
        break




