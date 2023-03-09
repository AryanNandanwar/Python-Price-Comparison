from tkinter import *
from tkinter import ttk,messagebox
import webbrowser
from bs4 import BeautifulSoup
import urllib
from urllib import request





log = Tk()
log.title('Login Page')
log.geometry('500x400')

Email = Label(log,text='Email',font=('Times New Roman',12,'bold'))
Email.place(x=25,y=50)
Email_Entry = Entry(log,width=45,font=('arial',10),bd=4)
Email_Entry.place(x=110,y=50)

PW = Label(log,text='Passsword',font=('Times New Roman',12,'bold'))
PW.place(x=25,y=110)
PW_Entry = Entry(log,width=45,font=('arial',10),bd=4,show='*')
PW_Entry.place(x=110,y=110)

Email_btn = Button(log,text='Enter',bg='lightgrey',fg='black',activebackground='lightgrey',bd=0)
Email_btn.place(x=450,y=50)

PW_btn = Button(log,text='Enter',bg='lightgrey',fg='black',activebackground='lightgrey',bd=0)
PW_btn.place(x=450,y=110)

PW_show = Button(log,text='Show Pass',bg='lightgrey',fg='black',activebackground='lightgrey',bd=0)
PW_show.place(x=120,y=150,height=20,width=60)


log.mainloop()