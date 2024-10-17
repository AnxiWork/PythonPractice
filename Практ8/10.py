# Анализируем текстовый файл и выводим статистику
def file_statistics(file):
    with open(file, "r") as f:
        text = f.read()
    num_chars = len(text)  # Количество символов
    num_words = len(text.split())  # Количество слов
    num_sentences = text.count('.') + text.count('!') + text.count('?')  # Количество предложений
    avg_word_length = num_chars / num_words if num_words else 0  # Средняя длина слова
    print(f"Символов: {num_chars}, Слов: {num_words}, Предложений: {num_sentences}, Средняя длина слова: {avg_word_length:.2f}")

file_statistics("sample.txt")