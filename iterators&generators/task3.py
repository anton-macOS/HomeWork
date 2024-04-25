# Напишіть функцію-генератор перестановок,
# яка отримує список елементів і видає усі можливі перестановки цих елементів.
#
# Приклад використання:
# for i in permutations([1, 2, 3]):
#  print(i)
#
# # [1, 2, 3]
# # [1, 3, 2]
# # [2, 1, 3]
# # ...

def permutation(nums: list):
    for i in range(len(nums)):
        yield nums


for i in permutation([1, 2, 3]):
    print(i)
