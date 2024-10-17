# Читаем файл и записываем строки в обратном порядке
with open("sample.txt", "r") as file:
    lines = file.readlines()  # Считываем все строки

with open("reversed.txt", "w") as file:
    file.writelines(reversed(lines))  # Записываем строки наоборот