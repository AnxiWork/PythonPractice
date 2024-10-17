#калькулятор с проверкой ввода
num1 = float(input("Первое число: "))
operation = input("Операция (+, -, *, /): ")
num2 = float(input("Второе число: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка! Деление на ноль."
else:
    result = "Неверная операция!"

print("Результат:", result)
