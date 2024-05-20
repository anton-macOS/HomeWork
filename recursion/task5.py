# Напишіть рекурсивну функцію, яка знаходить n-не число послідовності фібоначчі.
#
# Приклад роботи:
# result = recursive_fibonacci(10)   # 34

def recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


print(recursive_fibonacci(10))
