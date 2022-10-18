from datetime import datetime as dt

path = '1_Lectures\Lesson_4\Information gathering\log_csv'

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(path, 'a') as file:
        file.write('{}; temperature; {}\n'
                    .format(time, data))
    return

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(path, 'a') as file:
        file.write('{}; pressure; {}\n'
                    .format(time, data))
    return

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(path, 'a') as file:
        file.write('{}; wind_speed; {}\n'
                    .format(time, data))
    return
