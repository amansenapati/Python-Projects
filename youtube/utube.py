#utube.py
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox

win=tk.Tk()

#screen
win.title("Developed by @aman")
win.resizable(width=False,height=False)
win.geometry('500x300')
win.configure(bg='white')
win.iconbitmap('ut.ico')

#fun
def downld():
    if(link.get()==""):
        messagebox.showerror('Warning','Enter The Link')
    else:
        url=YouTube(str(link.get()))
        video=url.streams.first()
        video.download()
        messagebox.showinfo('Download','Download Completed')

#text
l1=Label(win,text="Youtube Video Downloader",font=('forte',25),fg='red')
l1.pack(pady=5)

img=PhotoImage(file='utube.png')
l2=Label(win,image=img)
l2.pack(pady=10)

l3=Label(win,text="Type Your Link Here:",font=('arial',15))
l3.pack(pady=5)

#entry
link=StringVar()
link_e=Entry(win,bd=3,width=65,textvariable=link)
link_e.pack(pady=10)

#button
b=Button(win,text="DOWNLOAD",width=10,bg='green',fg='yellow',command=downld)
b.pack()

win.mainloop()
