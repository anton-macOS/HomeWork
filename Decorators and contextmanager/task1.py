# Створіть простий контекстний менеджер FIleOpener, який буде відкривати файл,
# повертати його та закривати при виході з контексту
#
# Приклад використання:
# with FileOpener("file.txt", "r") as f:
#     f.read()
class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


with FileOpener("./Decorators and contextmanager/file.txt", "r") as f:
    f.read()
