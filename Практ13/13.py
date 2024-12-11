
# Лабораторная 13: Основы ООП

# Задание 1: Класс Автомобиль
# Создаём класс для описания автомобиля.
class Car:
    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def show_info(self):
        print(f"Автомобиль {self.model} с {self.wheels} колёсами движется со скоростью {self.speed} км/ч.")

car1 = Car(4, "Седан", 180)
car2 = Car(4, "Купе", 200)
car1.show_info()
car2.show_info()

# Задание 2: Класс Прямоугольник
# Класс для расчёта площади и периметра прямоугольника.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print("Площадь:", rect.area())
print("Периметр:", rect.perimeter())
