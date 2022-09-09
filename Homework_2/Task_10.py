# Реализуйте алгоритм перемешивания списка.

from random import Random
import random


number = int(input('Введите количество элементов списка: '))

def Function_list_creation(num):
    my_list = []
    dig = 0
    while dig <= num:
        my_list.append(dig)
        dig += 1
    return my_list
        
list_creation = Function_list_creation(number)
print(list_creation)    

def function_list_shuffle (m_list):
    random.shuffle(m_list)
    return m_list
    
list_shuffle = function_list_shuffle (list_creation)
print(list_shuffle)