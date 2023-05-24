'''
Задача 12:  Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
            Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
            а Катя должна их отгадать. Для этого Петя делает две подсказки. 
            Он называет сумму этих чисел S и их произведение P. 
            Помогите Кате отгадать задуманные Петей числа.
'''
import random

X = random.randint(1,1000)
Y = random.randint(1,1000)
S = X + Y
P = X * Y
print(f'X = {X}, Y = {Y}, S = {S}, P = {P}')
if X >= Y:
    x = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
    y = int(P / x)
else:
    y = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
    x = int(P / y)
    
print(f'x = {x}, y = {y}')
