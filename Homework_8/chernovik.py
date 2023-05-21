from os import link
from pytube import YouTube 
from cProfile import label
from tkinter import *



def input_data_link():
    link = StringVar('')
    link = txt_2.get()
    return link

def input_data_path():
    path = txt_1.get()      #"C:/SAVE_PATH"
    return path


def viewing_info():
    list_phon.insert(f'Наименование загружаемого файла:  {vid.title}; \n \
                       Просмотры: {vid.views}; \n \
                       Длина трека: {vid.length} секунд; \n \
                       Описание: {vid.description}; \n \
                       Рейтинги: {vid.rating}.')
    return

def loading():
    vid_download = vid.streams.get_by_itag('17')
    vid_download.download(path)
    return

# link = input('Введите ссылку на видео с Youtube: ')
# vid = YouTube(link)
# print('Наименование загружаемого файла: ', vid.title)
# print('Просмотры: ', vid.views)
# print('Длина трека: ', vid.length, 'секунд')
# print('Описание: ', vid.description)
# print('Рейтинги: ', vid.rating)
# vid_download = vid.streams.get_by_itag('17')
# vid_download.download("C:/SAVE_PATH")
# print('Скачивание завешено!')

#-----------------------------------------------------------------------------
window = Tk()
window.title("Загрузчик видео и аудио с YouTube")
window.geometry('600x500')
txt_2 = StringVar()

args1 = {'bg' : "snow3", 'fg' : "navy", 'font' : ("Arial Bold", 12), 'activebackground' : "green"}
args2 = {'fg' : "navy", 'font' : ("Arial Bold", 12)}

lb_l = Label(window, text = 'Укажите путь к папке сохранения файла: ', **args2)                                     
lb_l.place(x = 10, y = 10)
txt_1 = Entry(window, width = 25, font = ("Arial Bold", 10))  
txt_1.place(x = 320, y = 10)
txt_1.bind('<Return>', input_data_path)

lb_2 = Label(window, text = 'Введите ссылку на видео с Youtube: ', **args2)                                     
lb_2.place(x = 10, y = 50)
txt_2 = Entry(window, width = 25, font = ("Arial Bold", 10))  
txt_2.place(x = 320, y = 50)
x = txt_2.bind('<Return>', txt_2.get())

list_phon = Listbox(width = 90, height = 15, selectmode = EXTENDED) 
list_phon.place(x = 10, y = 100)
scroll_y = Scrollbar(orient="vertical", command=list_phon.yview)
scroll_y.place(x = 570, y = 150)
list_phon.config(yscrollcommand = scroll_y.set)
scroll_x = Scrollbar(orient="horizontal", command=list_phon.xview)
scroll_x.place(x = 100, y = 350)
list_phon.config(xscrollcommand = scroll_x.set)

btn = Button(window, width = 25, text = "Записать путь", **args1, command = input_data_path)
btn.place(x = 400, y = 380)
btn = Button(window, width = 25, text = "Записать ссылку", **args1, command = input_data_link)
btn.place(x = 400, y = 420)

vid = YouTube(x)
path = input_data_path()

print(f'vid = {vid}')
print(f'path = {path}')

btn = Button(window, width = 25, text = "Посмотреть информацию", **args1, command = viewing_info)
btn.place(x = 180, y = 380)
btn = Button(window, width = 25, text = "Загрузить", **args1, command = loading)
btn.place(x = 180, y = 420)

window.mainloop()