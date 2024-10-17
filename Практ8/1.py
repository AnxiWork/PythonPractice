# Читаем файл и считаем количество строк в нем
with open("sample.txt", "r") as file:
    print("Количество строк:", sum(1 for line in file))