num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
print(type(num_1))
if (num_2 == (num_1 ** 2)):
    print(True)
elif (num_1 == (num_2 ** 2)):
    print(True)
else: 
    print(False)