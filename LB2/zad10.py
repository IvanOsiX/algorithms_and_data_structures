while True:
    year = int(input("Введите год: "))
    # Проверка, по задаче цикл начинается с 1984 года
    if year < 1984:
        print("1984 год - начало цикла, введите год от 1984\n")
        continue
    break

# Находим смещение от начала цикла (1984 год)
offset = (year - 1984) % 60

# Вычисляем индексы для цвета и животного
color_idx = offset // 12  # 0-4 (5 цветов)
animal_idx = offset % 12  # 0-11 (12 животных)

# Определяем цвет
if color_idx == 0: color = "зеленой"
elif color_idx == 1: color = "красной"
elif color_idx == 2: color = "желтой"
elif color_idx == 3: color = "белой"
else: color = "черной"

# Определяем животное
if animal_idx == 0: animal = "крысы"
elif animal_idx == 1: animal = "коровы"
elif animal_idx == 2: animal = "тигра"
elif animal_idx == 3: animal = "зайца"
elif animal_idx == 4: animal = "дракона"
elif animal_idx == 5: animal = "змеи"
elif animal_idx == 6: animal = "лошади"
elif animal_idx == 7: animal = "овцы"
elif animal_idx == 8: animal = "обезьяны"
elif animal_idx == 9: animal = "курицы"
elif animal_idx == 10: animal = "собаки"
else: animal = "свиньи"

print(f"{year} — год {color} {animal}")