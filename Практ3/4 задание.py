list = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]

# Находим минимальный элемент списка
min_element = min(list)

# Удаляем минимальный элемент из списка
list.remove(min_element)

# Добавляем минимальный элемент в нужное место по условию
if min_element < 0:
    list.append(min_element)  # В конец, если меньше 0
else:
    list.insert(0, min_element)  # В начало, если >= 0

# Вывод измененного списка
print(list)
