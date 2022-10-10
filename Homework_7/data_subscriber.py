# модуль, берущий данные из модуля registration и записывающий данные в файлы, из него мы можем запросить данные

import registration as reg

# def get_last_name():
#     return reg.i_data[0]

# def name():
#     return reg.i_data[1]

# def get_group():
#     return reg.i_data[2]

# def get_phone_number_home():
#     return reg.i_data[3]

# def get_phone_number_work():
#     return reg.i_data[4]

# def get_phone_number_personal_1():
#     return reg.i_data[5]

# def get_phone_number_personal_2():
#     return reg.i_data[6]

# def get_email():
#     return reg.i_data[7]

# def get_address():
#     return reg.i_data[8]

# def get_other_information():
#     return reg.i_data[9]


def record_data_file(name, s):
    for i in range(len(reg.i_data)):
        k = reg.i_data[i]
        with open(name, 'a') as file:
            file.write(k + s) 
    with open(name, 'a') as file:
            file.write('\n')
            file.close()
    return

record_data_file('Homework_7\Telephone_directory_csv', ",")
record_data_file('Homework_7\Telephone_directory.txt', "\n\n")

        

