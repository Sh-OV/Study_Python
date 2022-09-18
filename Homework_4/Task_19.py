# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

num = int(input('Введите натуральное число: '))

def Function_list_filling (count):      # Функция создания последовательности (для нахождения многочлена)
    my_list = []
    while count >= 1:
        my_list.append(count)
        count -= 1
    return my_list

def Function_polynomial (my_list, numb):    # Функция вывода многочлена
    x = 0
    print(f'k = {numb} =>', end = ' ')
    for i in my_list[:len(my_list)-1]:
        x = x ** numb
        arg = random.randint(0, 100)
        st1 = f'{arg} * x^{numb}'
        if arg != 0:
            print( st1, end = ' + ')
            numb -= 1
        else:
            numb -= 1
    arg = random.randint(0, 100)
    st2 = f'{arg} * x'
    if arg != 0:
        print( st2, end = ' + ')
    arg = random.randint(0, 100)
    if arg != 0:
        st3 = f'{arg} = 0'
    print( st3)
    
list_filling = Function_list_filling (num)
Function_polynomial (list_filling, num)

