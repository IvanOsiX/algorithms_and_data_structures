# 1. Ввод массива с защитой
print("Введите элементы массива через пробел (только целые числа):")
while True:
    try:
        arr = list(map(int, input().split()))
        if len(arr) == 0:
            print("Ошибка! Вы ничего не ввели. Попробуйте снова.")
            continue
        break
    except ValueError:
        print("Ошибка! Вводите только целые числа через пробел. Попробуйте снова.")

# Бинарный поиск работает только с отсортированными массивами
arr.sort()
print(f"\nОтсортированный массив для поиска: {arr}")

# Ввод искомого значения с защитой
while True:
    try:
        target = int(input("Введите число, которое хотите найти: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")

# 2. Сам алгоритм бинарного поиска
print(f"\nПоиск числа {target}")

left = 0
right = len(arr) - 1
found_index = -1

while left <= right:
    mid = (left + right) // 2
    
    # Вывод текущей области поиска
    # Срез arr[left:right+1] берет элементы от left до right включительно
    current_subarray = arr[left:right+1]
    
    print(f"  Область поиска: {current_subarray}")
    print(f"  Границы: left={left}, right={right}")
    print(f"  Середина: индекс {mid}, значение {arr[mid]}")
    
    if arr[mid] == target:
        found_index = mid
        print(f"Найдено. {target} == {arr[mid]}")
        break
    elif arr[mid] > target:
        print(f"{arr[mid]} > {target}. Искомое число левее. Отбрасываем правую половину.\n")
        right = mid - 1
    else:
        print(f"{arr[mid]} < {target}. Искомое число правее. Отбрасываем левую половину.\n")
        left = mid + 1

# 3. Вывод результата
if found_index != -1:
    print(f"\nЧисло {target} найдено на индексе {found_index}.")
else:
    print(f"\nЧисло {target} не найдено в массиве.")