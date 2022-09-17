#  Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# Например.
# Искомое число 7 [fdgfh678, fdfgh45g, dfgdfgh779] --> [fdgfh678, dfgdfgh779]

def Function_list_filling (count):
    txt_list = []
    elem_txt = ""
    while count >= 1:
        elem_txt = input('Введите элементы - буквц, цифры в виде кода (через Enter): ')
        txt_list.append(elem_txt)
        count -= 1
    return txt_list

list_filling = Function_list_filling (7)
print(list_filling)

def Function_adjustment_request (line_1):
    line_2 = input('Введите запрос (искомое число): ')
    my_list = []
    i = 0
    count = 0;
    while i < len(line_1):
        for j in line_1[i]:
            if j == line_2:
                my_list.append(line_1[i])
        i += 1
    return my_list

adjustment_request = Function_adjustment_request (list_filling)
print(f'Искомое число есть в следующих элементах: {adjustment_request}')
