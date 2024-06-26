# Напишіть декоратор, який приймає як параметр число, та робить time.sleep
# перед викликом декорованої функції на це число.
#
# Приклад використання:
# @sleeper(5)
# def some_func(a, b, ...):
#     ...
import time


def sleeper(secs):
    def new_decorator(func):
        def new_func(*args, **kwargs):
            print(f'Функція зʼявиться через {secs} секунд!')
            for sec in range(secs + 1):
                time.sleep(1)
                print(secs - sec)
            print(f'Результат: {func(*args, **kwargs)}')
            return func(*args, **kwargs)
        return new_func
    return new_decorator


@sleeper(5)
def some_func(a, b, c):
    return a * b + c


res = some_func(1, 2, 3)
print(res)
