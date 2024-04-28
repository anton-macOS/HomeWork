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
import math as m

def permutation(nums: list):
    start = 0
    for i in range(start, m.factorial(len(nums))):
        nums[0], nums[i] = nums[i], nums[0]
        yield nums




for i in permutation([1, 2, 3]):
    print(i)
