# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

num = int(input('Введите натуральное число: '))

def Function_multiplier (number):
    prime_multipliers = [7, 5, 3, 2, 1]
    mult = 0
    for i in range(len(prime_multipliers)):
        if (number % prime_multipliers[i] == 0):
            mult = prime_multipliers[i]
            return mult
    

def Function_list_multiplier (number):
    my_list = []
    multip = number
    elem = 0
    i = 0
    while multip > 1:
        elem = Function_multiplier (multip)
        my_list.append(elem)
        multip = multip / elem
        i += 1
    return my_list
list_multiplier = Function_list_multiplier (num)
print(list_multiplier)


# Хотела сделать через рекурсию, пока не получилось...
# def function_multiplier (number):
#     prime_multipliers = [7, 5, 3, 2, 1]
#     mult = 1
#     count = 0
#     if mult == 1:
#         for i in range(len(prime_multipliers)):
#             print(f'len(prime_multipliers) = {len(prime_multipliers)}')
#             if (number % prime_multipliers[i] == 0):
#                 count = prime_multipliers[i]
#                 print(f'count = {count}')
#                 mult = number / prime_multipliers[i]
#                 print(f'mult = {mult}')
#                 return count
#     else:
#         print(mult)
#         count = function_multiplier (mult)
#         my_list.append(function_multiplier (mult))
#         print(my_list)
 
# my_list = []   
# my_list.append(function_multiplier (num))   

# print(my_list)
  