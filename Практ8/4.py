# Объединяем несколько файлов в один
def merge_files(files, target):
    with open(target, "w") as outfile:
        for fname in files:
            with open(fname, "r") as infile:
                outfile.write(infile.read())  # Записываем содержимое каждого файла

merge_files(["file1.txt", "file2.txt"], "merged.txt")