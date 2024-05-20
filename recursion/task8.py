# Напишіть реалізацію патерну SIngleton за допомогою створення метакласу.
# Сінглтон - це патерн при якому ми можемо створити лише 1 інстанс для нашого класу.
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            _instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = _instance
        return cls._instances[cls]


class MainClass(metaclass=SingletonMeta):
    pass


class SecondClass(metaclass=SingletonMeta):
    pass


first = MainClass()
second = MainClass()
print(id(first) == id(second))
