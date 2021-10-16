from tkinter import *
import os, shelve

inn_checked='NOK'
site_checked='NOK'
model_percantage='85%'
data = None


def inn_search():
    global data
    # Change to Toplevel (a popup) instead of a new Tk instance
    root.title('Проверка благотворительных организаций')
    Label(root, text = 'Введите ИНН организации').grid(sticky = W, columnspan = 2)
    data = Text(root, width = 55, height = 2, wrap = WORD)
    data.grid(sticky = W, columnspan = 2)
    Button(root, text = 'Submit', command = check_data).grid(row = 10, column = 0, sticky = W + E)
    Button(root, text = 'Cancel', command = root.destroy).grid(row = 10, column = 1, sticky = W + E)
def name_search():
    global data
    root.title('Проверка благотворительных организаций')
    Label(root, text = 'Введите Название организации').grid(sticky = W, columnspan = 2)
    data = Text(root, width = 55, height = 2, wrap = WORD)
    data.grid(sticky = W, columnspan = 2)
    Button(root, text = 'Submit', command = check_data).grid(row = 10, column = 0, sticky = W + E)
    Button(root, text = 'Cancel', command = root.destroy).grid(row = 10, column = 1, sticky = W + E)
def data_window_feedback():
    global data
    root.title('Результаты проверки:')
    Label(root, text='Проверка ИНН').grid(sticky=W, columnspan=2)
    Label(root, text=inn_checked).grid(sticky=W, columnspan=2)
    Label(root, text='Проверка сайта').grid(sticky=W, columnspan=3)
    Label(root, text=site_checked).grid(sticky=W, columnspan=3)
    Label(root, text='Благотворительный фонд соответствует требованиям на ').grid(sticky=W, columnspan=4)
    Label(root, text=model_percantage).grid(sticky=W, columnspan=4)

def check_data():
    global data
    global var
    var = (data.get(1.0, END))
    print(var)
    if data.get(1.0, END).strip() == '':
       print('Nothing Entered')
    else:
        data_window_feedback()
    return var

def rerun():
    root.destroy()
    start()



def start():
    global root
    root = Tk()
    root.title("Проверка благотворительных фондов")
    inflam = StringVar()  # move inflam init to a broader scope so that the buttons don't but
    inflam.set('n')    # initialize it as 'n'
    root.title('')
    root.geometry('480x500')
    Button(root, text = 'Проверка по ИНН', command = inn_search).grid(row = 1, column = 0, sticky = W)
    Button(root, text = 'Проверка по названию', command = name_search).grid(row = 2, column = 0, sticky = W)
    Button(root, text = 'Новый запрос', command = rerun,bg="blue", fg="white").grid(row = 1, column = 1, sticky = W)

    root.mainloop()

start()
