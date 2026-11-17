while True:
    num = int(input("Введите количество заданий (от 10 до 40): "))
    
    # Проверка на попадание в диапазон
    if 10 <= num <= 40:
        break
    print("Ошибка! Число заданий должно быть от 10 до 40. Попробуйте снова.\n")

# 1. Определяем текст для числа
# Сначала обрабатываем числа от 10 до 19
if num == 10: num_str = "десять"
elif num == 11: num_str = "одиннадцать"
elif num == 12: num_str = "двенадцать"
elif num == 13: num_str = "тринадцать"
elif num == 14: num_str = "четырнадцать"
elif num == 15: num_str = "пятнадцать"
elif num == 16: num_str = "шестнадцать"
elif num == 17: num_str = "семнадцать"
elif num == 18: num_str = "восемнадцать"
elif num == 19: num_str = "девятнадцать"

else:
    # Для чисел от 20 до 40 определяем десятки
    if num < 30: tens_str = "двадцать"
    elif num < 40: tens_str = "тридцать"
    else: tens_str = "сорок"
    
    # Определяем единицы (если число не оканчивается на 0)
    last_digit = num % 10
    if last_digit == 0: units_str = ""
    elif last_digit == 1: units_str = "одно"
    elif last_digit == 2: units_str = "два"
    elif last_digit == 3: units_str = "три"
    elif last_digit == 4: units_str = "четыре"
    elif last_digit == 5: units_str = "пять"
    elif last_digit == 6: units_str = "шесть"
    elif last_digit == 7: units_str = "семь"
    elif last_digit == 8: units_str = "восемь"
    elif last_digit == 9: units_str = "девять"
    
    # Склеиваем десятки и единицы
    if units_str == "":
        num_str = tens_str
    else:
        num_str = f"{tens_str} {units_str}"

# 2. Применяем правило согласования (Падежи)
last_digit = num % 10
last_two_digits = num % 100

# 21, 31 (и 1, но ее нет в диапазоне)
if last_digit == 1 and last_two_digits != 11:
    word_form = "учебное задание"
# 2, 3, 4, 22, 23, 24, 32, 33, 34
elif last_digit in [2, 3, 4] and last_two_digits not in [12, 13, 14]:
    word_form = "учебных задания"
# Все остальные (10-20, 25-30, 35-40)
else:
    word_form = "учебных заданий"

print(f"\n{num_str} {word_form}")