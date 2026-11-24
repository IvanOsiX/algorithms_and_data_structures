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

# 2. Поиск минимума и максимума по всей матрице
# Берем первый элемент как начальный минимум и максимум
min_val = matrix[0][0]
max_val = matrix[0][0]
min_col = 0
max_col = 0

for i in range(m):
    for j in range(n):
        # Если нашли новый минимум
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]
            min_col = j  # Запоминаем номер столбца
            
        # Если нашли новый максимум
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_col = j  # Запоминаем номер столбца

print(f"\nМинимальный элемент: {min_val} (в столбце {min_col + 1})")
print(f"Максимальный элемент: {max_val} (в столбце {max_col + 1})")

# 3. Меняем столбцы местами
# Проходим по каждой строке и меняем элементы в нужных столбцах
if min_col != max_col: # Проверка на случай, если все числа в матрице равны
    for i in range(m):
        # Множественное присваивание в Python
        matrix[i][min_col], matrix[i][max_col] = matrix[i][max_col], matrix[i][min_col]

# 4. Вывод результата
print("\nПреобразованная матрица:")
for row in matrix:
    print(row)