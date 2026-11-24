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

# 2. Преобразование каждой строки
for i in range(m):
    # Запоминаем первый элемент строки как начальный минимум и максимум
    min_val = matrix[i][0]
    max_val = matrix[i][0]
    min_idx = 0
    max_idx = 0
    
    # Ищем минимум и максимум в текущей строке
    for j in range(1, n):
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]
            min_idx = j  # Запоминаем индекс минимума
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_idx = j  # Запоминаем индекс максимума
            
    # 3. Меняем местами минимальный и максимальный элементы
    # В Python можно сделать это без временной переменной!
    matrix[i][min_idx], matrix[i][max_idx] = matrix[i][max_idx], matrix[i][min_idx]

# 4. Выводим преобразованную матрицу
print("\nПреобразованная матрица:")
for row in matrix:
    print(row)