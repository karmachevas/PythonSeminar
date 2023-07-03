# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

quantity_elem = int(input("Введите кол-во элементов: "))
a = []
for i in range(0, quantity_elem):
    a.append(int(input("Введите элемент: ")))
k = int(input("Введите число К: "))
for i in range(k):
    last = a.pop()
    a.insert(0, last)
print(a)