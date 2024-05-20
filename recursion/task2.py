# Напишіть рекурсивну функцію, яка обчислює факторіал заданого числа.
#
# Приклад роботи:
# result = recursive_fectorial(5)   # 120

def recursive_factorial(n):
    if n <= 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


print(recursive_factorial(5))