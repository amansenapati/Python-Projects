#pasgen.py
import tkinter as tk
from tkinter import *
import random as r
import pyperclip as py

win=tk.Tk()

#screen
win.title('PASSWORD GENERATOR')
win.configure(bg='white')
win.resizable(width=False,height=False)
win.geometry('400x400')
win.iconbitmap('pas.ico')

#fun
pas=""
def gen():
    global pas
    l='abcdefghijklmnopqrstuvwxyz'
    u='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n='1234567890'
    s='~!@#$%^&*()_+-={}[]|\:";\'<>?,./ '
    p=l+u+n+s
    for i in range(le.get()):
        pas=pas+r.choice(p)
        
    Entry.insert(e,0,pas)

def cpyclp():
    py.copy(pas)
    
#text
l1=Label(win,text='Password Generator',font=('forte',25),bg='white',fg='blue')
l1.pack()
l2=Label(win,text='Application',font=('forte',25),bg='white',fg='blue')
l2.pack()
l3=Label(win,text='PASSWORD LENGTH',font=('arial',13,'bold'),bg='white')
l3.pack(pady=20)

#spinbox
le=IntVar()
s=Spinbox(win,from_=8, to_=32,width=15,bd=3,state='readonly',textvariable=le)
s.place(x=150,y=135)

#button
gb=Button(win,text='GENERATE PASSWORD',command=gen)
gb.place(x=135,y=170)

#entry
e=Entry(win,bd=3,width=25,fg='black')
e.place(x=125,y=220)

#button
cpb=Button(win,text='COPY TO CLIPBOARD',command=cpyclp)
cpb.place(x=135,y=250)

win.mainloop()
