# Запрашиваем размеры матрицы
m = int(input("Введите количество строк M: "))
n = int(input("Введите количество столбцов N: "))

matrix = []

print(f"Введите элементы матрицы (по {n} чисел в каждой строке):")
for i in range(m):
    while True:
        # Вводим строку и сразу превращаем её в список чисел
        row = list(map(int, input().split()))
        
        # Проверяем: совпадает ли количество введенных чисел с N?
        if len(row) == n:
            matrix.append(row)
            break  # Всё верно, переходим к следующей строке
        else:
            print(f"Ошибка! Вы ввели {len(row)} чисел, а нужно ровно {n}. Попробуйте снова.")

# Защита от некорректного ввода K
while True:
    k = int(input(f"Введите номер строки K (от 1 до {m}): "))
    if 1 <= k <= m:
        break
    print(f"Ошибка! K должно быть от 1 до {m}.\n")

# Получаем нужную строку (K-1 из-за индексации с нуля)
target_row = matrix[k - 1]

# Считаем сумму и произведение
total_sum = 0
total_product = 1

for element in target_row:
    total_sum += element
    total_product *= element

# Выводим результат
print(f"Строка {k}: {target_row}")
print(f"Сумма элементов: {total_sum}")
print(f"Произведение элементов: {total_product}")