# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11
number = (input('Введите вещественное число: '))
len_num = len(number.split('.')[1])
def Sum_digits (num, quant):
    num = float(num)
    num *= 10 ** quant
    num = int(abs(num))
    
    count = 0
    sum = 0
    while (num > 0):
        sum += num % 10
        num //= 10
    return sum
rezult = Sum_digits(number, len_num)
print(f'{number} -> {rezult}')