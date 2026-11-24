from collections import deque

# Создаем пустую очередь
queue = deque()

# Выводим меню ОДИН РАЗ перед началом цикла
print("--- Работа с очередью ---")
print("1. Добавить элемент в конец")
print("2. Извлечь элемент из начала")
print("3. Проверить, пуста ли очередь")
print("4. Узнать размер очереди")
print("5. Проверить наличие элемента")
print("6. Очистить очередь")
print("7. Вывести все элементы")
print("0. Выйти")
print("-------------------------")

while True:
    # Внутри цикла просим только ввести команду
    try:
        choice = int(input("Команда: "))
    except ValueError:
        print("Ошибка! Введите число от 0 до 7.")
        continue

    if choice == 1:
        try:
            item = int(input("Введите число для добавления: "))
            queue.append(item)
            print(f"Элемент {item} встал в конец очереди.")
        except ValueError:
            print("Ошибка! Вводите только целые числа.")
            
    elif choice == 2:
        if len(queue) > 0:
            extracted_item = queue.popleft()
            print(f"Из начала очереди извлечен элемент: {extracted_item}")
        else:
            print("Очередь пуста, извлекать нечего!")
            
    elif choice == 3:
        if len(queue) == 0:
            print("Очередь пуста.")
        else:
            print("Очередь не пуста.")
            
    elif choice == 4:
        print(f"В очереди {len(queue)} элементов.")
        
    elif choice == 5:
        try:
            search_item = int(input("Какое число ищем? "))
            if search_item in queue:
                print(f"Элемент {search_item} есть в очереди.")
            else:
                print(f"Элемента {search_item} в очереди нет.")
        except ValueError:
            print("Ошибка! Вводите только целые числа.")
            
    elif choice == 6:
        queue.clear()
        print("Очередь полностью очищена.")
        
    elif choice == 7:
        if len(queue) > 0:
            print("Текущая очередь (от начала к концу):")
            for element in queue:
                print(element, end=" ")
            print() 
        else:
            print("Очередь пуста, выводить нечего.")
            
    elif choice == 0:
        print("Завершение работы программы.")
        break
        
    else:
        print("Такого пункта нет. Выберите от 0 до 7.")