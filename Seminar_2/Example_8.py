# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой

line_1 = input('Введите первую стрку: ')
line_2 = input('Введите вторую стрку: ')

def Function_counting_occurrences(l1, l2):
    count_s = l1.count(l2)
    return count_s

counting_occurrences = Function_counting_occurrences(line_1, line_2)
print(counting_occurrences)