# Напишіть ітератор CyclicIterator, який бере довільний ітерабельний
# об('єкт і циклічно перебирає його до нескінченності.'
#    ' Наприклад [”a”, “b”, “c”] → a, b, c, a, b, c, a, b…..)
#
# Приклад використання:
# for i in CyclicIterator([1, 2, 3]):
#  print(i)
#
# # 1 2 3 1 2 3 1 ...
class CyclicIterator:
    def __init__(self, info_list):
        self.info_list = info_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.info_list:
            print('Список пустий')
            raise StopIteration
        else:
            if self.index >= len(self.info_list):
                self.index = 0
            result = self.info_list[self.index]
            self.index += 1
            return result


for i in CyclicIterator([1, 2, 3]):
    print(i, end=' ')
