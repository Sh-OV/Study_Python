# модуль, принимающий данные от пользователя (добавление новых абонентов)
# и передающий их дальше для обработки в модуль data_subscriber

def list_contact_parameters():
    my_list = []
    pc_0 = 'Фамилия абонента: '
    my_list.append(pc_0)
    pc_1 = 'Имя абонента: '
    my_list.append(pc_1)
    pc_2 = 'Группа абонента: '
    my_list.append(pc_2)
    pc_3 = 'Домашний телефон: '
    my_list.append(pc_3)
    pc_4 = 'Рабочий телефон: '
    my_list.append(pc_4)
    pc_5 = 'Личный телефон 1: '
    my_list.append(pc_5)
    pc_6 = 'Личный телефон 2: '
    my_list.append(pc_6)
    pc_7 = 'E-mail: '
    my_list.append(pc_7)
    pc_8 = 'Адрес абонента: '
    my_list.append(pc_8)
    pc_9 = 'Прочая информация: '
    my_list.append(pc_9)
    return my_list

def input_data():
    question = list_contact_parameters()
    print('Заполните данные абонента, если какие-то данные отсутсвуют, нажмите 0')
    d_0 = input(question[0])
    d_1 = input(question[1])
    d_2 = input(question[2])
    d_3 = input(question[3])
    d_4 = input(question[4])
    d_5 = input(question[5])
    d_6 = input(question[6])
    d_7 = input(question[7])
    d_8 = input(question[8])
    d_9 = input(question[9])
    return [d_0, d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9]


