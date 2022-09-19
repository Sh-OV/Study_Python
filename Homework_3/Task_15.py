# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Задайте число для списка чисел Фибоначчи: '))

def Function_Fibo_list (number):
    f1 = 0
    f2 = 1
    f_pos = [0, 1]
    for i in range(number-1):
        fn = f1 + f2
        f1 = f2
        f2 = fn
        f_pos.append(fn)
    
    f1 = 1
    f2 = -1
    f_neg = [1, -1]
    for i in range(number-2):
        fn = f1 - f2
        f1 = f2
        f2 = fn
        f_neg.append(fn)
    
    help = 0
    i = 0
    if len(f_neg) % 2 == 0:
        len_list = len(f_neg) // 2
    else:
        len_list = len(f_neg) // 2 + 1
       
    while i < len_list:
        help = f_neg[i]
        f_neg[i] = f_neg[((len(f_neg)-1)-(1*i))]
        f_neg[((len(f_neg)-1)-(1*i))] = help
        i += 1
    
    fibo_liost = f_neg + f_pos
    return fibo_liost
    
fibo_list = Function_Fibo_list (num)
print(fibo_list)