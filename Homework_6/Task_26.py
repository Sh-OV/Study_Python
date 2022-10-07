# Реализуйте алгоритм перемешивания списка.

from random import Random
import random

number = int(input('Введите количество элементов списка: '))
list_creation = [i for i in range(0, number + 1)]
print(list_creation)   
random.shuffle(list_creation)
print(list_creation)


