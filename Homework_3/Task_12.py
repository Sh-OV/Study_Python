# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

num = int(input('Задайте количество элементов в списке (введите натуральное число): '))

def Function_creation_random_list (number):       # Функция создания списка рандомно 
    my_list = []
    for i in range(number):
        arg = random.randint(0, 10)
        my_list.append(arg)
    return my_list

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

creation_random_list = Function_creation_random_list (num)
multiplic_positions = Function_multiplication_positions (creation_random_list)

print(creation_random_list, end = " => ")
print(multiplic_positions)