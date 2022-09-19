# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

sys = int(input('Введите номер системы, в которую хотите преобразовать число (двоичная - 2, десятичная - 10 и т.п.): '))
num = int(input('Введите число, которе хотите преобразовать: '))

def Function_trans_lation_num (syst, number):
    trans = ''
    while number // syst > 0:
        dig = number % syst
        number //= syst
        trans = str(dig) + trans
    trans = str(number) + trans
    return trans

trans_lation_num = Function_trans_lation_num (sys, num)   

print(f'После преобразования десятичного числа {num} в {sys}-ичную получается: {trans_lation_num}')
