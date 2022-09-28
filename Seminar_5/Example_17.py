# Напишите программу, удаляющую из текста все слова, содержащие "абв".
my_text_1 = "Я неабв люблю абвук Python кабвуц"
my_text_2 = "абв"

my_list = my_text_1.split()
print(my_list)

# Первый варимант решения
i = 0
while i in range(len(my_list)):
    if my_text_2 in my_list[i]:
        my_list.remove(my_list[i])
    else:
        i += 1
print(my_list)

# Второй вариант решения
list_1 = [item for item in my_list if my_text_2 not in item]
print(list_1)