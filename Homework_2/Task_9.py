# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

number = int(input('Введите число целое число N: '))

def Function_list_filling (count):
    my_list = []
    num = -count
    while num <= count:
        my_list.append(num)
        num += 1
    return my_list

list_filling = Function_list_filling (number)
print(list_filling)

def Function_list_multiplication (m_list):
    numbers = input(f'Введите индексы списка, через пробел, которые необходимо умножить между собой \n(индексы должны быть в диапазоне от 0 до {len(m_list)}): ')
    data = numbers.split(' ')
    len_num = len(data)
    multiplic = 1
    for i in range(len(m_list)):
        for j in range(len(data)):
            if int(data[j]) == i:
               multiplic *= m_list[i]
            j += 1
    return [multiplic, data]

list_multiplication = Function_list_multiplication (list_filling)
print(f'Произведение элементов с индексами {list_multiplication[1]} --> {list_multiplication[0]}')

        
        



