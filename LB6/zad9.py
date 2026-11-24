# 1. Ввод размеров и матрицы
m = int(input("Введите количество строк M: "))
n = int(input("Введите количество столбцов N: "))

matrix = []
print(f"Введите элементы матрицы (по {n} чисел в каждой строке):")
for i in range(m):
    while True:
        row = list(map(int, input().split()))
        if len(row) == n:
            matrix.append(row)
            break
        print(f"Ошибка! Введите ровно {n} чисел.")

# 2. Сортировка строк (пузырьком)
# Внешний цикл отвечает за количество проходов
for i in range(m - 1):
    # Внутренний цикл сравнивает соседние строки
    for j in range(m - 1 - i):
        # Если первый элемент текущей строки больше первого элемента следующей
        if matrix[j][0] > matrix[j+1][0]:
            # Меняем строки местами целиком!
            matrix[j], matrix[j+1] = matrix[j+1], matrix[j]

# 3. Вывод результата
print("\nУпорядоченная матрица:")
for row in matrix:
    print(row)