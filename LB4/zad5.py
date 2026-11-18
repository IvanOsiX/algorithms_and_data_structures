def binary_search(arr, target, left=0, right=None):
    # При первом вызове right=None, поэтому ставим его на конец массива
    if right is None:
        right = len(arr) - 1

    # Базовый случай 1: элемент не найден (границы пересеклись)
    if left > right:
        return -1  # Возвращаем -1, что означает "не найдено"

    # Находим середину (целочисленное деление)
    mid = (left + right) // 2

    # Базовый случай 2: элемент найден
    if arr[mid] == target:
        return mid  # Возвращаем индекс найденного элемента

    # Рекурсивный шаг: ищем в нужной половине
    elif arr[mid] < target:
        # Если середина меньше искомого, ищем в правой части
        return binary_search(arr, target, mid + 1, right)
    else:
        # Если середина больше искомого, ищем в левой части
        return binary_search(arr, target, left, mid - 1)

# --- Проверка работы ---
# Создаем ОТСОРТИРОВАННЫЙ массив (это обязательно!)
my_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = int(input("Введите число для поиска: "))

result = binary_search(my_array, target)

if result != -1:
    print(f"Элемент {target} найден на индексе {result}.")
else:
    print(f"Элемент {target} не найден в массиве.")