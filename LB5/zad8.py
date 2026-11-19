
# Вводим размер массива
while True:
    try:
        n = int(input("Введите размер массива N: "))
        if n >= 2:
            break
        print("Ошибка! N должно быть не меньше 2.\n")
    except ValueError:
        print("Ошибка! Введите целое число.\n")

# Вводим элементы массива
my_array = []

for i in range(n):
    element = int(input(f"Введите элемент A[{i + 1}]: "))
    my_array.append(element)

# Находим минимальный элемент среди элементов с четными номерами
minimum = my_array[1]

for i in range(3, n, 2):
    if my_array[i] < minimum:  # noqa: PLR1730
        minimum = my_array[i]

# Выводим результат
print(f"Минимальный элемент: {minimum}")
