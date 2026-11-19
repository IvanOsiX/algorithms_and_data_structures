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

# Выводим элементы в нужном порядке
print("Элементы массива в нужном порядке:")

left = 0
right = n - 1

while left <= right:
    print(my_array[left], end=" ")

    # Если элементы еще не встретились, выводим элемент с конца
    if left != right:
        print(my_array[right], end=" ")

    left += 1
    right -= 1