# модуль, берущий данные из модуля registration и записывающий данные в файлы, из него мы можем запросить данные

import registration as reg
# import csv
# import pandas as pd

def record_data_file(name_1,  modif_1, sep_1, e_line_1, name_2,  modif_2, sep_2, e_line_2):     # запись данных в файлы csv, txt
    i_data = reg.input_data()
    for i in range(len(i_data)):
        k = i_data[i]
        with open(name_1, modif_1, encoding='utf-8') as file_1:
            file_1.write(k + sep_1) 
    with open(name_1, modif_1) as file_1:
            file_1.write(e_line_1)
            file_1.close()
    for j in range(len(i_data)):
        h = i_data[j]
        with open(name_2, modif_2, encoding='utf-8') as file_2:
            file_2.write(h + sep_2) 
    with open(name_2, modif_2) as file_2:
            file_2.write(e_line_2)
            file_2.close()
    return

def search_data_csv(name, search):          # поиск данных в файле csv
    index = []
    l_num = 0
    data = open(name, 'r', encoding='utf-8')
    for line in data:
        # print(f'line_old = {line}')
        line = line.split(',')
        # print(line, len(line))
        for i in range(len(line)):
            if line[i] == search:
                temp = line
                # print(f'temp = {temp}, l_num = {l_num}')
                index.append(l_num)
                index.append(temp)
        l_num += 1
    print(f'index = {index}')            
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
    print(f'list_data = {list_data}')
    data.close()
    return list_data

def replacing_data_file_csv(name, search):            # замена части данных в файле csv
    sear = search_data_csv(name, search)
    data = open(name, 'r+', encoding='utf-8')
    l_num = 0
    i = 0
    for line in data:
        print(f'line = {line}')
        if l_num == sear[i]:
            del line
            line.insert(record_data_file)
            print(f'line_new = {line}')
            i += 2
            
        l_num += 1
    return



# del str_text[index - 1: index + 2]
    #         str_text.insert(index - 1, temp)

def removal_data_file_csv(name, search):            # удаление части данных в файле csv
    search_data_csv(name, search)
    
    
    return




# record_data_file('Homework_7\Telephone_directory_csv', 'a', ",", '\n')
# record_data_file('Homework_7\Telephone_directory.txt', 'a', "\n\n", '----------\n')

# record_data_file('Homework_7\Telephone_directory_csv', 'a', ",", '\n', 'Homework_7\Telephone_directory.txt', 'a', "\n\n", '----------\n\n')

# search_data_csv('Homework_7\Telephone_directory_csv', 'Попов')

# search_data_txt('Homework_7\Telephone_directory.txt', 'Попов\n')

replacing_data_file_csv('Homework_7\Telephone_directory_csv', 'Мама')

