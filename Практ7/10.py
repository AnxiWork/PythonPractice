# Функция считает количество делителей числа n
def count_divisors(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)  # Проверяем все числа на делимость

# Проверяем на примере
print(count_divisors(12))