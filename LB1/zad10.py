import math

while True:
    x1 = float(input("Введите x1: "))
    y1 = float(input("Введите y1: "))
    x2 = float(input("Введите x2: "))
    y2 = float(input("Введите y2: "))
    x3 = float(input("Введите x3: "))
    y3 = float(input("Введите y3: "))

    area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

    # Проверка, если площадь равна 0
    # 1e-9 (это 0.000000001), чтобы избежать ошибок округления компьютера
    if area < 1e-9:
        print("\nОшибка! Точки лежат на одной прямой. Треугольник не существует.")
        print("Пожалуйста, введите координаты заново.\n")
        continue  # Возвращаемся в начало цикла и просим ввести заново

    side_ab = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    side_bc = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    side_ca = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    
    perimeter = side_ab + side_bc + side_ca

    print(f"\nПериметр треугольника: {perimeter:.2f}")
    print(f"Площадь треугольника: {area:.2f}")
    
    break