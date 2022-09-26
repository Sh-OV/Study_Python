# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

def creating_data_file ():
    list_1 = [1, 2, 3, 4, 5, 7, 8, 9]
    for i in range(len(list_1)):
        k = str(list_1[i])
        data = open('Seminar_5\.Example_15.txt', 'a')
        data.write(k + " ") # добавила разделители
        data.close()

file = open('Seminar_5\.Example_15.txt', 'r')
data = file.read().split()
file.close()
data = list(map(int, data))
num = [(data[i]-1) for i in range(1, len(data)) if data[i]-1 != data[i-1]]
print(num)

# for i in range(1, len(data)):
#     if data[i]-1 != data[i-1]:
#         print(data[i]-1)
        
