some = [9, "Hi", 23.5, "A"]

# Ввод количества элементов
N = int(input("Введите количество новых элементов: "))

# Ввод N элементов и добавление их в список
for _ in range(N):
    new_element = input("Введите новый элемент: ")
    some.append(new_element)

# Вывод списка
print(some)
