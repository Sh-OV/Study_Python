# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random

num1 = int(input('Введите натуральное число для создания первого многочлена: '))
num2 = int(input('Введите натуральное число для создания второго многочлена: '))

def Function_list_filling (count):      # Функция создания последовательности (для нахождения многочлена)
    my_list = []
    while count >= 1:
        my_list.append(count)
        count -= 1
    return my_list

def Function_polynomial (my_list, numb):    # Функция создания массива многочлена
    x = 0
    polyn_list = []
    for i in my_list[:len(my_list)-1]:
        x = x ** numb
        arg = random.randint(0, 20)
        st1 = f'{arg} * x^{numb} +'
        if arg != 0:
            polyn_list.append(st1)
            numb -= 1
        else:
            numb -= 1
    arg = random.randint(0, 20)
    st2 = f'{arg} * x +'
    if arg != 0:
        polyn_list.append(st2)
    arg = random.randint(0, 100)
    if arg != 0:
        st3 = f'{arg} = 0'
        polyn_list.append(st3)
    return " ".join (polyn_list)
    
def Function_converting_text_elements (my_list):    # Функция преобразования формулы многочлена в список элементов
    convert_list = []
    my_list = my_list.split(' = ')
    polyn_list = my_list[0].split(' + ')
    for i in range(len(polyn_list)):
        elem = polyn_list[i].split(' * ')
        for j in range(len(elem)):
            el = elem[j].split(' , ')
            convert_list.append(el)
    my_list = []
    for k in range(len(convert_list)):
        my_list += convert_list[k]
    return my_list

def Function_sum_polynomial (my_list_1, my_list_2):     # Функция сложения многочленов
    sum_polyn = []
    n = 1
    j = 1
    k = 1
    len_sum = len(my_list_1) + len(my_list_2)    
    for i in range(len_sum):
        sum_polyn.append(0) 

    while (j <= (len(my_list_1)-2) and k <= (len(my_list_2)-2) and n <= (len_sum)):
        el1 = []
        el2 = []
        el1 = my_list_1[j]
        el1 = el1.split('^')
        el2 = my_list_2[k]
        el2 = el2.split('^')
    
        if(len(el1) >= 2 and len(el2) >= 2):
            if int(el1[1]) > int(el2[1]):
                sum_polyn[n] = my_list_1[j]
                sum_polyn[n-1] = my_list_1[j-1]
                j += 2
                n += 2
                
            elif int(el1[1]) == int(el2[1]):
                sum_polyn[n] = my_list_1[j]
                sum_polyn[n-1] = int(my_list_1[j-1]) + int(my_list_2[k-1])
                j += 2
                k += 2
                n += 2
               
            elif int(el1[1]) < int(el2[1]):
                sum_polyn[n] = my_list_2[k]
                sum_polyn[n-1] = my_list_2[k-1]
                k += 2
                n += 2
                
        elif(len(el1) >= 2 and len(el2) < 2):
            sum_polyn[n] = my_list_1[j]
            sum_polyn[n-1] = my_list_1[j-1]
            j += 2
            n += 2
           
        elif(len(el2) >= 2 and len(el1) < 2):
            sum_polyn[n] = my_list_2[k]
            sum_polyn[n-1] = my_list_2[k-1]
            k += 2
            n += 2

        else:
            j += 1
            k += 1
            n += 1
            
    if my_list_1[len(my_list_1) - 2] == my_list_2[len(my_list_2)-2]:
        sum_polyn[-1] = int(my_list_1[-1]) + int(my_list_2[-1])
        sum_polyn[-2] = (my_list_1[-2])
        sum_polyn[-3] = int(my_list_1[-3]) + int(my_list_2[-3])
    else:
        if my_list_1[len(my_list_1) - 2] == "x":
            sum_polyn[-1] = int(my_list_1[-1]) + int(my_list_2[-1])
            sum_polyn[-2] = (my_list_1[-2])
            sum_polyn[-3] = int(my_list_1[-3])
        elif my_list_2[len(my_list_2) - 2] == "x":
            sum_polyn[-1] = int(my_list_1[-1]) + int(my_list_2[-1])
            sum_polyn[-2] = (my_list_2[-2])
            sum_polyn[-3] = int(my_list_2[-3])
    return sum_polyn

def Function_readability_polynomial (my_list):
    my_polyn = ""
    count = 0
    n = 2
    k = 1
    for i in range(len(my_list)):
        if my_list[i] == 0:
            count += 1
    
    while count > 0:
        my_list.remove(0)
        count -= 1
    
    while n < len(my_list):
        my_list.insert(n, '+')
        n += 3
    
    while k < len(my_list):
        my_list.insert(k, '*')
        k += 4
        
    my_list.insert(len(my_list), '= 0')
    my_list = [str(i) for i in my_list]
    
    return ' '.join (my_list)
    

list_filling_1 = Function_list_filling (num1)
list_filling_2 = Function_list_filling (num2)

polynomial_1 = Function_polynomial (list_filling_1, num1)
polynomial_2 = Function_polynomial (list_filling_2, num2)

converting_text_elements_1 = Function_converting_text_elements (polynomial_1)
converting_text_elements_2 = Function_converting_text_elements (polynomial_2)

sum_polynomial = Function_sum_polynomial (converting_text_elements_1, converting_text_elements_2)
readability_polynomial = Function_readability_polynomial (sum_polynomial)

print(f'Формула первого многочлена -> {polynomial_1}')
print(f'Формула второго многочлена -> {polynomial_2}')
print(f'Формула суммы многочленов -> {readability_polynomial}')


