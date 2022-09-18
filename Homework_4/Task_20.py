# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random

num1 = int(input('Введите натуральное число для создания первого многочлена: '))
num2 = int(input('Введите натуральное число для создания первого многочлена: '))

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
    print(f'my_list_1 = {my_list_1}')
    print(f'my_list_2 = {my_list_2}')
    sum_polyn = []
    
    n = 1
    j = 1
    k = 1
    print(f'len(my_list_1) = {len(my_list_1)}')
    print(f'len(my_list_2) = {len(my_list_2)}')
    len_sum = len(my_list_1) + len(my_list_2)    
    for i in range(len_sum):
        sum_polyn.append(0)
    print(f'len_sum = {len_sum}')    
    
  
    while (j <= (len(my_list_1)-2) and k <= (len(my_list_2)-2) and n <= (len_sum)):
    # while (j <= len_sum and k <= len_sum and n <= len_sum):
        el1 = []
        el2 = []
        # for i in range(5):
        #     el1.append(0)
        #     el2.append(0)
        el1 = my_list_1[j]
        el1 = el1.split('^')
        el2 = my_list_2[k]
        el2 = el2.split('^')
        # print(f'el1 = {el1}')
        # print(f'el1[0] = {el1[0]}')
        # print(f'el1[1] = {el1[1]}')
        # print(f'el2 = {el2}')
        # print(f'el2[0] = {el2[0]}')
        # print(f'el2[1] = {el2[1]}')
        
        if(len(el1) >= 2 and len(el2) >= 2):
            if int(el1[1]) > int(el2[1]):
                # print(f'n =  {n}, j =  {j}')
                sum_polyn[n] = my_list_1[j]
                # print(f'sum_polyn[n] =  {sum_polyn[n]}')
                sum_polyn[n-1] = my_list_1[j-1]
                # print(f'sum_polyn[n-1] = {sum_polyn[n-1]}')
                j += 2
                n += 2
                continue
            elif int(el1[1]) == int(el2[1]):
                # print(f'n =  {n}, j =  {j}, k = {k}')
                sum_polyn[n] = my_list_1[j]
                # print(f'sum_polyn[n] =  {sum_polyn[n]}')
                sum_polyn[n-1] = int(my_list_1[j-1]) + int(my_list_2[k-1])
                # print(f'sum_polyn[n-1] = {sum_polyn[(n-1)]}')
                j += 2
                k += 2
                n += 2
                continue
            elif int(el1[1]) < int(el2[1]):
                # print(f'n =  {n}, k =  {k}')
                sum_polyn[n] = my_list_2[k]
                # print(f'sum_polyn[n] =  {sum_polyn[n]}')
                sum_polyn[n-1] = my_list_2[k-1]
                # print(f'sum_polyn[n-1] = {sum_polyn[(n-1)]}')
                k += 2
                n += 2
                continue  
            
        elif(len(el1) >= 1 and len(el2) < 2):
            # print(f'n =  {n}, j =  {j}')
            sum_polyn[n] = my_list_1[j]
            # print(f'sum_polyn[n] =  {sum_polyn[n]}')
            sum_polyn[n-1] = my_list_1[j-1]
            # print(f'sum_polyn[n-1] = {sum_polyn[n-1]}')
            j += 2
            n += 2
            continue
            
        elif(len(el2) >= 1 and len(el1) < 2):
            # print(f'n =  {n}, k =  {k}')
            sum_polyn[n] = my_list_2[k]
            # print(f'sum_polyn[n] =  {sum_polyn[n]}')
            sum_polyn[n-1] = my_list_2[k-1]
            # print(f'sum_polyn[n-1] = {sum_polyn[(n-1)]}')
            k += 2
            n += 2
            continue  
        
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
    print(sum_polyn)
    return sum_polyn






# def Function_sum_polynomial (my_list_1, my_list_2):
#     if len(my_list_1) >= len(my_list_2):
#         for i in range(len(my_list_1)):
#             if i % 2 != 0:
#                 for j in range(len(my_list_2)):
#                     if my_list_1[i] == my_list_2[j]:
#                         my_list_1[i-1] = int(my_list_1[i-1]) + int(my_list_2[j-1])
#     if my_list_1[len(my_list_1) - 2] == my_list_2[len(my_list_2)-2]:
#         my_list_1[len(my_list_1)-1] = int(my_list_1[len(my_list_1)-1]) + int(my_list_2[len(my_list_2)-1])
    
#     print(my_list_1)

list_filling_1 = Function_list_filling (num1)
list_filling_2 = Function_list_filling (num2)

polynomial_1 = Function_polynomial (list_filling_1, num1)
polynomial_2 = Function_polynomial (list_filling_2, num2)

converting_text_elements_1 = Function_converting_text_elements (polynomial_1)
converting_text_elements_2 = Function_converting_text_elements (polynomial_2)

Function_sum_polynomial (converting_text_elements_1, converting_text_elements_2)



