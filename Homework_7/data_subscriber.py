# модуль, берущий данные из модуля registration и записывающий данные в файлы, из него мы можем запросить данные

import registration as reg
import csv
import pandas as pd

def record_data_file(name_1,  modif_1, e_line_1, name_2,  modif_2, e_line_2):     # запись данных в файлы csv, txt
    i_data = reg.input_data()
    for i in range(len(i_data)):
        k = i_data[i]
        with open(name_1, modif_1, encoding='utf-8') as file_1:
            file_1.write(k + ',') 
    with open(name_1, modif_1) as file_1:
            file_1.write(e_line_1)
            file_1.close()
    for j in range(len(i_data)):
        h = i_data[j]
        with open(name_2, modif_2, encoding='utf-8') as file_2:
            file_2.write(h + '\n\n') 
    with open(name_2, modif_2) as file_2:
            file_2.write(e_line_2)
            file_2.close()
    return

def record_data_file_csv(name,  modif, sep, e_line):     # запись данных в файлы csv
    i_data = reg.input_data()
    for i in range(len(i_data)):
        k = i_data[i]
        with open(name, modif, encoding='utf-8') as file:
            file.write(k + sep) 
    with open(name, modif) as file:
            file.write(e_line)
            file.close()
    return

def record_data_file_txt(name,  modif, sep, e_line):     # запись данных в файлы txt
    i_data = reg.input_data()
    for j in range(len(i_data)):
        h = i_data[j]
        with open(name, modif, encoding='utf-8') as file:
            file.write(h + sep) 
    with open(name, modif) as file:
            file.write(e_line)
            file.close()
    return

def search_data_csv(name, search):          # поиск данных в файле csv
    index = []
    l_num = 0
    data = open(name, 'r', encoding='utf-8')
    for line in data:
        line = line.split(',')
        for i in range(len(line)):
            if line[i] == search:
                temp = line
                index.append(l_num)
                index.append(temp)
                # index.append([l_num, temp])
        l_num += 1
    # print(f'index = {index}')            
    data.close()
    return index

def search_data_txt(name, search):              # поиск данных в файле txt
    index = []
    str_line = ''
    data = open(name, 'r', encoding='utf-8')
    for line in data:
        if line != '----------\n':
           str_line += line + ' | '
        else:
            str_line += line
            index.append(str_line)
            str_line = ''
    
    list_data = []
    for i in range(len(index)):
        user_list = []
        user_list = index[i].split(' | ')
        for k in range(len(user_list)):
            if user_list[k] == search:
                temp = user_list
                list_data.append(temp)           
    # print(f'list_data = {list_data}')
    data.close()
    return list_data

def replacing_data_elem_csv(name, search, replacement):            # замена конкретного элемента в файле csv
    data = pd.read_csv(name)
    print(data.head(20))
    data.replace(to_replace=search, value=replacement, inplace=True)
    print(data.head(20))
    data.to_csv(name, index=None)
    return

def removal_data_file_csv(name, search):            # удаление части данных в файле csv
    sear = search_data_csv(name, search)
    data = pd.read_csv(name)
    print(data.head(6))
    data.drop(labels=None, axis=0, index=sear[0]-1, inplace=True)
    print(data.head(6))
    data.to_csv(name, index=None)
    return




# record_data_file('Homework_7\Telephone_directory_csv', 'a', ",", '\n')
# record_data_file('Homework_7\Telephone_directory.txt', 'a', "\n\n", '----------\n')

# record_data_file('Homework_7\Telephone_directory_csv', 'a', ",", '\n', 'Homework_7\Telephone_directory.txt', 'a', "\n\n", '----------\n\n')

# search_data_csv('Homework_7\Telephone_directory_csv', 'массажист')

# search_data_txt('Homework_7\Telephone_directory.txt', 'Попов\n')

# replacing_data_file_csv('Homework_7\Telephone_directory_csv', 'Попов', 'a', ",", '\n')

# removal_data_file_csv('Homework_7\Telephone_directory_csv', 'Щёголева')

# replacing_data_elem_csv('Homework_7\Telephone_directory_csv', "Мама", "Мамулечка")









#  Функция считывет из файла информацию, записывает в список и в списке меняет данные

# def replacing_data_file_csv(name, search, modif, sep, e_line):            # замена части данных в файле csv
#     sear = search_data_csv(name, search)
#     data = open(name, 'r+', encoding='utf-8')
#     my_list = []
#     for line in data:
#         my_list.append(line)
#     k = 0
    
#     for i in range(len(my_list)):
#         if i == sear[k]:
#             print(my_list[i])
#             del my_list[i]
#             # my_list.insert(i, record_data_file_csv(name,  modif, sep, e_line))
#             my_list.insert(i, reg.input_data())
#             print(my_list[i])
#             if k < len(sear) - 2:
#                 k += 2
#         else:
#             print('НЕТ')
#     print(my_list)
#     data.close()      
#     return



# def replacing_data_file_csv(name, search, modif, sep, e_line):            # замена части данных в файле csv
#     sear = search_data_csv(name, search)
#     l_num = 0
#     k = 0
#     data = open(name, 'r+', encoding='utf-8')
#     for line in data:
#         if l_num == sear[k]:
#             line = reg.input_data()
#             data.writerows(line)
#             if k < len(sear) - 2:
#                 k += 2
#         l_num += 1
#     data.close()      
#     return    


# def removal_data_file_csv(name, search):            # удаление части данных в файле csv
#     sear = search_data_csv(name, search)
#     us = input('Выберите контакт, который надо удалить и напишите номер его строки: ')
#     data = pd.read_csv(name)
#     print(data.head(8))
#     l_num = 0
#     k = 0
#     # for line in data:
#     for i in range(len(data)):
#             if i == sear[us]:
#                 data.drop(labels=None, axis=0, index=sear[us]-1, inplace=True)
#             # if k < len(sear) - 2:
#             #     k += 2
#         # l_num += 1
    
#     print(data.head(8))
#     data.to_csv(name, index=None)
#     return


# def replacing_data_file_csv(name, search, replacement):            # замена строки в файле csv
#     # i_data = reg.input_data()
#     data = pd.read_csv(name)
#     print(data.head(20))
#     # data.str.replace(to_replace=search, value=reg.input_data(), inplace=True)
#     # data.str.replace(search, reg.input_data())
#     # data.apply(lambda x: x.replace(search, reg.input_data()), axis=1, broadcast=None)
#     data.apply(lambda x: x.replace(search, input('Введите данные: ')), axis=1)
#     print(data.head(20))
#     data.to_csv(name, index=None)
#     return