#  Напишите программу вычисления арифметического выражения заданного строкой.
#  Используйте операции +, -, /, *. приоритет операций стандартный.
#  Пример:
#  2 + 2 => 4;
#  1 + 2 * 3 = > 7;
#  1 - 2 * 3 => -5;
#  Добавьте возможность использования скобок, меняющих приоритет операций.
#  Пример:
#  1 + 2 * 3 = > 7;
#  (1 + 2) * 3 = > 9;

from curses.ascii import isdigit

# РЕШЕНИЕ В КЛАССЕ:

def adding_spaces_text (str_text):      # функция добавления пробелов
    spaces = ''
    for i in str_text:
        if i.isdigit():
            spaces += i
        else:   
            spaces += ' ' + i + ' '
    spaces = spaces.split()
    return  spaces

def processing_arithmetic_expression (str_text):    # функция арифметических вычислений
    # str_text = str_text.split()
    # adding_spaces_text (str_text)
    print(f'3 = {str_text}')
    for i in range(len(str_text)):
        if str_text[i].isdigit():
            str_text[i] = int(str_text[i])

    d_1 = {'*': lambda x, y: x * y,
           '/': lambda x, y: x / y}
    d_2 = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y}

    index = 0
    while ('*' in str_text) or ('/' in str_text):
        if str_text[index] in d_1:
            temp = d_1[str_text[index]](str_text[index - 1], str_text[index + 1])
            del str_text[index - 1: index + 2]
            str_text.insert(index - 1, temp)
            index = 0
        else:
            index += 1
            
    while ('+' in str_text) or ('-' in str_text):
        if str_text[index] in d_2:
            temp = d_2[str_text[index]](str_text[index - 1], str_text[index + 1])
            del str_text[index - 1: index + 2]
            str_text.insert(index - 1, temp)
            index = 0
        else:
            index += 1
            
    return str_text
    
def calculations_parentheses(user_str):     # функция вычислений в скобках
    print(f'2 = {user_str}')
    print(f'len = {len(user_str)}')
    a = '('
    b = ')'
    index_open = []
    index_close = []
    
    for i in range(len(user_str)):
        if user_str[i] == a:
            index_open.append(i)
        if user_str[i] == b:
            index_close.append(i)
    print(index_open, index_close, len(index_open))        
    
    if index_open != []: 
        parentheses = user_str
        help = []
        k = 0
        while k < len(index_open):
            for i in range(len(user_str)):
                print(f'{index_open[- 1-k]} : {user_str[index_open[- 1-k]]} ')
                print(f'{index_close[k]} : {user_str[index_close[k]]} ')
                print(f'i = {i}, k = {k}')
                if i > index_open[- 1-k] and i < index_close[k]:
                    help.append(user_str[i]) 
                else:
                    continue 
                 
                print(f'help = {help}')                   
                temp = processing_arithmetic_expression (help)
                print(f'temp = {temp}')
                del parentheses[index_open[- 1-k]: index_close[k] + 1]
                parentheses.insert(index_open[- 1-k], temp)
                print(f'parentheses = {parentheses}')
               
            k += 1

            
        
        
# input_text = input('Введите арифметическое выражение: ')
input_text = '1+((2-7+11)*9-12)*2/2'
# print(input_text)
adding_spaces = adding_spaces_text (input_text)
print(f'1 = {adding_spaces}')   
calculations_parentheses(adding_spaces)
print(eval(input_text))   




