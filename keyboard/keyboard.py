#keyboard.py
from tkinter import *
import tkinter as tk
from tkinter import ttk

#func

exp=" "

def press(num):
    global exp
    exp=exp+str(num)
    var.set(exp)

def clear():
    global exp
    exp=" "
    var.set(exp)
    
def enter():
    global exp
    exp=" Next Line : "
    var.set(exp)

def tab():
    global exp
    exp=exp+"      "
    var.set(exp)

def spac():
    global exp
    exp=exp+" "
    var.set(exp)

win=tk.Tk()

#window size
win.title('On Screen Keyboard')
win.iconbitmap('key.ico')
win.geometry('1010x250')
win.maxsize(width=1010,height=250)
win.minsize(width=1010,height=250)


#entry box
var=StringVar()
e=Entry(win,bd=2,state='readonly',textvariable=var)
e.grid(rowspan=1,columnspan=100, ipadx=999,ipady=20)

#background color
win.configure(bg='light blue')

#button

#first line

q=Button(win,text='Q',command=lambda:press('Q'))
q.grid(row=1,column=0,ipadx=10,ipady=10)

w=Button(win,text='W',command=lambda:press('W'))
w.grid(row=1,column=1,ipadx=10,ipady=10)

e=Button(win,text='E',command=lambda:press('E'))
e.grid(row=1,column=2,ipadx=10,ipady=10)

r=Button(win,text='R',command=lambda:press('R'))
r.grid(row=1,column=3,ipadx=10,ipady=10)

t=Button(win,text='T',command=lambda:press('T'))
t.grid(row=1,column=4,ipadx=10,ipady=10)

y=Button(win,text='Y',command=lambda:press('Y'))
y.grid(row=1,column=5,ipadx=10,ipady=10)

u=Button(win,text='U',command=lambda:press('U'))
u.grid(row=1,column=6,ipadx=10,ipady=10)

i=Button(win,text='I',command=lambda:press('I'))
i.grid(row=1,column=7,ipadx=10,ipady=10)

o=Button(win,text='O',command=lambda:press('O'))
o.grid(row=1,column=8,ipadx=10,ipady=10)

p=Button(win,text='P',command=lambda:press('P'))
p.grid(row=1,column=9,ipadx=10,ipady=10)

br1=Button(win,text='{',command=lambda:press('}'))
br1.grid(row=1,column=10,ipadx=10,ipady=10)

br2=Button(win,text='}',command=lambda:press('}'))
br2.grid(row=1,column=11,ipadx=10,ipady=10)

sl=Button(win,text='\\',command=lambda:press('\\'))
sl.grid(row=1,column=12,ipadx=10,ipady=10)

eq=Button(win,text='=',command=lambda:press('='))
eq.grid(row=1,column=13,ipadx=10,ipady=10)

cle=Button(win,text='Clear',command=clear)
cle.grid(row=1,columnspan=75,ipadx=40,ipady=10)

#second line

a=Button(win,text='A',command=lambda:press('A'))
a.grid(row=2,column=0,ipadx=10,ipady=10)

s=Button(win,text='S',command=lambda:press('S'))
s.grid(row=2,column=1,ipadx=10,ipady=10)

d=Button(win,text='D',command=lambda:press('D'))
d.grid(row=2,column=2,ipadx=10,ipady=10)

f=Button(win,text='F',command=lambda:press('F'))
f.grid(row=2,column=3,ipadx=10,ipady=10)

g=Button(win,text='G',command=lambda:press('G'))
g.grid(row=2,column=4,ipadx=10,ipady=10)

h=Button(win,text='H',command=lambda:press('H'))
h.grid(row=2,column=5,ipadx=10,ipady=10)

j=Button(win,text='J',command=lambda:press('J'))
j.grid(row=2,column=6,ipadx=10,ipady=10)

k=Button(win,text='K',command=lambda:press('K'))
k.grid(row=2,column=7,ipadx=10,ipady=10)

l=Button(win,text='L',command=lambda:press('L'))
l.grid(row=2,column=8,ipadx=10,ipady=10)

dot1=Button(win,text=':',command=lambda:press(':'))
dot1.grid(row=2,column=9,ipadx=10,ipady=10)

