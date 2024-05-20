# Напишіть метаклас, який буде перейменовувати всі атрибути,
# назва яких починається з '__' на атрибути '__private_{attr}
class MyMetaClass(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        class_name = f'_{name}__'
        for attr_name, attr_value in attrs.items():
            if attr_name.startswith(class_name) and not attr_name.endswith('__'):
                old_attr_name = attr_name[len(class_name):]
                new_attr_name = f'_{name}__private_{old_attr_name}'
                new_attrs[new_attr_name] = attr_value
            else:
                new_attrs[attr_name] = attr_value
        return super().__new__(cls, name, bases, new_attrs)


class NewClass(metaclass=MyMetaClass):
    __name = 'Anton'
    age = 33
    __height = 191


class OneMoreClass(metaclass=MyMetaClass):
    name = 'Vlad'
    __age = 25
    __height = 195


anton = NewClass()
vlad = OneMoreClass()
print(anton._NewClass__private_name)
print(vlad._OneMoreClass__private_age)
print()
print(dir(anton))
print(dir(vlad))
