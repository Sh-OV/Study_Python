import logging

path_log = 'Homework_8\log.txt'
_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

def get_file_handler():                 # Обработчик файла
    file_handler = logging.FileHandler(path_log, 'a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler

def get_stream_handler():               # Обработчик потока
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger











# from cgitb import handler
# import logging
# # import view_csv as vc
# # from cv2 import log
# # import requests

# path_log = 'Homework_8\log.txt'

# logging.basicConfig(level=logging.DEBUG,
#                     filename=path_log, filemode='a',
#                     format='%(asctime)s : %(levelname)s : %(message)s')

# # add_csv = vc.add_subscriber()
# # logging.debug(f'В файл csv добавлен контакт: {add_csv}')

# # logging.debug("debug")
# # logging.info("info")
# # logging.warning("warning")
# # logging.error("error")
# # logging.critical("critical")

# logger = logging.getLogger(__name__)
# handler = logging.FileHandler(path_log)
# formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)

# logger.info('tast the custom logger')
# # def main(name):
# #     logger.debug(f'Enter in the main() function: name = {name}')     # уровень DEBAG

# #     # r = requests.get('https://ya.ru/')


# # if __name__ == '__main__':
# #     main('oleg')
    