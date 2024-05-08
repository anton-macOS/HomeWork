# До попереднього завдання додайте клас Electric та додайте туди приватний атрибут
# battery та метод charge() який буде встановлювати атрибут battery до 100.
# Створіть окремий клас ElectricCar та ElectricMoto та успадкуйтесь від Vehicle та Electric.
# Створіть інстанси всіх класів, та викличте метод mro для кожного інстансу, щоб подивитись
# порядок успадкування в кожному класі.
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


class Electric():
    def __init__(self, battery):
        self.__battery = battery

    def charge(self):
        self.__battery = 100
        return f'Battery charge is {self.__battery}'



class ElectricCar(Vehicle, Electric):
    def __init__(self, name, model, battery):
        Vehicle.__init__(self, name, model)
        Electric.__init__(self, battery)


class ElectricMoto(Vehicle, Electric):
    def __init__(self, name, model, battery):
        Vehicle.__init__(self, name, model)
        Electric.__init__(self, battery)


car = ElectricCar('Mercedes', 'EQS', 50)
moto = ElectricMoto('Ducati', 'Electricity', 70)
print(ElectricCar.mro())
print(ElectricMoto.mro())

