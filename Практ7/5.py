# Функция считает количество гласных в строке
def count_vowels(text):
    vowels = "aeiouAEIOU"  # Список гласных, включая заглавные
    return sum(1 for char in text if char in vowels)  # Подсчитываем гласные

# Проверяем на примере
print(count_vowels("Hello World"))