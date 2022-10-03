# Создайте программу для игры с конфетами человек против бота. Наделите бота "интеллектом".
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 

import random

def draw (number):      # функция жеребьевки
    lot_bot = 0
    lot_g = 0
    while lot_bot == lot_g:
        print(f'Правила игры: На столе лежит {number} конфета. Вы играете с Ботом, делая ход друг после друга\n Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет\n Все конфеты оппонента достаются сделавшему последний ход')
        print("Проведем жребий: у кого выпадет большее число, тот ходит первым")
        lot_bot = random.randint(1, 10)
        print(f'Жребий для Бота - выпало число: {lot_bot}')
        lot_g = random.randint(1, 10)
        print(f'Жребий для игрока - выпало число: {lot_g}')
    if lot_bot > lot_g:
        return 1
    elif lot_bot < lot_g:
        return 2

def steps_game (count, s, dr):      # функция игры
    dig = s
    if dr == 1:
        print("Первым ходит Bot")
        while count > 0:
            if count <= s * 2 and count > 0:
                if count > s:
                    bot = count - (s + 1)
                    if bot < 1:
                        bot = count - s
                    count -= bot    
                    print(f'Бот сделал свой ход. он забрал {bot} конфет. Осталось {count} конфет')    
                else:
                    bot = count
                    print(f'<Bot забрал оставшиеся {bot} конфет и стал ПОБЕДИТЕЛЕМ ! Не расстраивайтесь, попоробуйте еще раз!')
                    return
            elif count > s * 2:
                bot = random.randint(1, s + 1)
                count -= bot
                print(f'Бот сделал свой ход. он забрал {bot} конфет. Осталось {count} конфет')
            else:
                print("Победителем стал игрок! Поздравляем!!!") 
                return
            if count >= s:
                step_g = s + 1
                while step_g > s:
                    step_g = int(input(f'Ваш ход, ход не должен превышать {s}: '))
                    if step_g > s:
                        print("Ваша ставка превышает разрешенную, переходите!")
                count -= step_g
                print(f' Осталось {count} конфет')       
    else:
        print("Первым ходит игрок")
        while count > 0:
            if count > 0:
                step_g = s + 1
                while step_g > s:
                    step_g = int(input(f'Ваш ход, ход не должен превышать {s}: '))
                    if step_g > s:
                        print("Ваша ставка превышает разрешенную, переходите!")
                count -= step_g
                print(f' Осталось {count} конфет')       
            if count <= s * 2 and count > 0:
                if count > s:
                    bot = count - (s + 1)
                    if bot < 1:
                        bot = count - s
                    count -= bot    
                    print(f'Бот сделал свой ход. он забрал {bot} конфет. Осталось {count} конфет')    
                else:
                    bot = count
                    print(f'<Bot забрал оставшиеся {bot} конфет и стал ПОБЕДИТЕЛЕМ ! Не расстраивайтесь, попоробуйте еще раз!')
                    return
            elif count > s * 2:
                bot = random.randint(1, s + 1)
                count -= bot
                print(f'Бот сделал свой ход. он забрал {bot} конфет. Осталось {count} конфет')
            else:
                print("Победителем стал игрок! Поздравляем!!!") 
                return
            
num = 2021      # лежит конфет на столе
st = 28         # можно взять конфет за один ход  
      
draw = draw (num)
print(draw) 
steps_game (num, st, draw)  
    
    
                