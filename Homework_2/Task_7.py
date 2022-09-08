# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
number = int(input('Введите число целое число N:'))
arg = 0
count = 1
my_list = []

while count <= number:
    if count == 1:
        arg = count
    else:
        arg = count * my_list[count-2]
    my_list.append(arg)
    count += 1
    
print(f'Пусть N = {number}, тогда {my_list}')