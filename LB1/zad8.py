while True:
    a = float(input("Введите точку A: "))
    b = float(input("Введите точку B: "))
    c = float(input("Введите точку C: "))
    
    if (a < c < b) or (b < c < a):
        break
    else:
        print("Ошибка! Точка C должна находиться между A и B. Попробуйте снова.\n")

length_ac = abs(a - c)
length_bc = abs(b - c)
sum_lengths = length_ac * length_bc

print(f"Длина отрезка AC: {length_ac}")
print(f"Длина отрезка BC: {length_bc}")
print(f"Произведение длин отрезков AC и BC: {sum_lengths}")