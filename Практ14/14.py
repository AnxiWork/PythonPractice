
# Лабораторная 14: Конструкторы и методы

# Задание 1: Конструктор для класса Car
# Создаём конструктор, устанавливающий значения атрибутов.
class Car:
    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def show_info(self):
        print(f"Модель: {self.model}, Скорость: {self.speed}, Колёс: {self.wheels}")

car1 = Car(4, "Седан", 180)
car2 = Car(4, "Спорткар", 220)
car1.show_info()
car2.show_info()
