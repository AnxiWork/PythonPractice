# Функция вычисляет факториал числа n
def factorial(n):
    result = 1  # Начинаем с 1, так как умножение на 0 даст 0
    for i in range(2, n + 1):
        result *= i  # Умножаем все числа от 2 до n
    return result

# Проверяем факториал 5
print(factorial(5))