## Дополнительные библиотеки для Python ищем на сайте 

<https://pypi.org>

## Для создания виртуального окружения в локальном проекте необходимо следующее:

1. В корневой папке нашего проекта открываем терминал и пишем:

python3 -m venv .venv   // Для моего компьютера не сработала

py -3.10 -m venv .venv  // Вот так получилось 

Эта команда (одна из этих) устанавливает оболочку python в наш проект в папку .venv

2. После того, как мы установили оболочку, надо ее активировать. Для этого делаем следующее:

    1). В правом нижнем углу в VSCode написана версия питона и путь к нему, которые VSCode использует в данный момент. Для того, чтобы эти данные в VSCode отображались надо, чтобы был открыт любой файл с расширением .py

    2). Нажимаем на вышеуказанную надпись, сверху, посередине, откроется окно "выбор интерпритатора"

    3). Нажимаем "+ введите путь к интерпритатору...". Появляется активное акно "Введите путь к интерпритатру Python"

    4). Идем в наш проект, к файлу .venv\Scripts\python.exe и копируем путь к нему (правой кнопкой мыши по файлу - открывается меню, где можно выбрать "Скопировать путь")

    5). Вставляем скопированный путь в активное акно "Введите путь к интерпритатру Python", нажимаем Enter

    6). Внизу справа в VSCode, где написана версия питона и путь к нему поменяется на указанный нами

3. Теперь надо активировать виртуальный Python в терминале VSCode:

    1). Необходимо скопировать путь до папки Scripts, которая находится в папке .venv

    2). Набираем в терминале команду: 

        cd и через пробел вставляем путь к папке Scripts  // если не получилось можно попробовать cmd вместо cd

    3). Затем пишем команду:

        cmd  // похоже команды 2 и 3 надо поменять местами

    4). Затем пишем команду:

        activate

    5). Убеждаемся, что терминал работате с нашим виртуальным приложением - строка в терминале должна начинаться (.venv)

## Чтобы выйти из виртуального окружения в обычный python (в терминале) надо:

    1) Набрать команду:

           exit

    2) В правом нижнем углу в VSCode нажать на версию python и заменить виртуальный python на глобальный