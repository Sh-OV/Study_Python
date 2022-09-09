# Напишите программу, которая принимает на вход число N и
# выдает последовательность из N членов
# Пример
# Для N = 5 : 1, -3, 9, -27, 81

number = int(input('Введите натуральное число N: '))

def Function_list_filling (count):
    my_list = []
    num = 2
    dig = 1
    my_list.append(dig)
    while num <= count:
        dig *= -3
        my_list.append(dig)
        num += 1
    return my_list

list_filling = Function_list_filling (number)
print(list_filling)