# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элеменотов менять нельзя.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.
def creating_data_file ():      # Функция записи данных в txt файл
    list_1 = [1, 5, 2, 3, 7, 9, 11, 8, 15]
    for i in range(len(list_1)):
        k = str(list_1[i])
        data = open('Seminar_5\.Example_16.txt', 'a')
        data.write(k + " ") # добавила разделители
        data.close()
# creating_data_file ()

file = open('Seminar_5\.Example_16.txt', 'r')
data = file.read().split()
file.close()

data = list(map(int, data))
count = data[0]
m_list = [data[i] for i in range(1, len(data)) if data[i] > max(data[0:i])]
m_list.insert(0, data[0])
print(m_list)

def sequence_search(list_n):
    my_list = []
    count = list_n[0]
    my_list.append(count)
    for i in range(1, len(list_n)):
        if list_n[i] > count:
            count = list_n[i]
            my_list.append(count)
    print(my_list)
    
sequence_search(data)