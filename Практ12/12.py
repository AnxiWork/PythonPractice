
# Лабораторная 12: Модули в Python

# Задание 1: Модуль math
# Вычисляем площадь круга с использованием числа π из модуля math.
from math import pi, ceil

radius = float(input("Введите радиус круга: "))
area = pi * radius ** 2
print("Площадь круга:", ceil(area))

# Задание 2: Генерация случайного числа
# Используем модуль random для генерации случайного числа.
import random

number = random.randint(1, 10)
print("Случайное число от 1 до 10:", number)

# Задание 3: Работа с модулем datetime
# Выводим текущую дату и время в определённом формате.
from datetime import datetime

now = datetime.now()
print("Текущая дата и время:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Задание 4: Работа с модулем os
# Вывод текущего каталога и изменение его.
import os

print("Текущий каталог:", os.getcwd())
new_dir = input("Введите путь для смены каталога: ")
try:
    os.chdir(new_dir)
    print("Каталог изменён на:", os.getcwd())
except FileNotFoundError:
    print("Ошибка: каталог не найден.")
