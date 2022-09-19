# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

import random

num = int(input('Задайте количество элементов в списке (введите натуральное число): '))

def Function_creation_random_list (number):       # Функция создания списка рандомно 
    my_list = []
    for i in range(number):
        arg = random.randint(0, 100)
        my_list.append(arg)
    return my_list

def Function_sum_positions (m_list):
    sum = 0
    for i in range(len(m_list)):
        if i % 2 > 0:
            sum += m_list[i]
    return sum


creation_random_list = Function_creation_random_list (num)
sum_positions = Function_sum_positions (creation_random_list)

print(creation_random_list)
print(f'Сумма нечетных позиций = {sum_positions}')
