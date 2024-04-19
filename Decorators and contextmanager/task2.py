# Створіть простий контекстний менеджер file_opener за допомогою декоратора з contextlib,
# який буде відкривати файл, повертати його та закривати при виході з контексту
#
# Приклад використання:
# with file_opener("file.txt", "r") as f:
# f.read()
from contextlib import contextmanager
@contextmanager
def file_opener(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()


with file_opener("./Decorators and contextmanager/file.txt", "r") as f:
    print(f.read())


