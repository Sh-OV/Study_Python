# Для натурального n создать словарь индекс-значение, состоящий
# из элементов последовательности 3n + 1
# Пример:
# Для n = 6 : {1:4, 2:7, 3:10, 4:13, 5:16, 6:19}

number = int(input('Введите натуральное число N: '))

print('Решение № 1 (не совсем правильное):')
def Function_list_filling (count):
    my_list = []
    dig = ""
    num = 1
    fig = 0
    while num <= count:
        fig = (3 * num + 1)
        dig = f"{num} : {fig}"
        my_list.append(dig)
        num += 1
    return my_list

list_filling = Function_list_filling (number)
print(list_filling)

print('Решение № 2 (метод создания словаря):')
my_dict = {x: (3 * x + 1) for x in range(1, number)}
print(my_dict)