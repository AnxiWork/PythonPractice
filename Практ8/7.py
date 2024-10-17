# Логируем данные вместе с текущей датой и временем
from datetime import datetime

with open("log.txt", "a") as log:
    data = input("Введите данные: ")  # Ввод от пользователя
    log.write(f"{datetime.now()}: {data}\n")