'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
            Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
            В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
'''
import random

n = int(input('Введите натуральное число N: '))
a = random.randint(1, 10)
arr = []
for i in range(1,n+1):
    print(i * a, end=' ')
    arr.append(i * a)
x = random.randint(1, n * a)

print()
print(x)
num = 0

for item in arr:
    if item == x:
        num = x

if num == 0:
    for k in range(0, len(arr)):
        if x < arr[0]:
            num = arr[k]
        elif k >= 1 and x > arr[k-1] and x < arr[k]:
            min = arr[k-1]
            max = arr[k]
            if x-min > max-x:
                num = max
            else: num = min
        elif x > arr[len(arr)-1]:
            num = arr[len(arr)-1]

print(f'-> {num}')
