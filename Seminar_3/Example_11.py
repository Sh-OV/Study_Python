# Напишите программу, которая определит позицию второго вхождения строки в списке, либо сообщит, что ее нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем "qwe", ответ: 3    # индекс второго вхождения 3, ищем фразу целиком
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем "йцу", ответ 5 # т.к. элемент на 4 позиции содержит не только искомую фразу, пропускаем
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "цук"], ищем "йцу", ответ -1 # т.к. второго вхождения нет

def Function_list_filling (count):
    txt_list = []
    elem_txt = ""
    while count >= 1:
        elem_txt = input('Введите элементы первой стрки (через Enter): ')
        txt_list.append(elem_txt)
        count -= 1
    return txt_list

list_filling = Function_list_filling (7)
print(list_filling)

def Function_poisk_index (line_1):
    line_2 = input('Введите вторую стрку: ')
    i = 0
    count = 0;
    while i < len(line_1):
        if line_2 == line_1[i]:
            count += 1
            if count == 2:
                num = i
            if count < 2:
                num = -1
        i += 1
    return num

poisk_index = Function_poisk_index (list_filling)
print(f'Nндекс второго вхождения равен: {poisk_index}')

