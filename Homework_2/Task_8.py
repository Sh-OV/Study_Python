# Задайте список из k чисел последовательности (1 + 1\k)^k 
# и выведите на экран их сумму.

number = int(input('Введите число целое число k для создания последовательности: '))
sum = 0
num = 1
seq_num = 0

while num <= number:
    seq_num = (1 + 1 / num) ** num
    sum += seq_num
    num += 1
    
print(round(sum, 2))

