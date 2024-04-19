# Напишіть декоратор, який приймає як параметр число, та робить time.sleep
# перед викликом декорованої функції на це число.
#
# Приклад використання:
# @sleeper(5)
# def some_func(a, b, ...):
#     ...
import time


def new_decorator(secs):
    def sleeper(func):
        def new_func(*args, **kwargs):
            print(f'Функція зʼявиться через {secs} секунд!')
            for sec in range(secs + 1):
                time.sleep(1)
                print(secs - sec)
            print(func(*args, **kwargs))

        return new_func
    return sleeper


@new_decorator(10)
def some_func(a, b, c):
    return f'Результат: {a * b + c}'


some_func(1, 2, 3)
