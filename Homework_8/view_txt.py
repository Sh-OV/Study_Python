
from tkinter import *
import registration as reg



path_txt = 'Homework_8\Telephone_directory.txt'

def insert_list(name, end_s):
    if name.get() == '':
        list_phon.insert(END, '0')
    else:
        list_phon.insert(END, name.get())
    list_phon.insert(END, end_s)
    name.delete(0, END)

def add():
    list_phon.insert(END, "\n")
    insert_list(txt_1, "\n\n")
    insert_list(txt_2, "\n\n")
    insert_list(txt_3, "\n\n")
    insert_list(txt_4, "\n\n")
    insert_list(txt_5, "\n\n")
    insert_list(txt_6, "\n\n")
    insert_list(txt_7, "\n\n")
    insert_list(txt_8, "\n\n")
    insert_list(txt_9, "\n\n")
    insert_list(txt_10, "\n\n")
    list_phon.insert(END, '----------\n')
    return

def save():
    f = open(path_txt, 'r+', encoding='utf-8')
    f.writelines("".join(list_phon.get(0, END)))
    f.close()
    return

def delete():
    select = list(list_phon.curselection())
    select.reverse()
    for i in select:
        list_phon.delete(i - 1, i + 20)
    return 'Удален контакт'

window = Tk()
window.title("Телефонный справочник, txt")
window.geometry('1050x600')

args1 = {'bg' : "pale green", 'fg' : "blue", 'font' : ("Arial Bold", 12), 'activebackground' : "blue"}
args2 = {'fg' : "navy", 'font' : ("Arial Bold", 12)}
lc = reg.list_contact_parameters()

lb_l = Label(window, text = lc[0], **args2)                                     
lb_l.place(x = 10, y = 10)
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

btn = Button(window, width = 25, text = "Добавить абонента", **args1, command = add)
btn.place(x = 500, y = 450)
btn = Button(window, width = 25, text = "Удалить абонента", **args1, command = delete)
btn.place(x = 750, y = 450)
btn = Button(window, width = 25, text = "Сохранить", **args1, command = save)
btn.place(x = 500, y = 500)

list_phon = Listbox(width = 80, height = 25, selectmode = EXTENDED) 
list_phon.place(x = 500, y = 10)
scroll_y = Scrollbar(orient="vertical", command=list_phon.yview)
scroll_y.place(x = 1000, y = 50)
list_phon.config(yscrollcommand = scroll_y.set)
scroll_x = Scrollbar(orient="horizontal", command=list_phon.xview)
scroll_x.place(x = 550, y = 425)
list_phon.config(xscrollcommand = scroll_x.set)

f = open(path_txt, 'r+', encoding='utf-8')
for x in f:
    list_phon.insert(END,x)
print(x)
f.close()

window.mainloop()
