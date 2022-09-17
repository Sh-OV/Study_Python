# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
from time import time

def Custom_generator_rand_numb ():
    my_list = []
    count = 0
    n = 0
    number_gen = int(input('Введите количесмтво необходимых случайных чисел: '))
    while n < (number_gen + 1):
        sec = str(time())
        num = sec[13:17] 
        print(num)
        my_list.append(num)
        n += 1
    return my_list

generator_rand_numb = Custom_generator_rand_numb()
print(generator_rand_numb)

