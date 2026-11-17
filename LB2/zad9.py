while True:
    num = int(input("Введите число от 100 до 999: "))
    if 100 <= num <= 999:
        break
    print("Ошибка! Число должно быть трехзначным. Попробуйте снова.\n")

# Вытаскиваем сотни, остаток и единицы
hundreds = num // 100      # Целочисленное деление на 100
remainder = num % 100      # Остаток от деления на 100

# Переводим сотни в текст
if hundreds == 1: h_str = "сто"
elif hundreds == 2: h_str = "двести"
elif hundreds == 3: h_str = "триста"
elif hundreds == 4: h_str = "четыреста"
elif hundreds == 5: h_str = "пятьсот"
elif hundreds == 6: h_str = "шестьсот"
elif hundreds == 7: h_str = "семьсот"
elif hundreds == 8: h_str = "восемьсот"
else: h_str = "девятьсот"

# Теперь разбираемся с остатком (десятки и единицы)
t_str = ""
u_str = ""

if remainder == 0:
    pass  # Если остаток 0, то десятков и единиц нет (например, ровно 200)
    
elif remainder < 10:
    # Только единицы (например, 204)
    if remainder == 1: u_str = "один"
    elif remainder == 2: u_str = "два"
    elif remainder == 3: u_str = "три"
    elif remainder == 4: u_str = "четыре"
    elif remainder == 5: u_str = "пять"
    elif remainder == 6: u_str = "шесть"
    elif remainder == 7: u_str = "семь"
    elif remainder == 8: u_str = "восемь"
    elif remainder == 9: u_str = "девять"

elif remainder < 20:
    # Числа от 10 до 19 (исключения)
    if remainder == 10: t_str = "десять"
    elif remainder == 11: t_str = "одиннадцать"
    elif remainder == 12: t_str = "двенадцать"
    elif remainder == 13: t_str = "тринадцать"
    elif remainder == 14: t_str = "четырнадцать"
    elif remainder == 15: t_str = "пятнадцать"
    elif remainder == 16: t_str = "шестнадцать"
    elif remainder == 17: t_str = "семнадцать"
    elif remainder == 18: t_str = "восемнадцать"
    elif remainder == 19: t_str = "девятнадцать"
        
else:
    # Числа от 20 до 99
    tens = remainder // 10  # Десятки
    units = remainder % 10  # Единицы
    
    if tens == 2: t_str = "двадцать"
    elif tens == 3: t_str = "тридцать"
    elif tens == 4: t_str = "сорок"
    elif tens == 5: t_str = "пятьдесят"
    elif tens == 6: t_str = "шестьдесят"
    elif tens == 7: t_str = "семьдесят"
    elif tens == 8: t_str = "восемьдесят"
    elif tens == 9: t_str = "девяносто"
    
    # Единицы для чисел от 20 и выше
    if units == 1: u_str = "один"
    elif units == 2: u_str = "два"
    elif units == 3: u_str = "три"
    elif units == 4: u_str = "четыре"
    elif units == 5: u_str = "пять"
    elif units == 6: u_str = "шесть"
    elif units == 7: u_str = "семь"
    elif units == 8: u_str = "восемь"
    elif units == 9: u_str = "девять"

# Собираем строку, убирая лишние пробелы
result = f"{h_str} {t_str} {u_str}".replace("  ", " ").strip()
print(result)