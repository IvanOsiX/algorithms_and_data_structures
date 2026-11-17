x1 = float(input("Введите координату x1: "))
y1 = float(input("Введите координату y1: "))
x2 = float(input("Введите координату x2: "))
y2 = float(input("Введите координату y2: "))

width = abs(x2 - x1)
height = abs(y2 - y1)

area = width * height
perimeter = 2 * (width + height)

print(f"Ширина прямоугольника: {width}")
print(f"Высота прямоугольника: {height}")
print(f"Площадь прямоугольника (S): {area:.2f}")
print(f"Периметр прямоугольника (P): {perimeter:.2f}")