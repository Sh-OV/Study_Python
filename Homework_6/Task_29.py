# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

from random import Random
import random

num = int(input('Задайте количество элементов в списке (введите натуральное число): '))

list_1 = [i for i in range(num)]
creation_random_list = list(map(lambda x: random.randint(0, 5), list_1))

non_repeating_elements = list(filter(lambda x: creation_random_list.count(x) == 1, creation_random_list))
print(f'{creation_random_list} => {non_repeating_elements}')
