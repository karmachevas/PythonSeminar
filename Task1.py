# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент. 
# В исходном списке минимум 2 элемента.

my_list = [1, 2, 3, 4, 5]
first_elem = my_list.pop(0)
my_list.insert(0,my_list.pop())
my_list.append(first_elem)
print(my_list)