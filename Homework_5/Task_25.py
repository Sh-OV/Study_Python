# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def creating_data_file (text_1, path):      # функция записи данных
    data = open(path, 'r+')
    data.writelines(text_1)
    data.close()
    data = open(path, 'r')
    file = str(data.read())
    data.close()
    return file

def data_encoding_RLE (file):       # функция кодирования RLE (сжатие данных)
    text_coding = ''
    count = 1
    i = 0
    while i < len(file):
        if i < len(file) - 1:
            if file[i] == file[i + 1]:
                count += 1
            else:
                text_coding += str(count) + file[i]
                count = 1
        if i == len(file) - 1:
            text_coding += str(count) + file[i]
        i += 1
    return text_coding
            
def data_decoding_RLE (text_2):       # функция раскодирования RLE (восстановления данных)
    text_decoding = ''
    i = 0
    while i < len(text_2):
        if i % 2 == 0:
            k = 0
            while k < int(text_2[i]):
                text_decoding += text_2[i + 1]
                k += 1
        i += 1
    return text_decoding

creating_data = creating_data_file (input('Введите символы для кодирования: '), 'Homework_5\.Task_25_input.txt')
data_encoding = data_encoding_RLE (creating_data)
creating_RLE = creating_data_file (data_encoding, 'Homework_5\.Task_25_output.txt')
data_decoding = data_decoding_RLE (creating_RLE)
creating_decoding = creating_data_file (data_decoding, 'Homework_5\.Task_25_input.txt')

print(creating_data)
print(creating_RLE)
print(creating_decoding)
