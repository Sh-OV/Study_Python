from pytube import YouTube 

link = input('Введите ссылку на видео с Youtube: ')
vid = YouTube(link)
print('Наименование загружаемого файла: ', vid.title)
print('Просмотры: ', vid.views)
print('Длина трека: ', vid.length, 'секунд')
print('Описание: ', vid.description)
print('Рейтинги: ', vid.rating)
vid_download = vid.streams.get_by_itag('17')
vid_download.download("D:\SAVE_PATH")
print('Скачивание завешено!')

