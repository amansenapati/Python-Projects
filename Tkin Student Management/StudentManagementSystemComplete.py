#StudentManagementSystemComplete.py
import pandas as pandas


def addstudent():
    def submitadd():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addedtime=time.strftime("%H:%M:%S")
        addeddate=time.strftime("%d/%m/%Y")
        try:
            strr='insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res=messagebox.askyesnocancel('Notifications','Id {} Name {} Added successfully.. and want to clean the form'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')

        except:
            messagebox.showerror('Notifications','Id Already Exist try another id...',parent=addroot)
        strr='select * from studentdata'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenmttable.insert('',END,values=vv)

    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.iconbitmap('stu.ico')
    addroot.resizable(False,False)
    #add student label
    idlabel=Label(addroot,text="Enter Id : ",bg='gold2',font=('calibiri',20,'bold'),relief=GROOVE,bd=4,width=12,anchor=W)
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot, text="Enter Name : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                    width=12, anchor=W)
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text="Enter Mobile : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                    width=12, anchor=W)
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text="Enter Email : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                    width=12, anchor=W)
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text="Enter Address : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                    width=12, anchor=W)
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text="Enter Gender : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                    width=12, anchor=W)
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text="Enter D.O.B : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                    width=12, anchor=W)
    doblabel.place(x=10, y=370)

    #add button
    submitbtn=Button(addroot,text='Submit',font=('calibiri',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',
                     command=submitadd)
    submitbtn.place(x=150,y=420)

    #add student entry
    idval=StringVar()
    nameval=StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry=Entry(addroot,font=('calbiri',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=235,y=10)

    nameentry=Entry(addroot,font=('calbiri',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=235,y=70)

    mobileentry=Entry(addroot,font=('calbiri',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=235,y=130)

    emailentry=Entry(addroot,font=('calbiri',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=235,y=190)

    addressentry=Entry(addroot,font=('calbiri',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=235,y=250)

    genderentry=Entry(addroot,font=('calbiri',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=235,y=310)

    dobentry=Entry(addroot,font=('calbiri',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=235,y=370)

    addroot.mainloop()

def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if(id!=''):
            strr='select * from studentdata where id=%s'
            mycursor.execute(strr,(id))
            datas=mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (name != ''):
            strr = 'select * from studentdata where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (mobile != ''):
            strr = 'select * from studentdata where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)

        elif (email != ''):
            strr = 'select * from studentdata where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)

        elif (address != ''):
            strr = 'select * from studentdata where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)

        elif (gender != ''):
            strr = 'select * from studentdata where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)

        elif (dob != ''):
            strr = 'select * from studentdata where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)

        elif (addeddate != ''):
            strr = 'select * from studentdata where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='firebrick1')
    searchroot.iconbitmap('stu.ico')
    searchroot.resizable(False, False)
    # add student label
    idlabel = Label(searchroot,  text="Enter Id : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                    width=12, anchor=W)
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text="Enter Name : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                      width=12, anchor=W)
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text="Enter Mobile : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                        width=12, anchor=W)
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text="Enter Email : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                       width=12, anchor=W)
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text="Enter Address : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE,
                         bd=4,
                         width=12, anchor=W)
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text="Enter Gender : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                        width=12, anchor=W)
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text="Enter D.O.B : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                     width=12, anchor=W)
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text="Enter Date : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                     width=12, anchor=W)
    datelabel.place(x=10, y=430)

    # add button
    submitbtn = Button(searchroot, text='Search', font=('calibiri', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white', bg='red',command=search)
    submitbtn.place(x=150, y=480)

    # add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval=StringVar()

    identry = Entry(searchroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=235, y=10)

    nameentry = Entry(searchroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=235, y=70)

    mobileentry = Entry(searchroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=235, y=130)

    emailentry = Entry(searchroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=235, y=190)

    addressentry = Entry(searchroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=235, y=250)

    genderentry = Entry(searchroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=235, y=310)

    dobentry = Entry(searchroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=235, y=370)

    dateentry = Entry(searchroot, font=('calbiri', 15, 'bold'), bd=5,textvariable=dateval)
    dateentry.place(x=235, y=430)

    searchroot.mainloop()

def deletestudent():
    cc=studenmttable.focus()
    content=studenmttable.item(cc)
    pp=content['values'][0]
    strr='delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} seleted successfully...'.format(pp))
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenmttable.delete(*studenmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenmttable.insert('', END, values=vv)


def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date=dateval.get()
        tme=timeval.get()

        strr='update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,tme,id))
        con.commit()
        messagebox.showinfo('Notification','Id {} deleted successfully...'.format(id),parent=updateroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenmttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x590+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='firebrick1')
    updateroot.iconbitmap('stu.ico')
    updateroot.resizable(False, False)
    # add student label
    idlabel = Label(updateroot, text="Enter Id : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                    width=12, anchor=W)
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text="Enter Name : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                      width=12, anchor=W)
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text="Enter Mobile : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                        width=12, anchor=W)
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text="Enter Email : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                       width=12, anchor=W)
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text="Enter Address : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE,
                         bd=4,
                         width=12, anchor=W)
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text="Enter Gender : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                        width=12, anchor=W)
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text="Enter D.O.B : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                     width=12, anchor=W)
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text="Enter Date : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                     width=12, anchor=W)
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text="Enter Time : ", bg='gold2', font=('calibiri', 20, 'bold'), relief=GROOVE, bd=4,
                      width=12, anchor=W)
    timelabel.place(x=10, y=490)

    # add button
    updatebtn = Button(updateroot, text='Update', font=('calibiri', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white', bg='red',command=update)
    updatebtn.place(x=150, y=540)

    # add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval=StringVar()
    timeval=StringVar()

    identry = Entry(updateroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=235, y=10)

    nameentry = Entry(updateroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=235, y=70)

    mobileentry = Entry(updateroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=235, y=130)

    emailentry = Entry(updateroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=235, y=190)

    addressentry = Entry(updateroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=235, y=250)

    genderentry = Entry(updateroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=235, y=310)

    dobentry = Entry(updateroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=235, y=370)

    dateentry = Entry(updateroot, font=('calbiri', 15, 'bold'), bd=5,textvariable=dateval)
    dateentry.place(x=235, y=430)

    timeentry = Entry(updateroot, font=('calbiri', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=235, y=490)

    cc=studenmttable.focus()
    content=studenmttable.item(cc)
    pp=content['values']
    if(len(pp)!=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()



def showstudent():
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenmttable.delete(*studenmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenmttable.insert('', END, values=vv)

def exportstudent():
    ff=filedialog. asksaveasfilename()
    gg=studenmttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=studenmttable.item(i)
        pp=content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths=r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification', 'Student data is saved {}'.format(paths))

def exitstudent():
    res=messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res==True):
        root.destroy()


#Connect db
def Connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()
        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr='create database studentmanagementsystem'
            mycursor.execute(strr)
            strr='use studentmanagementsystem'
            mycursor.execute(strr)
            strr='create table studentdata(id int primary key,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            #strr = 'alter table studentdata modify column id int primary key'
            #mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and Now you are connected to the database...',parent=dbroot)

        except:
            strr='use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database...', parent=dbroot)
        dbroot.destroy()


    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='light blue')
    #Connect db label
    hostlabel=Label(dbroot,text="Enter Host :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,bd=5,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text="Enter User :", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, bd=5, width=13,
                    anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password :", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, bd=5, width=13,
                    anchor='w')
    passwordlabel.place(x=10, y=130)

    #Connect db entry
    hostval=StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    #Connect db button
    submitbutton=Button(dbroot,text='Submit',font=('calbiri',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.iconbitmap('data.ico')

#tick
def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d/%m/%Y")
    clock.config(text="Date :"+date_string +"\n"+"Time :"+time_string)
    clock.after(200,tick)

#Intro Slider
def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count=0
        text=''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
        count+=1
    SliderLabel.after(200,IntroLabelTick)


import time
import pandas
from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter import ttk
from tkinter.ttk import Treeview

import pymysql

root=Tk()

root.title("Student Management System")
root.config(bg='purple')
root.geometry('1174x695+200+50')
root.iconbitmap('stu.ico')
root.resizable(False,False)

#frames
DataEntryFrame= Frame(root,bg='white',relief=GROOVE ,bd=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

#datentry frame intro

frontLabel=Label(DataEntryFrame,text="-------------Student-------------",width=25,font=('calibiri',25,'bold'))
frontLabel.pack(side=TOP,expand=True)

addbtn=Button(DataEntryFrame,text='1. Add Student',width=20,font=('calibiri',20,'bold'),bd=5,bg='skyblue',activebackground='blue',relief=RIDGE,
              activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryFrame,text='2. Search Student',width=20,font=('calibiri',20,'bold'),bd=5,bg='skyblue',activebackground='blue',relief=RIDGE,
              activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEntryFrame,text='3. Delete Student',width=20,font=('calibiri',20,'bold'),bd=5,bg='skyblue',activebackground='blue',relief=RIDGE,
              activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame,text='4. Update Student',width=20,font=('calibiri',20,'bold'),bd=5,bg='skyblue',activebackground='blue',relief=RIDGE,
              activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn=Button(DataEntryFrame,text='5. Show All',width=20,font=('calibiri',20,'bold'),bd=5,bg='skyblue',activebackground='blue',relief=RIDGE,
              activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryFrame,text='6. Export Data',width=20,font=('calibiri',20,'bold'),bd=5,bg='skyblue',activebackground='blue',relief=RIDGE,
              activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame,text='7. Exit',width=20,font=('calibiri',20,'bold'),bd=5,bg='skyblue',activebackground='blue',relief=RIDGE,
              activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)


#Show Data frame
ShowDataFrame=Frame(root,bg='white',relief=GROOVE,bd=5)
ShowDataFrame.place(x=550,y=80,width=500,height=600)

#show data frame
style=ttk.Style()
style.configure('Treeview.Heading',font=('calibiri',15,'bold'),foreground='black')
style.configure('Treeview',font=('times',12,'bold'),foreground='black',background='white')
scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
studenmttable=Treeview(ShowDataFrame,column=('Id','Name','Mobile No.','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                       yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
studenmttable.heading('Id',text='Id')
studenmttable.heading('Name',text='Name')
studenmttable.heading('Mobile No.',text='Mobile No.')
studenmttable.heading('Email',text='Email')
studenmttable.heading('Address',text='Address')
studenmttable.heading('Gender',text='Gender')
studenmttable.heading('D.O.B',text='D.O.B')
studenmttable.heading('Added Date',text='Added Date')
studenmttable.heading('Added Time',text='Added Time')
studenmttable['show']='headings'
studenmttable.column('Id',width=100)
studenmttable.column('Name',width=200)
studenmttable.column('Mobile No.',width=200)
studenmttable.column('Email',width=300)
studenmttable.column('Address',width=200)
studenmttable.column('Gender',width=100)
studenmttable.column('D.O.B',width=150)
studenmttable.column('Added Date',width=150)
studenmttable.column('Added Time',width=150)

scroll_x.config(command=studenmttable.xview)
scroll_y.config(command=studenmttable.yview)
studenmttable.pack(fill=BOTH,expand=1)
#slider
ss="Welcome To Student Management System"
count=0
text=''
SliderLabel=Label(root,text=ss,font=('calibiri',25,'bold'),relief=RIDGE,bd=5,width=35,bg='cyan',fg='purple')
SliderLabel.place(x=260,y=0)
IntroLabelTick()

#clock
clock=Label(root,font=('calibiri',15,'bold'),relief=RIDGE,bd=5,bg='lawn green')
clock.place(x=0,y=0)
tick()

#ConnectDatabasebutton
connectbutton=Button(root,text="Connect To Database",width=21,height=3,font=('calibiri',10,'bold'),relief=RIDGE,bd=5,bg='lawn green',
                     activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=990,y=0)

root.mainloop()
