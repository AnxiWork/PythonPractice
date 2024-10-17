# Функция ищет наибольшую букву в строке
def find_largest_letter(text):
    return max(text)  # max вернет букву с наибольшим ASCII значением

# Проверяем на примере
print(find_largest_letter("hello"))