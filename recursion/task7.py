# Створіть простий метаклас, який буде прінтити будь яке повідомлення,
# коли новий клас створюється за його допомогою.

class MyMetaClass(type):
    def __new__(cls, name, base, attrs):
        print('Hello I am new class - {} by MetaClass'.format(name))
        return super().__new__(cls, name, base, attrs)


class NewClass(metaclass=MyMetaClass):
    pass


class OneMoreNewClass(metaclass=MyMetaClass):
    pass
