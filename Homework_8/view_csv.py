from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter import Listbox
from tkinter import Entry
import registration as reg
import datetime

path_csv = 'Homework_8\Telephone_directory_csv'

def add_subscriber(index = END):
    list_phon.insert(index, txt_1.get() + ',' + txt_2.get() + ',' + txt_3.get() + ',' + txt_4.get() + ',' \
                    + txt_5.get() + ',' + txt_6.get() + ',' + txt_7.get() + ',' + txt_8.get() + ',' \
                    + txt_9.get() + ',' + txt_10.get() + ',' + '\n')
    save()
    del_window_text()
    return

def del_window_text():
    x = txt_1.get()
    txt_1.delete(0, END)
    txt_2.delete(0, END)
    txt_3.delete(0, END)
    txt_4.delete(0, END)
    txt_5.delete(0, END)
    txt_6.delete(0, END)
    txt_7.delete(0, END)
    txt_8.delete(0, END)
    txt_9.delete(0, END)
    txt_10.delete(0, END)
    return
    

def save(arg = 'r+'):
    f = open(path_csv, arg, encoding='utf-8')
    f.writelines("".join(list_phon.get(0, END)))
    f.close()
    return

def delete_subscriber(select = END):
    select = list(list_phon.curselection())
    select.reverse()
    for i in select:
        list_phon.delete(i)
    save('w')
    return

def save_changes():
    select = list(list_phon.curselection())
    add_subscriber(select)
    delete_subscriber(select)
    

def changes_data_note():
    select = list(list_phon.curselection())
    chang_str = list_phon.get(select).split(',')
    print(chang_str)
    txt_1.insert(0, chang_str[0])
    txt_2.insert(1, chang_str[1])
    txt_3.insert(2, chang_str[2])
    txt_4.insert(3, chang_str[3])
    txt_5.insert(4, chang_str[4])
    txt_6.insert(5, chang_str[5])
    txt_7.insert(6, chang_str[6])
    txt_8.insert(7, chang_str[7])
    txt_9.insert(8, chang_str[8])
    txt_10.insert(9, chang_str[9])
    return 


window = Tk()
window.title("Телефонный справочник, csv")
window.geometry('1500x600')

args1 = {'bg' : "pale green", 'fg' : "blue", 'font' : ("Arial Bold", 12), 'activebackground' : "green"}
args2 = {'fg' : "navy", 'font' : ("Arial Bold", 12)}
lc = reg.list_contact_parameters()

lb_l = Label(window, text = lc[0], **args2).place(x = 10, y = 10)
txt_1 = Entry(window, width = 25, font = ("Arial Bold", 12))                                           
txt_1.place(x = 250, y = 10)
lb_2 = Label(window, text = lc[1], **args2)                                     
lb_2.place(x = 10, y = 50)
txt_2 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_2.place(x = 250, y = 50)
lb_3 = Label(window, text = lc[2], **args2)                                     
lb_3.place(x = 10, y = 90)
txt_3 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_3.place(x = 250, y = 90)
lb_4 = Label(window, text = lc[3], **args2)                                     
lb_4.place(x = 10, y = 130)
txt_4 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_4.place(x = 250, y = 130)
lb_5 = Label(window, text = lc[4], **args2)                                     
lb_5.place(x = 10, y = 170)
txt_5 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_5.place(x = 250, y = 170)
lb_6 = Label(window, text = lc[5], **args2)                                     
lb_6.place(x = 10, y = 210)
txt_6 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_6.place(x = 250, y = 210)    
lb_7 = Label(window, text = lc[6], **args2)                                     
lb_7.place(x = 10, y = 250)
txt_7 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_7.place(x = 250, y = 250)
lb_8 = Label(window, text = lc[7], **args2)                                     
lb_8.place(x = 10, y = 290)
txt_8 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_8.place(x = 250, y = 290)
lb_9 = Label(window, text = lc[8], **args2)                                     
lb_9.place(x = 10, y = 330)
txt_9 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_9.place(x = 250, y = 330)
lb_10 = Label(window, text = lc[9], **args2)                                     
lb_10.place(x = 10, y = 370)
txt_10 = Entry(window, width = 25, font = ("Arial Bold", 12))  
txt_10.place(x = 250, y = 370)

btn = Button(window, width = 25, text = "Добавить абонента", **args1, command = add_subscriber)
btn.place(x = 600, y = 450)
btn = Button(window, width = 25, text = "Удалить абонента", **args1, command = delete_subscriber)
btn.place(x = 900, y = 450)
btn = Button(window, width = 25, text = "Изменить", **args1, command = changes_data_note)
btn.place(x = 600, y = 500)
btn = Button(window, width = 25, text = "Сохранить изменение", **args1, command = save_changes)
btn.place(x = 900, y = 500)


list_phon = Listbox(width = 120, height = 25, selectmode = EXTENDED) 
list_phon.place(x = 500, y = 10)
scroll_y = Scrollbar(orient="vertical", command=list_phon.yview)
scroll_y.place(x = 1235, y = 50)
list_phon.config(yscrollcommand = scroll_y.set)
scroll_x = Scrollbar(orient="horizontal", command=list_phon.xview)
scroll_x.place(x = 550, y = 425)
list_phon.config(xscrollcommand = scroll_x.set)

f = open(path_csv, 'r+', encoding='utf-8')
for x in f:
    list_phon.insert(END,x)
f.close()

window.mainloop()
