import math

x1 = float(input("Введите xA: "))
y1 = float(input("Введите yA: "))
x2 = float(input("Введите xB: "))
y2 = float(input("Введите yB: "))
x3 = float(input("Введите xC: "))
y3 = float(input("Введите yC: "))

# Считаем расстояния по теореме Пифагора
dist_ab = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
dist_ac = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

# Проверка растояния точек
if dist_ab < dist_ac:
    print(f"\nТочка B ближе к A. \nРасстояние: {dist_ab:.2f}")
elif dist_ac < dist_ab:
    print(f"\nТочка C ближе к A. \nРасстояние: {dist_ac:.2f}")
else:
    print(f"\nТочки B и C на одинаковом расстоянии от A: {dist_ab:.2f}")