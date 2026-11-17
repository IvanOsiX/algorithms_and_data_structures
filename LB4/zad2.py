def fibonacci(n):
    # Базовые случаи: первые два числа известны заранее
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Рекурсивный шаг: сумма двух предыдущих чисел
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Защита от некорректного ввода
while True:
    try:
        num = int(input("Введите номер числа Фибоначчи (n >= 0): "))
        if num >= 0:
            break
        print("Ошибка! Номер не может быть отрицательным. Попробуйте снова.\n")
    except ValueError:
        print("Ошибка! Введите целое число.\n")

# Вызов функции и вывод результата
result = fibonacci(num)
print(f"{num}-е число Фибоначчи равно: {result}")