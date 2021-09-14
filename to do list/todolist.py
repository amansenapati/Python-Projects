#todolist.py
import tkinter as tk
from tkinter import *

win=tk.Tk()

#screen
win.title('To Do List')
win.resizable(width=False,height=False)
win.geometry('400x450')
win.iconbitmap('todo.ico')

#scroll
scr=Scrollbar(win)
scr.pack(side=RIGHT,fill=Y)

#func

def insert():
    v=var.get()
    tols.insert(END,v)
    var.set('')

def delete():
    tols.delete(ANCHOR)

l=Label(win,text='To Do List',font=('Forte',25),fg='lightblue')
l.pack()

tols=Listbox(win,width=28,height=15,yscrollcommand=Y)
tols.insert(END,'Apple')
tols.insert(END,'Banana')
tols.insert(END,'Cherry')
tols.insert(END,'Mango')
tols.pack(pady=10)

scr.config(command=tols.yview)

var=StringVar()
e=Entry(win,bd=3,width=15,textvariable=var)
e.place(x=115,y=310)

ins=Button(win,text='Add To List',width=8,height=1,command=insert)
ins.place(x=115,y=340)

dele=Button(win,text='Delete',width=8,height=1,command=delete)
dele.place(x=220,y=340)


win.mainloop()
