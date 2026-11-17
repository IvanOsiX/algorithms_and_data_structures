import math

x1 = float(input("Введите координату x1: "))
y1 = float(input("Введите координату y1: "))
x2 = float(input("Введите координату x2: "))
y2 = float(input("Введите координату y2: "))

dx = x2 - x1
dy = y2 - y1

distance = math.sqrt(dx**2 + dy**2)

print(f"Расстояние между точками: {distance:.2f}")