com1=Button(win,text='"',command=lambda:press('"'))
com1.grid(row=2,column=10,ipadx=10,ipady=10)

ent=Button(win,text='Enter',command=enter)
ent.grid(row=2,columnspan=75,ipadx=40,ipady=10)

#third line

z=Button(win,text='Z',command=lambda:press('Z'))
z.grid(row=3,column=0,ipadx=10,ipady=10)

x=Button(win,text='X',command=lambda:press('X'))
x.grid(row=3,column=1,ipadx=10,ipady=10)

c=Button(win,text='C',command=lambda:press('C'))
c.grid(row=3,column=2,ipadx=10,ipady=10)

v=Button(win,text='V',command=lambda:press('V'))
v.grid(row=3,column=3,ipadx=10,ipady=10)

b=Button(win,text='B',command=lambda:press('B'))
b.grid(row=3,column=4,ipadx=10,ipady=10)

n=Button(win,text='N',command=lambda:press('N'))
n.grid(row=3,column=5,ipadx=10,ipady=10)

m=Button(win,text='M',command=lambda:press('M'))
m.grid(row=3,column=6,ipadx=10,ipady=10)

angbr1=Button(win,text='<',command=lambda:press('<'))
angbr1.grid(row=3,column=7,ipadx=10,ipady=10)

angbr2=Button(win,text='>',command=lambda:press('>'))
angbr2.grid(row=3,column=8,ipadx=10,ipady=10)

que=Button(win,text='?',command=lambda:press('?'))
que.grid(row=3,column=9,ipadx=10,ipady=10)

op1=Button(win,text='+',command=lambda:press('+'))
op1.grid(row=3,column=10,ipadx=10,ipady=10)

op2=Button(win,text='-',command=lambda:press('-'))
op2.grid(row=3,column=11,ipadx=10,ipady=10)

op3=Button(win,text='*',command=lambda:press('*'))
op3.grid(row=3,column=12,ipadx=10,ipady=10)

op4=Button(win,text='%',command=lambda:press('%'))
op4.grid(row=3,column=13,ipadx=10,ipady=10)

#fourth line

ta=Button(win,text='Tab',command=tab)
ta.grid(row=4,column=0,ipadx=20,ipady=10)

co=Button(win,text=',',command=lambda:press(','))
co.grid(row=4,column=1,ipadx=10,ipady=10)

dot2=Button(win,text='.',command=lambda:press('.'))
dot2.grid(row=4,column=2,ipadx=10,ipady=10)

sl1=Button(win,text='/',command=lambda:press('/'))
sl1.grid(row=4,column=3,ipadx=10,ipady=10)

n1=Button(win,text='1',command=lambda:press('1'))
n1.grid(row=4,column=4,ipadx=10,ipady=10)

n2=Button(win,text='2',command=lambda:press('2'))
n2.grid(row=4,column=5,ipadx=10,ipady=10)

n3=Button(win,text='3',command=lambda:press('3'))
n3.grid(row=4,column=6,ipadx=10,ipady=10)

n4=Button(win,text='4',command=lambda:press('4'))
n4.grid(row=4,column=7,ipadx=10,ipady=10)

n5=Button(win,text='5',command=lambda:press('5'))
n5.grid(row=4,column=8,ipadx=10,ipady=10)

n6=Button(win,text='6',command=lambda:press('6'))
n6.grid(row=4,column=9,ipadx=10,ipady=10)

n7=Button(win,text='7',command=lambda:press('7'))
n7.grid(row=4,column=10,ipadx=10,ipady=10)

n8=Button(win,text='8',command=lambda:press('8'))
n8.grid(row=4,column=11,ipadx=10,ipady=10)

n9=Button(win,text='9',command=lambda:press('9'))
n9.grid(row=4,column=12,ipadx=10,ipady=10)

n0=Button(win,text='0',command=lambda:press('0'))
n0.grid(row=4,column=13,ipadx=10,ipady=10)

sp=Button(win,text='Space',command=spac)
sp.grid(row=4,columnspan=75,ipadx=55,ipady=10)








































win.mainloop()
