from tkinter import *
import csv
import datetime
import glob
import os
import pandas as pd
from tkinter.ttk import *
window = Tk()
window.geometry('850x200')
df = pd.read_csv('zemlepolzovateli.csv',error_bad_lines=False,engine='python',sep=';',header=0,encoding='cp1251')

#========================================

lbl = Label(window, text="Представитель")
lbl.grid(column=0, row=1)

combo1 = Combobox(window,width=60)
combo1['values']= [0]
combo1.current(0) #set the selected item index
combo1.grid(column=1, row=1)

#========================================

lb2 = Label(window, text="Орг.")
lb2.grid(column=0, row=0)

combo = Combobox(window,width=60)
combo['values']= sorted(df.full_name.unique().tolist())
combo.current(0) #set the selected item index
combo.grid(column=1, row=0)

def clicked():
    print(combo.get())
    print(df[df.full_name == combo.get()].sgls_predstavitel.tolist())
    combo1.set('')
    combo1['values']= df[df.full_name == combo.get()].sgls_predstavitel.tolist()
    combo1.current(0)

btn_zm = Button(window, text="Список работников", command=clicked)
btn_zm.grid(column=2, row=0)
#========================================
lb3 = Label(window, text="Текущая дата:",anchor='w')
lb3.grid(column=0, row=2)

lb4 = Label(window, text=datetime.datetime.now().strftime("%d.%m.%Y"))
lb4.grid(column=1, row=2)
#========================================
lb5 = Label(window, text="Номер согласования:")
lb5.grid(column=0, row=3)

list_of_files = sorted(glob.glob("Согласование*.docx"))
print(list_of_files[-1])
#latest_file = max(list_of_files, key=os.path.getctime)
latest_file = list_of_files[-1]
new_sgls_index = int(latest_file.split(" ")[6])+1
print(new_sgls_index)
lb6 = Label(window, text=new_sgls_index)
lb6.grid(column=1, row=3)
#=======================================
lb7 = Label(window, text="Название проекта:")
lb7.grid(column=0, row=4)

txt = Entry(window,width=60)
txt.grid(column=1, row=4)
window.mainloop()
















