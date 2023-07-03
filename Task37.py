def rekurs(n):
    if n == 0:
        return False #Остановка рекурсии
    else:
        element = int(input()) # Ввод числа
        rekurs(n - 1)          # Вызов рекурсии для следующего числа
        print(element)         # Вывод числа
rekurs(5)