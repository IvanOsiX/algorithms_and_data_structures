while True:
    a = float(input("Введите первое ненулевое число: "))
    b = float(input("Введите второе ненулевое число: "))
    if a != 0 and b != 0:
        break
    print("Ошибка! Числа не должны быть равны нулю. Попробуйте снова.")

a_square = a*a
b_square = b*b

print(f"Сумма квадратов (a² + b²): {a_square + b_square}")
print(f"Разность квадратов (a² - b²): {a_square - b_square}")
print(f"Произведение квадратов (a² * b²): {a_square * b_square}")
print(f"Частное квадратов (a² / b²): {a_square / b_square}")