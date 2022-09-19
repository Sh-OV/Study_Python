# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19
import random

num = int(input('Задайте количество элементов в списке (введите натуральное число): '))

def Function_creation_random_list_float (number):       # Функция создания списка вещественных чисел рандомно 
    my_list = []
    for i in range(number):
        arg = round(random.randint(0, 10) + random.random(),2)
        my_list.append(arg)
    return my_list

def Function_difference_min_max_float (my_list):        # Функция нахождения разницы между min и max
    fl_list = []
    diff = 0
    min = 100
    max = 0
    help = 0
    for i in range(len(my_list)):
        help = round(my_list[i] * 100 % 100,0)
        if min > help:
            min = help
        if max < help:
            max = help
    diff = (max - min) / 100
    return diff
        
        
creation_random_list_float = Function_creation_random_list_float (num)
diff_min_max_float = Function_difference_min_max_float (creation_random_list_float)
print(creation_random_list_float, end = ' => ')
print(diff_min_max_float)