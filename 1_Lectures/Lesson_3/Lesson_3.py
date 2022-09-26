# colors = ['red', 'green', 'blue']
# data = open('1_Lectures\Lesson_2\.file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()


# path = '1_Lectures\Lesson_2\.file.txt'
# data = open(path, 'r')
# for line in data:
#  print(line)
# data.close()

# К чему это всё?
# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
for i in range(len(list_1)):
    k = str(list_1[i])
    data = open('1_Lectures\Lesson_3\.file.txt', 'a')
    data.write(k + " ") # разделителей не будет
    data.close()
    
path = '1_Lectures\Lesson_3\.file.txt'
data = open(path, 'r')
for line in data:
 print(line)
data.close()

f = open('1_Lectures\Lesson_3\.file.txt', 'r')
data = f.read()# + ' '
f.close()
numbers = []
while data != '':
 space_pos = data.index(' ')
 numbers.append(int(data[:space_pos]))
 data = data[space_pos+1:]
out = []
for e in numbers:
 if not e % 2:
    out.append((e,e **2))
print(out)

#  или:

list_2 = [(i, i**2) for i in list_1 if i % 2 == 0]
print(list_2)

# или

file = open('1_Lectures\Lesson_3\.file.txt', 'r')
data = file.read().split()
file.close()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print(data)



