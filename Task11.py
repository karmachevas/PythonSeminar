# 1 1 2 3 5 8 13 21
number = int(input("Введите число: "))
first_number = 1
second_number = 1
number_fibonachi = 1
position_number = 2
if number == 1:
    print(1)
while number > number_fibonachi:
    number_fibonachi = first_number + second_number
    first_number = second_number
    second_number = number_fibonachi
    position_number += 1
    if number == number_fibonachi:
        print(position_number)
    elif number < number_fibonachi:
        print(-1)
