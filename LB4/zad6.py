def reverse_words(s):
    # Убираем лишние пробелы по краям, чтобы не было пустых слов
    s = s.strip()
    
    # Базовый случай: если в строке нет пробелов, значит, это одно слово
    if " " not in s:
        return s
    
    # Находим индекс первого пробела
    space_index = s.find(" ")
    
    # Отрезаем первое слово (от начала до пробела)
    first_word = s[:space_index]
    
    # Запоминаем всё остальное (от пробела до конца), убирая лишний пробел
    rest_of_string = s[space_index+1:]
    
    # Рекурсивный шаг: переворачиваем остаток и приклеиваем первое слово в конец
    return reverse_words(rest_of_string) + " " + first_word

# --- Проверка ---
text = input("Введите строку: ")
result = reverse_words(text)
print(f"Результат: {result}")