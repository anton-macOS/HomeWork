# Напишіть простий декоратор, який буде прінтити повідомлення
# “Function is been called” до та після виклику функції. Будьте уважні,
# деворатор повинен працювати з усіма функціями, які приймають різні параметри,
# та не забувайте повертати результат роботи функції.
#
# Приклад використання:
# @called_decorator
# def some_func(1, b, c):
#     ...
#     some code
#     ...
def called_decorator(func):
    def print_func(*args, **kwargs):
        print('Function is been called')
        func(*args, **kwargs)
        print('Function is been called')

    return print_func


@called_decorator
def new_inputs(a, b, c):
    print(a * b + c)


new_inputs(1, 5, 5)



