# Напишите программу, которая на вход будет принимать число N и выводить числа от -N до N
# print('Мое решение - принимать число N и выводить числа от -N до N: ')
num = int(input('Введите число N: '))
for i in range(-num, num + 1):
    print( i, end = ' ')
 