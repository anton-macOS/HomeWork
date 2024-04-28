# Напишіть ітератор, який буде працювати так само як функція range,
# приймати початковий елемент, останній та крок.
#
# Приклад використання:
# for i in RangeIterator(1, 10, 2):
#  print(i)
#
# # 1, 3, 5, 7, 9
class RangeIterator:
    def __init__(self, start, stop, step):
        self.start = start
        self.end = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            current = self.start
            self.start += self.step
            return current


for i in RangeIterator(1, 10, 2):
    print(i)
