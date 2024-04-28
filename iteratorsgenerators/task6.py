# Додайте до попереднього ітератора CycleIterator метод peek,
# який буде підглядувати та повертати наступне значення, але не переходити
# на наступну ітерацію. Наприклад ітератор вже повернув a, b наступний елемент - c,
# якщо я викличу peek він його поверне, а якщо я викличу next()
# або в циклі наступну ітерацію викличу він повинен все одно повернути c
#
# Приклад використання:
# cycle_iter = CycleIterator([1, 2, 3])
# print(next(cycle_iter))
# print(cycle_iter.peak())
# print(next(cycle_iter))
#
# # 1 2 2 ...
class CyclicIterator:
    def __init__(self, info_list):
        self.info_list = info_list
        self.index = 0

    def __iter__(self):
        return self

    def peak(self):
        result = self.info_list[self.index]
        return result

    def __next__(self):
        if not self.info_list:
            print('Список пустий')
            raise StopIteration
        else:
            result = self.info_list[self.index]
            self.info_list.append(result)
            self.index += 1
            return result


cycle_iter = CyclicIterator([1, 2, 3])
print(next(cycle_iter))
print(f'Настпупний буде - {cycle_iter.peak()}')
print(next(cycle_iter))
