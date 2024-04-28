# Напишіть генератор Фібоначчі, який видає числа у послідовності Фібоначчі
#
# Приклад використання:
# for i in fibonacci():
#  print(i)
#
# # 0, 1, 1, 2, 3, 5 ....
def fibonacci(max_nums):
    count = 1
    a, b = 0, 1
    while count <= max_nums:
        yield a
        a, b = b, a + b
        count += 1


for i in fibonacci(10):
    print(i)






