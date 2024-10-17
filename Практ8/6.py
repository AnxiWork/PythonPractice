# Читаем и выводим содержимое CSV-файла
import csv

with open("data.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(", ".join(row))  # Выводим строки с разделителем