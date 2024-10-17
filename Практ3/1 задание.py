# Создание списка с помощью цикла for
first_list = [i for i in range(1, 6)]  # Список из 5 элементов: [1, 2, 3, 4, 5]

# Создание пустого списка и выполнение операций
second_list = []           # Пустой список
second_list.append(5)      # Добавление числа 5
second_list.append(-6)     # Добавление числа -6
second_list.extend(first_list)  # Добавление всего первого списка целиком
second_list.sort()         # Сортировка списка

# Вывод обоих списков
print("Первый список:", first_list)
print("Второй список:", second_list)
