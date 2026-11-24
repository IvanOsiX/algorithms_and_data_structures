# 1. Ввод размеров и матрицы (с проверкой длины строк)
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

# 2. Поиск столбца с наименьшим произведением
# Заводим переменные для хранения лучшего результата.
# min_product пока равен None (ничего не найдено), а индекс -1.
min_product = None
min_col_index = -1

# Внешний цикл перебирает СТОЛБЦЫ (от 0 до N-1)
for j in range(n):
    # Для каждого нового столбца произведение начинается с 1
    current_product = 1
    
    # Внутренний цикл перебирает СТРОКИ в текущем столбце
    for i in range(m):
        current_product *= matrix[i][j]
        
    # Проверяем: если это первый проверенный столбец ИЛИ произведение меньше найденного
    if min_product is None or current_product < min_product:
        min_product = current_product
        min_col_index = j # Запоминаем индекс столбца (от 0)

# 3. Вывод результата
# Прибавляем 1 к индексу, так как люди считают столбцы с 1, а не с 0
print(f"Номер столбца с наименьшим произведением: {min_col_index + 1}")
print(f"Наименьшее произведение: {min_product}")