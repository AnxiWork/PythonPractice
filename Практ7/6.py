# Эта функция вычисляет среднее значение списка чисел
def calculate_average(numbers):
    return sum(numbers) / len(numbers)  # Сумма делится на количество элементов

# Проверяем на примере
print(calculate_average([1, 2, 3, 4, 5]))