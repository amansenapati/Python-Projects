#calc.py
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math

win=tk.Tk()

#screen
win.title('Calculator')
win.resizable(width=False,height=False)
win.geometry('480x588')
win.configure(bg='lightgrey')
win.iconbitmap('calc.ico')

#func menu
def hel():
    top=Toplevel()

    top.title("View Help")
    top.resizable(width=False,height=False)
    top.geometry('320x300')
    top.configure(bg='lightgrey')
    top.iconbitmap('que.ico')
    
    l1=Label(top,text='Help',font=('Helvetica',20,'bold'),bg='lightgrey',fg='yellow')
    l1.pack(pady=10)
    l2=Label(top,text='Functions :- ( + - x / % sqrt )',fg='green',font=(10))
    l2.pack()
    l3=Label(top,text='+ : used to add the number')
    l3.place(x=60,y=100)
    l4=Label(top,text='- : used to subtract the number')
    l4.place(x=60,y=120)
    l5=Label(top,text='x : used to multiply the number')
    l5.place(x=60,y=140)
    l6=Label(top,text='/ : used to divide the number')
    l6.place(x=60,y=160)
    l7=Label(top,text='% : used to find the remainder of number')
    l7.place(x=60,y=180)
    l8=Label(top,text='sqrt : used to find the square root of number')
    l8.place(x=60,y=200)

    top.mainloop()

#features will be added in future for scientific calculator
def sci():
    pass

def ext():
    win.destroy()

def about():
    top1=Toplevel()

    top1.title("About Calculator")
    top1.resizable(width=False,height=False)
    top1.geometry('300x300')
    top1.configure(bg='lightgrey')
    top1.iconbitmap('abt.ico')
    
    l1=Label(top1,text='Calculator',font=('Helvetica',20,'bold'),bg='lightgrey',fg='blue')
    l1.pack(pady=10)
    l2=Label(top1,text='Version 1.0',fg='red')
    l2.pack()
    l3=Label(top1,text='This calculator and its user interface are protected')
    l3.pack()
    l4=Label(top1,text='by trademark and other pending or existing intellectual')
    l4.pack()
    l5=Label(top1,text='property rights only in India.')
    l5.pack()
    l6=Label(top1,text='Copyright (c) 2001-2021 @aman')
    l6.place(x=70,y=250)
    l7=Label(top1,text='All Rights Reserved.')
    l7.place(x=105,y=270)

    top1.mainloop()

#menu
main_menu=Menu(win)
win.config(menu=main_menu)

file_menu=Menu(main_menu)
main_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_cascade(label='Exit',command=ext)

view_menu=Menu(main_menu)
main_menu.add_cascade(label='View',menu=view_menu)
view_menu.add_cascade(label='Scientific',command=sci)

help_menu=Menu(main_menu)
main_menu.add_cascade(label='Help',menu=help_menu)
help_menu.add_cascade(label='View Help',command=hel)
help_menu.add_separator()
help_menu.add_cascade(label='About Calculator',command=about)


#func logic
exp=''
def backclear():
    global exp
    l=list(exp)
    l.pop()
    exp=''.join(l)
    var.set(exp)

def clear():
    global exp
    exp=''
    var.set(exp)

def sqrt():
    global exp
    exp=math.sqrt(int(exp))
    var.set(exp)
    
def press(n):
    global exp
    exp=exp+n
    var.set(exp)

def ans():
    global exp
    exp=eval(exp)
    var.set(exp)
    

#box
var=StringVar()
e=Entry(win,font=('Helvetica',20,'bold'),bg='black',fg='white',
        width=28,justify=RIGHT,bd=25,textvariable=var)
e.grid(row=0,column=0,columnspan=1,padx=4,pady=4)

#button

#first line
c=Button(win,text='C',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='black',fg='white',bd=4,command=clear)
c.place(x=10,y=90)

ce=Button(win,text='\U00002B05',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='black',fg='white',bd=4,command=backclear)
ce.place(x=130,y=90)

sqr=Button(win,text='Sqrt',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='black',fg='white',bd=4,command=sqrt)
sqr.place(x=250,y=90)

op1=Button(win,text='+',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='black',fg='white',bd=4,command=lambda:press('+'))
op1.place(x=370,y=90)

#second line
n7=Button(win,text='7',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='white',fg='black',bd=4,command=lambda:press('7'))
n7.place(x=10,y=185)

n8=Button(win,text='8',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='white',fg='black',bd=4,command=lambda:press('8'))
n8.place(x=130,y=185)

n9=Button(win,text='9',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='white',fg='black',bd=4,command=lambda:press('9'))
n9.place(x=250,y=185)

op2=Button(win,text='-',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='black',fg='white',bd=4,command=lambda:press('-'))
op2.place(x=370,y=185)

#third line
n4=Button(win,text='4',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='white',fg='black',bd=4,command=lambda:press('4'))
n4.place(x=10,y=280)

n5=Button(win,text='5',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='white',fg='black',bd=4,command=lambda:press('5'))
n5.place(x=130,y=280)

n6=Button(win,text='6',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='white',fg='black',bd=4,command=lambda:press('6'))
n6.place(x=250,y=280)

op3=Button(win,text='x',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='black',fg='white',bd=4,command=lambda:press('*'))
op3.place(x=370,y=280)

#fourth line
n1=Button(win,text='1',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='white',fg='black',bd=4,command=lambda:press('1'))
n1.place(x=10,y=375)

n2=Button(win,text='2',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='white',fg='black',bd=4,command=lambda:press('2'))
n2.place(x=130,y=375)

n3=Button(win,text='3',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='white',fg='black',bd=4,command=lambda:press('3'))
n3.place(x=250,y=375)

op4=Button(win,text='/',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='black',fg='white',bd=4,command=lambda:press('/'))
op4.place(x=370,y=375)

#fifth line
n0=Button(win,text='0',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='white',fg='black',bd=4,command=lambda:press('0'))
n0.place(x=10,y=470)

dot=Button(win,text='.',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='black',fg='white',bd=4,command=lambda:press('.'))
dot.place(x=130,y=470)

op5=Button(win,text='%',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='black',fg='white',bd=4,command=lambda:press('%'))
op5.place(x=250,y=470)

eq=Button(win,text='=',width=5,height=2,font=('Helvetica',20,'bold')
          ,bg='black',fg='white',bd=4,command=ans)
eq.place(x=370,y=470)

win.mainloop()
