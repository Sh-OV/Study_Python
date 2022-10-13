import logic_module as lm


def choosing_action():          # функция выбора и выполнения действия с базой данных (1 добавить пользователя, 2 найти пользователя, 3 заменить данные, 4 удалить данные)
    choos = int(input('Выберите цифру от 1 до 4, в зависимости от операции с телефонной книгой \n' +
                  '(1 добавить пользователя, 2 найти пользователя, 3 заменить данные, 4 удалить данные):  '))
    if choos == 1:
        lm.writing_database()
    elif choos == 2:
        return lm.search_database()
    elif choos == 3:
       return lm.making_changes_database()
    elif choos == 4:
        return lm.deleting_part_database()
    else:
        return None

question = 1
while question == 1:
    choosing_action()
    question = int(input('Если Вам необходимо выполнить еще какие-либо действия \n' +
                     'с телефонной книгой - нажмите 1, если нет - нажмите 0:  '))

