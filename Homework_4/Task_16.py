# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

import math

user_d = (input('Введите значение точности (например: 0.001): '))
len_u = user_d.split('.')
d_len = len(len_u[1])
pi = round(math.pi,d_len)
print(f'при $d = {user_d}, π = {pi}')