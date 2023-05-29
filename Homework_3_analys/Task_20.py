'''
Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12
    '''
word = input('Введите слово: ') 
word = word.upper()

def search_alf(text):
    cyrillic =  {'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 
                 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 
                 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'ь', 'Э', 'Ю', 'Я'}
    answer = bool(cyrillic.intersection(set(text)))
    return answer

arr_1point_en = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
arr_2point_en = ['D', 'G']
arr_3point_en = ['B', 'C', 'M', 'P']
arr_4point_en = ['F', 'H', 'V', 'W','Y']
arr_5point_en = ['K']
arr_8point_en = ['J', 'X']
arr_10point_en = [ 'Q', 'Z']

arr_1point_ru = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
arr_2point_ru = ['Д', 'К', 'Л', 'М', 'П', 'У']
arr_3point_ru = ['Б', 'Г', 'Ё', 'Ь', 'Я']
arr_4point_ru = ['Й', 'Ы']
arr_5point_ru = ['Ж', 'З', 'Х', 'Ц', 'Ч']
arr_8point_ru = ['Ш', 'Э', 'Ю']
arr_10point_ru = ['Ф', 'Щ', 'Ъ']

def calculation_word_en(text):
    res = 0
    for item in text:
        for letter in arr_1point_en:
            if item == letter:
                res += 1
        for letter in arr_2point_en:
            if item == letter:
                res += 2
        for letter in arr_3point_en:
            if item == letter:
                res += 3
        for letter in arr_4point_en:
            if item == letter:
                res += 4
        for letter in arr_5point_en:
            if item == letter:
                res += 5
        for letter in arr_8point_en:
            if item == letter:
                res += 8
        for letter in arr_10point_en:
            if item == letter:
                res += 10
    return res

def calculation_word_ru(text):
    res = 0
    for item in text:
        for letter in arr_1point_ru:
            if item == letter:
                res += 1
        for letter in arr_2point_ru:
            if item == letter:
                res += 2
        for letter in arr_3point_ru:
            if item == letter:
                res += 3
        for letter in arr_4point_ru:
            if item == letter:
                res += 4
        for letter in arr_5point_ru:
            if item == letter:
                res += 5
        for letter in arr_8point_ru:
            if item == letter:
                res += 8
        for letter in arr_10point_ru:
            if item == letter:
                res += 10
    return res

answer_search_alf = search_alf(word)

if answer_search_alf == True:
    calc_word = calculation_word_ru(word)
else:
    calc_word = calculation_word_en(word)

print(calc_word)