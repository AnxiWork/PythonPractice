# Считаем количество уникальных слов в файле
from collections import Counter

with open("sample.txt", "r") as file:
    words = file.read().split()  # Разбиваем текст на слова
    unique_words = Counter(words)  # Считаем вхождения слов

print(dict(unique_words))