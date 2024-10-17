# Копируем содержимое одного файла в другой
def copy_file(source, target):
    with open(source, "r") as src, open(target, "w") as tgt:
        tgt.write(src.read())  # Читаем и записываем содержимое

copy_file("sample.txt", "copy.txt")