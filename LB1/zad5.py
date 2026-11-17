while True:
    a = float(input("Введите первое ненулевое число: "))
    b = float(input("Введите второе ненулевое число: "))
    
    if a != 0 and b != 0:
        break
    print("Ошибка! Числа не должны быть равны нулю. Попробуйте снова.")

a_abs = abs(a)
b_abs = abs(b)

sum_abs = a_abs + b_abs
raz_abs = a_abs - b_abs
proiz_abs = a_abs * b_abs
chas_abs = a_abs / b_abs

print(f"Сумма модулей (|{a}| + |{b}|): {sum_abs}")
print(f"Разность модулей (|{a}| - |{b}|): {raz_abs}")
print(f"Произведение модулей (|{a}| * |{b}|): {proiz_abs}")
print(f"Частное модулей (|{a}| / |{b}|): {chas_abs}")