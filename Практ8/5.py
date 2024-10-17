# Ищем и заменяем слово в файле
def find_and_replace(file, find_word, replace_word):
    with open(file, "r") as f:
        content = f.read()
    with open(file, "w") as f:
        f.write(content.replace(find_word, replace_word))  # Замена слова

find_and_replace("sample.txt", "old", "new")