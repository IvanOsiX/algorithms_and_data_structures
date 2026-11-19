
# Вводим размер массива
while True:
    try:
        n = int(input("Введите размер массива N: "))
        if n > 1:
            break
        print("Ошибка! N должно быть больше 1.\n")
    except ValueError:
        print("Ошибка! Введите целое число.\n")

# Вводим элементы массива
my_array = []

for i in range(n):
    element = int(input(f"Введите элемент A[{i + 1}]: "))
    my_array.append(element)

# Находим разность между первыми двумя элементами
difference = my_array[1] - my_array[0]

# Проверяем, является ли массив арифметической прогрессией
for i in range(1, n - 1):
    if my_array[i + 1] - my_array[i] != difference:
        difference = 0
        break

# Выводим результат
print(f"Результат: {difference}")
