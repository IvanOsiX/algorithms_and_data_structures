# Вводим размер массива
while True:
    try:
        n = int(input("Введите размер массива N: "))
        if n > 0:
            break
        print("Ошибка! N должно быть больше 0.\n")
    except ValueError:
        print("Ошибка! Введите целое число.\n")

# Вводим элементы массива
my_array = []

for i in range(n):
    element = int(input(f"Введите элемент A[{i + 1}]: "))
    my_array.append(element)

# Вводим K и L
while True:
    try:
        k = int(input("Введите K: "))
        l = int(input("Введите L: "))

        if 1 <= k <= l <= n:
            break
        print("Ошибка! Должно выполняться условие 1 <= K <= L <= N.\n")
    except ValueError:
        print("Ошибка! Введите целые числа.\n")

# Находим сумму элементов от K до L
total = 0

for i in range(k - 1, l):
    total += my_array[i]

# Вычисляем среднее арифметическое
average = total / (l - k + 1)

# Выводим результат
print(f"Среднее арифметическое: {average}")
