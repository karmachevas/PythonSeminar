# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

quantity_elem = int(input("Введите кол-во элементов: "))
a = []
new = []
for i in range(0, quantity_elem):
    a.append(int(input("Введите элемент: ")))
for elem in a:
    if elem not in new:
        new.append(elem)
print(len(new))
