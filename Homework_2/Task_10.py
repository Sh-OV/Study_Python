# Реализуйте алгоритм перемешивания списка.

number = int(input('Введите количество элементов списка: '))

def Function_list_creation(num):
    my_list = []
    dig = 0
    while dig <= num:
        my_list.append(dig)
        dig += 1
    return my_list
        
list_creation = Function_list_creation(number)
print(list_creation)    
