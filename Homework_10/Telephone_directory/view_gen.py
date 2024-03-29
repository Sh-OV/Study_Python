from cProfile import label
from tkinter import *
import logger as lg

# --------------------------------------------------------------------
logger = lg.get_logger(__name__)

def process(msg):
    logger.info("Перед процессом")
    print(msg)
    logger.info("После процесса")
# ---------------------------------------------------------------------


def f_csv():
    wind().destroy()
    import view_csv as vc
      
def f_txt():
    wind().destroy()
    import view_txt as vt
 
 
def wind():    
    window_one = Tk()
    window_one.title("ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    window_one.geometry('420x200')

    args1 = {'bg' : "pale green", 'fg' : "blue", 'font' : ("Arial Bold", 12), 'activebackground' : "white"}
    args2 = {'fg' : "navy", 'font' : ("Arial Bold", 12)}

    lb_l = Label(window_one, text = 'Выберите формат файла, с которым будете работать: ', **args2)                                     
    lb_l.grid(row = 0, column = 0)

    btn = Button(window_one, width = 25, text = "file_csv", **args1, command = f_csv)
    btn.grid(row = 1, column = 0)
    btn = Button(window_one, width = 25, text = "file_txt", **args1, command = f_txt)
    btn.grid(row = 2, column = 0)

    window_one.mainloop()

wind()