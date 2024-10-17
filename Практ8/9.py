# Шифруем и дешифруем записи в дневнике
def encrypt(text, shift):
    return ''.join(chr((ord(char) + shift - 32) % 95 + 32) for char in text)

def decrypt(text, shift):
    return ''.join(chr((ord(char) - shift - 32) % 95 + 32) for char in text)

message = input("Введите сообщение: ")
encrypted = encrypt(message, 3)  # Шифруем со сдвигом 3
print("Зашифровано:", encrypted)
print("Расшифровано:", decrypt(encrypted, 3))