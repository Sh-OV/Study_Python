# Задайте строку из набора чисел. Напитшите програмиму, которая покажет большее и меньшее число.
# В качестве символа - разделителя используйте пробел

def Function_user_data ():
    user = input('Введите числа через прорбел: ')
    user_s = user.split(' ')
    user_list = list(map(int, user_s))
    return user_list
user_data = Function_user_data ()
print(user_data)

def Function_max_min_number (my_list):
    min = my_list[0]
    max = my_list[0]
    for i in range(0, len(my_list)):
        if my_list[i] < min:
            min = my_list[i]
        if my_list[i] > max:
            max = my_list[i]
    return min, max

max_min_number = Function_max_min_number (user_data)
print(f'max = {max_min_number[1]}, min = {max_min_number[0]}')