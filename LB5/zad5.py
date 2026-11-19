
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

# Сначала выводим элементы с нечетными номерами
print("Элементы в нужном порядке:")

for i in range(0, n, 2):
    print(my_array[i], end=" ")

# Затем выводим элементы с четными номерами в обратном порядке
for i in range(n - 1, 0, -1):
    if i % 2 != 0:
        print(my_array[i], end=" ")