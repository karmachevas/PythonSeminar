# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

lst = [4, 5, 2, 2, 2, 4, 5, 3, 4]
max_elem = max(lst)
min_elem = min(lst)
for i in range(len(lst)):
    if lst[i] == max_elem:
        lst.pop(i)
        lst.insert(i, min_elem)
print(lst)