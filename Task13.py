quantity_days = int(input("Введите кол-во дней: "))
count_days = 0
max_ottepel = 0
last_day = -1
for i in range(1, quantity_days + 1):
    current_day = int(input(f"Введите температуру {i} дня "))
    if current_day > 0:
        if last_day <= 0:
            count_days = 0
        count_days += 1
        if count_days > max_ottepel:
            max_ottepel = count_days
    last_day = current_day
print(max_ottepel)