# Задайте два числа. Напишите программу, которая НОК (наименьшее общее кратное) этих двух чисел
# Решим задачу через алгоритм Евклида

def Function_user_data ():
    user = input('Введите два натуральных числа (через пробел): ')
    user_s = user.split(' ')
    user_list = list(map(int, user_s))
    return user_list
user_data = Function_user_data ()
print(user_data)


def Function_algorithm_Euclid (my_list):
    n = my_list[0]
    m = my_list[1]
    nod = 0
    count = m * n
    while n != m:
        if n > m:
            n = n - m
        else:
            m = m - n
    nod = n
    nok = count / nod
    return nok
    
algorithm_Euclid = Function_algorithm_Euclid (user_data)
print(algorithm_Euclid)

