# Створіть клас Vehacle який матиме атрибути make та model та метод get_info()
# який буде повертатиінформацію про марку та модель авто. Створіть ще два класи Car
# та Moto які будуть додавати додаткові атрибути wheels і успадковуватись від Vehacle .
# Створіть сутності класів Car та Moto та викличте там метод get_info()
class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def get_info(self):
        return f'Vehicle name is {self.name}, model - {self.model}'


class Car(Vehicle):
    def __init__(self, name, model, wheels):
        super().__init__(name, model)
        self.wheels = wheels

    def get_info(self):
        print(super().get_info())
        return f'And have {self.wheels} wheels'


class Moto(Vehicle):
    def __init__(self, name, model, wheels):
        super().__init__(name, model)
        self.wheels = wheels

    def get_info(self):
        print(super().get_info())
        return f'And have {self.wheels} wheels'


car1 = Car('Mercedes', 'ML350', 4)
moto1 = Moto('Ducati', 'Penigale', 2)

print(car1.get_info())
print()
print(moto1.get_info())
