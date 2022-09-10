# Реализуйте алгоритм перемешивания списка.

from random import Random
import random


number = int(input('Введите количество элементов списка: '))

# Функция создания последовательности по введенному числу пользователя
def Function_list_creation(num):
    my_list = []
    dig = 0
    while dig <= num:
        my_list.append(dig)
        dig += 1
    return my_list
        
list_creation = Function_list_creation(number)
print(list_creation)   

# Функция создания пользовательского перемешивания списка
def function_list_shuffle_custom (c_list):
    m_list = []
    r = 3
    for i in range(len(c_list)):
        arg = c_list[i - r]
        m_list.append(arg)
    return m_list

list_shuffle_custom = function_list_shuffle_custom (list_creation)
print(list_shuffle_custom)

# Функция перемешивания списка - используем возможности Python
def function_list_shuffle (m_list):
    random.shuffle(m_list)
    return m_list
    
list_shuffle = function_list_shuffle (list_creation)
print(list_shuffle)


        

