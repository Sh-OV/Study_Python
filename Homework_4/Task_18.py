# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

def Function_user_data ():        # Функция обработки данных от пользователя
    user = input('Введите числа через прорбел: ')
    user_s = user.split(' ')
    user_list = []
    for i in range(len(user_s)):
        user_list.append(int(user_s[i]))
    return user_list

def Function_non_repeating_elements (user_list):    # Функция создания списка неповторяющихся элементов
    my_list = []
    elem = 0
    for i in user_list:
        count = 0
        elem = i
        for j in user_list:
            if elem == j:
                count += 1
        if count == 1:
            my_list.append(i)
    return my_list

user_data = Function_user_data ()
print(user_data)
                
non_repeating_elements = Function_non_repeating_elements (user_data)
print(non_repeating_elements)