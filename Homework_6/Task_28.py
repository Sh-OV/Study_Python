# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

num = int(input('Введите количество элементов списка: '))
list_creation = [i for i in range(0, num + 1)]

def Function_multiplication_positions (rand_list):
    my_list = []
    i = 0
    if len(rand_list) % 2 == 0:
        len_list = len(rand_list) // 2
    else:
        len_list = len(rand_list) // 2 + 1
       
    while i < len_list:
        mult = rand_list[i] * rand_list[((len(rand_list)-1)-(1*i))]
        my_list.append(mult)
        i += 1
    return my_list

multiplic_positions = Function_multiplication_positions (list_creation)

print(list_creation, end = " => ")
print(multiplic_positions)