# Самостоятельная работа в классе:
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
print("Мое решение задачи - Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них:")
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))
num_4 = int(input('Введите четвертое число: '))
num_5 = int(input('Введите пятое число: '))

if (num_1 > (num_2 and num_3 and num_4 and num_5)):
    print(num_1, ',', num_2, ',', num_3, ',', num_4, ',', num_5, '=>', num_1)
elif (num_2 > (num_1 and num_3 and num_4 and num_5)):
    print(num_1, ',', num_2, ',', num_3, ',', num_4, ',', num_5, '=>', num_2)
elif (num_3 > (num_1 and num_2 and num_4 and num_5)):
    print(num_1, ',', num_2, ',', num_3, ',', num_4, ',', num_5, '=>', num_3)
elif (num_4 > (num_1 and num_2 and num_3 and num_5)):
    print(num_1, ',', num_2, ',', num_3, ',', num_4, ',', num_5, '=>', num_4)
elif (num_5 > (num_1 and num_2 and num_3 and num_4)):       
    print(num_1, ',', num_2, ',', num_3, ',', num_4, ',', num_5, '=>', num_5)
# неверное решение, т. к. если цифры одинаковы - ответ не выдает, 
# а если использовать >=, то при совпадении первых 2 цифр, дальше код не смотрит и выдает неверный ответ
# -------------------------------------------------------------------------------------------------
print("Решение в классе - Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них:")
my_list = []
# my_list.append[] - добавляем элемент в конец списка
# range(5) => [0,1,2,3,4] 
# renge(5, 16) => [5,6,7,8,9,10,11,12,13,14,15]
# range(1, 11, 2) => [1, 3, 5, 7, 9]
for i in range(5):
    num = int(input('--> '))
    my_list.append(num)
print(my_list)
# print(max(my_list))
# print(min(my_list))
maxx = my_list[0]
# print(my_list[1:3])                       # срез от 1 до 3 элементов
# print(my_list[1::2])                      # срез списка с шагом 2
for iten in my_list[1:]:                  # чтобы не сравнивать 0 элемент с самам собой - взяли срез от первого элемента и до конца (т.к. после : нет аргументов, проверит до конца списка)
    if iten > maxx:
        maxx = iten
print(maxx)
# Для того чтобы получить индекс самого большого элемента
maxx_i = 0
for i in range(1, len(my_list)):
    if my_list[i] > maxx: 
        maxx_i = i
        maxx = my_list[i]
        
print(maxx, maxx_i)

#  почему-то не работает maxx_i = i (всегда первоначальное число 0)