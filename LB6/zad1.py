# Защита от некорректного ввода (M должно быть нечетным)
while True:
    try:
        m = int(input("Введите порядок матрицы M (нечетное число): "))
        if m > 0 and m % 2 != 0:
            break
        print("Ошибка! M должно быть положительным нечетным числом (1, 3, 5...).\n")
    except ValueError:
        print("Ошибка! Введите целое число.\n")

# 1. Создаем и заполняем матрицу
matrix = []
counter = 1
for i in range(m):
    row = []
    for j in range(m):
        row.append(counter)
        counter += 1
    matrix.append(row)

print("\nИсходная матрица:")
for row in matrix:
    print(row)

# 2. Алгоритм спирального обхода
print("\nЭлементы по спирали против часовой стрелки:")

top = 0
bottom = m - 1
left = 0
right = m - 1

# Работаем, пока границы не сойдутся в центре
while top <= bottom and left <= right:
    
    # 1. Первый столбец сверху вниз
    for i in range(top, bottom + 1):
        print(matrix[i][left], end=" ")
    left += 1 # Сдвигаем левую границу вправо

    # 2. Последняя строка слева направо
    for i in range(left, right + 1):
        print(matrix[bottom][i], end=" ")
    bottom -= 1 # Сдвигаем нижнюю границу вверх

    # 3. Последний столбец снизу вверх (если границы еще не пересеклись)
    if top <= bottom:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][right], end=" ")
        right -= 1 # Сдвигаем правую границу влево

    # 4. Первая строка справа налево (если границы еще не пересеклись)
    if left <= right:
        for i in range(right, left - 1, -1):
            print(matrix[top][i], end=" ")
        top += 1 # Сдвигаем верхнюю границу вниз

print() # Переход на новую строку в конце