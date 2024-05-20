# Напишіть рекурсивну функцію, яка обчислює суму цифр заданого числа.
#
# Приклад роботи:
# result = recursive_sum(1234)   # 10

def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + recursive_sum(n // 10)


print(recursive_sum(1234))
