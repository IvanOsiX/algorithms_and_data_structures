
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

# Ищем два одинаковых элемента
found = False

for i in range(n):
    for j in range(i + 1, n):
        if my_array[i] == my_array[j]:
            print(f"Номера одинаковых элементов: {i + 1} и {j + 1}")
            found = True
            break

    if found:
        break
