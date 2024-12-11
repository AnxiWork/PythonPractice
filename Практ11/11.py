
# Лабораторная 11: Работа с файлами и исключениями

# Задание 1: Запись строк в файл
# Запрашиваем строки у пользователя и записываем их в файл.
with open("file_strings.txt", "w") as file:
    while True:
        line = input("Введите строку (пустая строка для завершения): ")
        if not line:
            break
        file.write(line + "\n")

# Задание 2: Чтение строк из файла
# Читаем строки из файла и выводим их.
try:
    with open("file_strings.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Файл не найден.")

# Задание 3: Работа с несуществующим файлом
# Пытаемся открыть несуществующий файл и обрабатываем исключение.
try:
    with open("nonexistent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Ошибка: файл отсутствует.")
