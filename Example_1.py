# Напишите программу, которая принимаетна ввод 2 числа и проверяет
# является ил одно число квадратом другого?

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
# print(type(num_1))
if (num_2 == (num_1 ** 2)) and (num_1 == (num_2 ** 2)):
    print(True)
# elif (num_1 == (num_2 ** 2)):
    # print(True)
else: 
    print(False)
    
# Самостоятельная работа в классе:
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))
num_4 = int(input('Введите четвертое число: '))
num_5 = int(input('Введите пятое число: '))

if (num_1 >= (num_2 and num_3 and num_4 and num_5)):
    print(num_1, ',', num_2, ',', num_3, ',', num_4, ',', num_5, '=>', num_1)
elif (num_2 >= (num_1 and num_3 and num_4 and num_5)):
    print(num_1, ',', num_2, ',', num_3, ',', num_4, ',', num_5, '=>', num_2)
elif (num_3 >= (num_1 and num_2 and num_4 and num_5)):
    print(num_1, ',', num_2, ',', num_3, ',', num_4, ',', num_5, '=>', num_3)
elif (num_4 >= (num_1 and num_2 and num_3 and num_5)):
    print(num_1, ',', num_2, ',', num_3, ',', num_4, ',', num_5, '=>', num_4)
elif (num_5 >= (num_1 and num_2 and num_3 and num_4)):
    print(num_1, ',', num_2, ',', num_3, ',', num_4, ',', num_5, '=>', num_5)