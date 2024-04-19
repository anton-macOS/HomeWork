# Напишіть декоратор, який буде прінтити
# “{імʼя функції яку викликали} is been called with parameters:
#     {список параметрів з якими функцію викликали}”,
#     а після виклику функції “Function {function_name} return this value: {значення яке функція повернула}”
#
# Приклад використання:
# @function_info
# def some_func(a, b, c):
#     ...
#     code
#     return ...
def function_info(func):
    def print_func(*args):
        print(f'{func.__name__} is been called with parameters: {args}')
        result = func(*args)
        print(f'Function {func.__name__} return this value: {result}')
    return print_func


@function_info
def some_func(a, b, c):
    return a * b + c


some_func(1, 2, 3)
