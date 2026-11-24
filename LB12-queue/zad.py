from collections import deque

# Создаем пустую очередь
queue = deque()

while True:
    print("\n--- Работа с очередью ---")
    print("1. Добавить элемент в конец")
    print("2. Извлечь элемент из начала")
    print("3. Проверить, пуста ли очередь")
    print("4. Узнать размер очереди")
    print("5. Проверить наличие элемента")
    print("6. Очистить очередь")
    print("7. Вывести все элементы")
    print("0. Выйти\n")
    
    try:
        choice = int(input("Выберите действие: "))
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
        # Проверяем, есть ли что извлекать
        if len(queue) > 0:
            extracted_item = queue.popleft()
            print(f"Из начала очереди извлечен элемент: {extracted_item}")
        else:
            print("Очередь пуста, извлекать нечего!")
            
    elif choice == 3:
        # Проверка пустоты
        if len(queue) == 0:
            print("Очередь пуста.")
        else:
            print("Очередь не пуста.")
            
    elif choice == 4:
        # Получение размера
        print(f"В очереди {len(queue)} элементов.")
        
    elif choice == 5:
        try:
            search_item = int(input("Какое число ищем? "))
            # Проверка наличия элемента в очереди
            if search_item in queue:
                print(f"Элемент {search_item} есть в очереди.")
            else:
                print(f"Элемента {search_item} нет в очереди.")
        except ValueError:
            print("Ошибка! Вводите только целые числа.")
            
    elif choice == 6:
        # Очистка очереди
        queue.clear()
        print("Очередь полностью очищена.")
        
    elif choice == 7:
        # Перебор элементов
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