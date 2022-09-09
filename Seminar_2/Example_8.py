# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой

print('Решение № 1: ')

line_1 = input('Введите первую стрку: ')
line_2 = input('Введите вторую стрку: ')

def Function_counting_occurrences(l1, l2):
    count_s = l1.count(l2)
    return count_s

counting_occurrences = Function_counting_occurrences(line_1, line_2)
print(counting_occurrences)

print('Решение № 2: ')

counter = 0
count = 0
len_1 = len(line_1)
len_2 = len(line_2)

while count < len_1:
    if (line_1[count : (count + len_2)] == line_2):
        counter += 1
    count += 1
print(counter)