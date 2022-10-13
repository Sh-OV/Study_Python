# модуль, содержащий логику программы (в нем располагается главная функция, определяется чсто за чем идет и т.д.)

import registration as reg
import data_subscriber as ds
import csv
import pandas as pd

patch_csv = 'Homework_7\Telephone_directory_csv'
patch_txt = 'Homework_7\Telephone_directory.txt'


def writing_database():                 # запись данных в базу данных (используя модуль data_subscriber)
    ds.record_data_file(patch_csv,  'a', "\n", patch_txt,  'a', "----------\n\n")
    return

def search_database():                  # поиск данных в базе
    user_request = input('Введите искомый элемент: ')
    u_txt = user_request + '\n'
    print(f'u_txt = {u_txt}')
    res_csv = ds.search_data_csv(patch_csv, user_request)
    res_txt = ds.search_data_txt(patch_txt, u_txt)
    print(res_csv)
    print(res_txt)
    return

def making_changes_database():          # внесение изменений в базу данных (пока только в формат csv)
    user_request = input('Введите искомый элемент: ')
    user_replacement = input('Введите элемент на который будем заменять: ')
    ds.replacing_data_elem_csv(patch_csv, user_request, user_replacement)
    return

def deleting_part_database():           # удаление части базы данных (пока только из формата csv)
    user_request = input('Введите элемент контакта, который хотите удалить: ')
    ds.removal_data_file_csv(patch_csv, user_request)
    return

