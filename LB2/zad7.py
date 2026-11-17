while True:
    month = int(input("Введите номер месяца (1-12): "))
    
    # Проверяем месяц
    if month < 1 or month > 12:
        print("Ошибка! Месяц должен быть от 1 до 12. Введите снова.\n")
        continue
    
    # Считаем лимит дней
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        max_days = 28  # Февраль в високосный год
        
    # Проверка на правильность ввода дня
    while True:
        day = int(input("Введите номер дня: "))

        # Проверяем день
        if day < 1 or day > max_days:
            print(f"Ошибка! В этом месяце всего {max_days} дней. Введите день от 1 до {max_days}.\n")
            continue
        
        break
    break

# Если проверки пройдены, делаем перевод в текст
if day == 1: day_str = "первое"
elif day == 2: day_str = "второе"
elif day == 3: day_str = "третье"
elif day == 4: day_str = "четвертое"
elif day == 5: day_str = "пятое"
elif day == 6: day_str = "шестое"
elif day == 7: day_str = "седьмое"
elif day == 8: day_str = "восьмое"
elif day == 9: day_str = "девятое"
elif day == 10: day_str = "десятое"
elif day == 11: day_str = "одиннадцатое"
elif day == 12: day_str = "двенадцатое"
elif day == 13: day_str = "тринадцатое"
elif day == 14: day_str = "четырнадцатое"
elif day == 15: day_str = "пятнадцатое"
elif day == 16: day_str = "шестнадцатое"
elif day == 17: day_str = "семнадцатое"
elif day == 18: day_str = "восемнадцатое"
elif day == 19: day_str = "девятнадцатое"
elif day == 20: day_str = "двадцатое"
elif day == 21: day_str = "двадцать первое"
elif day == 22: day_str = "двадцать второе"
elif day == 23: day_str = "двадцать третье"
elif day == 24: day_str = "двадцать четвертое"
elif day == 25: day_str = "двадцать пятое"
elif day == 26: day_str = "двадцать шестое"
elif day == 27: day_str = "двадцать седьмое"
elif day == 28: day_str = "двадцать восьмое"
elif day == 29: day_str = "двадцать девятое"
elif day == 30: day_str = "тридцатое"
elif day == 31: day_str = "тридцать первое"

# Определяем месяц
if month == 1: month_str = "января"
elif month == 2: month_str = "февраля"
elif month == 3: month_str = "марта"
elif month == 4: month_str = "апреля"
elif month == 5: month_str = "мая"
elif month == 6: month_str = "июня"
elif month == 7: month_str = "июля"
elif month == 8: month_str = "августа"
elif month == 9: month_str = "сентября"
elif month == 10: month_str = "октября"
elif month == 11: month_str = "ноября"
elif month == 12: month_str = "декабря"

print(f"\nВаша дата: {day_str} {month_str}")