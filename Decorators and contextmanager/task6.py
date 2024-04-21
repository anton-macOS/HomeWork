# Напишіть декоратор, який буде приймати необмежену кількість
# типів даних (str, int і так далі) та перевіряти аргументи які передали
# в декоровану функцію на те чи вони є типами, які передали в декоратор,
# та повертати помилку якщо ні. Наприклад ми передали @my_decorator(int, str)
# а декоровану функцію викликали з аргументами func(2, “hello”, True) повинна
# повернутись помилка бо ми не очікуємо bool тип.
#
# Приклад використання:
# @type_checker(int, str)
# def some_func(a, b, c):
#     ...
def type_checker(*expected_types):
    def new_decorator(func):
        def wrapper(*args, **kwargs):
            for i in args:
                if type(i) not in expected_types:
                    raise Exception(f'Не очікуємо {type(i).__name__}')
            for value in kwargs.values():
                if type(value) not in expected_types:
                    raise Exception(f'Не очікуємо {type(value).__name__}')
            print('Все гуд')
            return func(*args, **kwargs)
        return wrapper
    return new_decorator


@type_checker(str, int, bool)
def new_func(a, b, c):
    return a, b, c


result = new_func(1, 'Hello', True)
print(result)
