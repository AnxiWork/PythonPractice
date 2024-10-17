# Функция создает числовую последовательность от start до end включительно
def generate_sequence(start, end):
    return list(range(start, end + 1))  # Генерируем список с помощью range

# Проверяем на примере
print(generate_sequence(1, 10))