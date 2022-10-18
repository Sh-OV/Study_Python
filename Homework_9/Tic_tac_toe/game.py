# Создайте программу для игры в ""Крестики-нолики"".
import pygame
import sys


def check_win (array, signal, dig):
    zer = 0
    
    for row in array:
        zer += row.count(0)
        if row.count(signal) == dig:
            return f'Победил {signal}'
        
    for i in range(dig):
        s = 0
        for k in range(dig):
            if array[k][i] == signal:
                s += 1
        if s == dig:
            return f'Победил {signal}'
   
    s = 0 
    for i in range(dig):
        if array[i][i] == signal:
            s += 1
    if s == dig:
        return f'Победил {signal}'
    
    s = 0   
    for i in range(dig):
        if array[i][dig - 1 - i] == signal:
            s += 1
    if s == dig:
        return f'Победил {signal}'
        
    if zer == 0:
        return "Ничья!"
    
    return False
 
 # count = int(input('Введите количество рядов: '))
count = 4
   
pygame.init()
size_block = 100                # Размер блока в пикселях
margin = 15                      # Размер отступа в пикселях
width = heigth = size_block * count + margin * (count + 1)    # Размер окна будет состоять из 3-х блоков и  4-х отступов

size_window = (width, heigth)
screen = pygame.display.set_mode (size_window)
pygame.display.set_caption ("Крестики - нолики")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*count for i in range(count)]             # Массив, заполненный нулями (ноль обозначает, что клетка пока пустая)
query = 0   # множество чисел - ходы игроков (будем увеличивать ее на +1)
game_over = False

while True:                                 
    for event in pygame.event.get():            # Цикл обработки событий
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'X'
                else:
                    mas[row][col] = 'O'
                query += 1 
        elif event.type == pygame.KEYDOWN: #and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0]*count for i in range(count)] 
            query = 0
            screen.fill(black)
            
    if not game_over:        
        for row in range(count):                            # Цикл для отрисовки игрового поля
            for col in range(count):                        # Цикл нахождения координат блока
                if mas[row][col] == 'X':
                    color = red
                elif mas[row][col] == 'O':
                    color = green
                else:
                    color = white   
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect (screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x + 20, y + 20), (x + size_block - 20, y + size_block - 20), 5)
                    pygame.draw.line(screen, white, (x + size_block - 20, y + 20), (x + 20, y + size_block - 20), 5)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block / 2, y + size_block / 2), size_block // 2 - 15, 5)
    
    if (query - 1) % 2 == 0:    #
        game_over = check_win (mas, 'X', count)
    else:
        game_over = check_win (mas, 'O', count)
    
    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('Ariel', 90)     # 'stxinqkai'
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])
    
    pygame.display.update()                             # Для отображения изменений на экране

