# Напишіть рекурсивну функцію, яка повертає лічільник з числа яке ми до неї передамо до 1-го.
# За допомогою модулю time зробіть затримку в 1 секунду між кожним повертанням лічільника.
#
# Приклад роботи:
# result = recursive_count_down(10)
# # 10
# # 9
# # 8
# # 7
# # 6
# # 5
# # 4
# # 3
# # 2
# # 1
import time as t


def recursive_count_down(n):
    if n <= 1:
        return 1
    else:
        print(n)
        t.sleep(1)
        return recursive_count_down(n - 1)


print(recursive_count_down(10))

