# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = int(input('введите трехзначное число: '))
sum = 0 
for i in range(3):
    r = num % 10
    sum += r
    num //= 10
print(f'Сумма чисел введенного числа = {sum}')