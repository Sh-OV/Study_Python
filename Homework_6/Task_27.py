# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

import random
from functools import reduce

num = int(input('Задайте количество элементов в списке (введите натуральное число): '))

list_1 = [i for i in range(num)]
creation_random_list = list(map(lambda x: random.randint(0, 100), list_1))
print(creation_random_list)

odd_positions = [i for i in creation_random_list if i % 2 > 0]
print(odd_positions)

odd_positions = list(map(lambda x: int(x), odd_positions))
sum_odd_positions = sum(odd_positions)
print(f'Сумма нечетных позиций = {sum_odd_positions}')
