a = float(input("Введите точку A: "))
b = float(input("Введите точку B: "))
c = float(input("Введите точку C: "))

length_ac = abs(a-c)
length_bc = abs(b-c)
sum_lenght = length_ac+length_bc

print(f"Расстояние между точками A({a}) и C({c}): {length_ac}")
print(f"Расстояние между точками B({b}) и C({c}): {length_bc}")
print(f"Сумма отрезков AC и BC: {sum_lenght}")