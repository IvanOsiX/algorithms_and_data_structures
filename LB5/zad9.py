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

# Переменная для хранения номера последнего локального максимума
last_max = 0

# Проверяем элементы массива
for i in range(n):
    if i == 0:
        if my_array[i] > my_array[i + 1]:
            last_max = i + 1

    elif i == n - 1:
        if my_array[i] > my_array[i - 1]:
            last_max = i + 1

    else:
        if my_array[i] > my_array[i - 1] and my_array[i] > my_array[i + 1]:
            last_max = i + 1

# Выводим результат
print(f"Номер последнего локального максимума: {last_max}")
