
# Лабораторная 15: Наследование и инкапсуляция

# Задание 1: Наследование
# Создаём базовый класс Vehicle и класс-наследник Motorcycle.
class Vehicle:
    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def show_info(self):
        print(f"Транспорт {self.model} с {self.wheels} колёсами, скорость {self.speed} км/ч.")

class Motorcycle(Vehicle):
    def __init__(self, wheels, model, speed, engine):
        super().__init__(wheels, model, speed)
        self.engine = engine

    def show_engine(self):
        print(f"Мотоцикл {self.model} имеет двигатель {self.engine}.")

moto = Motorcycle(2, "Спортбайк", 220, "V-Twin")
moto.show_info()
moto.show_engine()
