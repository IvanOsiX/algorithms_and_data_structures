# 1. Ввод размеров (с проверкой на четность)
while True:
    m = int(input("Введите количество строк M (четное): "))
    n = int(input("Введите количество столбцов N (четное): "))
    if m > 0 and n > 0 and m % 2 == 0 and n % 2 == 0:
        break
    print("Ошибка! M и N должны быть положительными четными числами.\n")

# 2. Ввод матрицы
matrix = []
print(f"Введите элементы матрицы (по {n} чисел в каждой строке):")
for i in range(m):
    while True:
        row = list(map(int, input().split()))
        if len(row) == n:
            matrix.append(row)
            break
        print(f"Ошибка! Введите ровно {n} чисел.")

# 3. Находим середины матрицы
mid_m = m // 2
mid_n = n // 2

# 4. Меняем четверти местами
# Перебираем только левую верхнюю четверть
for i in range(mid_m):
    for j in range(mid_n):
        # Меняем элемент из левой верхней на элемент из правой нижней
        # (i + mid_m) и (j + mid_n) сдвигают нас в правую нижнюю четверть
        matrix[i][j], matrix[i + mid_m][j + mid_n] = matrix[i + mid_m][j + mid_n], matrix[i][j]

# 5. Вывод результата
print("\nПреобразованная матрица:")
for row in matrix:
    print(row)