
# Лабораторная 10: Работа с конструкцией 'with...as'

# Задание 1: Открытие файла для записи
# Откроем файл для записи и запишем в него текст.
with open("file1.txt", "w") as file:
    file.write("Пример текста для файла.")

# Задание 2: Чтение из файла
# Запишем текст в файл и затем прочитаем его.
with open("file2.txt", "w") as file:
    file.write("Это текст для чтения.")
with open("file2.txt", "r") as file:
    print(file.read())

# Задание 3: Добавление текста в файл
# Пользователь вводит текст, который добавляется в файл.
with open("file3.txt", "a") as file:
    user_input = input("Введите текст для добавления: ")
    file.write(user_input + "\n")

# Задание 4: Безопасное деление чисел
# Функция для безопасного деления с обработкой исключений.
def safe_division():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print("Результат:", num1 / num2)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
    except ValueError:
        print("Ошибка: вводите только числа.")

safe_division()
