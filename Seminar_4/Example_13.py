#  Найдите корни квадратного уровнения Ах2 + Вх + С = 0 двумя способами:
#  1) с помощью математических формул нахождения корней квадратного уровнения
#  2) с помощью дополнительных библиотек Python

def Function_user_data ():
    user = input('Введите аргументы (A, B, C) для квадратного уравнения Ах2 + Вх + С = 0 (через пробел): ')
    user_s = user.split(' ')
    user_list = list(map(int, user_s))
    return user_list
user_data = Function_user_data ()
print(user_data)

def Function_quadratic_equation (my_list):
    a = my_list[0]
    b = my_list[1]
    c = my_list[2]
    if a == 0:
        x1 = - b - c
        result = f'Т.к. А = 0, уравнение является линейным и имеет 1 корень. х = {x1}'
    else:    
        discrim = b ** 2 - 4 * a * c
        print(discrim)
        if discrim > 0:
            x1 = round((- b + discrim ** (1/2)) / (2 * a),3)
            x2 = round((- b - discrim ** (1/2)) / (2 * a),3)
            result = (f'Уравнение имеет 2 корня. х1 = {x1}, x2 = {x2}')
        elif discrim == 0:
            x1 = round((- b + discrim ** (1/2)) / (2 * a),3)
            result = f'Уравнение имеет 1 корень. х = {x1}'
        else:
            result = f'Уравнение корней НЕ ИМЕЕТ'
    return result
            
quadratic_equation  = Function_quadratic_equation (user_data)
print(quadratic_equation)