from tkinter import *
from tkinter import ttk,messagebox
import webbrowser
from bs4 import BeautifulSoup
import urllib
from urllib import request

sub = Tk()

sub.title('Subscription Page')
sub.geometry('500x400')

Name = Label(sub,text='Name',font=('Times New Roman',12,'bold'))
Name.place(x=25,y=50)
Name_Entry = Entry(sub,width=45,font=('arial',10),bd=4)
Name_Entry.place(x=110,y=50)

Contact_no = Label(sub,text='Contact No',font=('Times New Roman',12,'bold'))
Contact_no.place(x=25,y=110)
Contactno_Entry = Entry(sub,width=45,font=('arial',10),bd=4)
Contactno_Entry.place(x=110,y=110)

Email_id = Label(sub,text='Email',font=('Times New Roman',12,'bold'))
Email_id.place(x=25,y=160)
Emailid_Entry = Entry(sub,width=45,font=('arial',10),bd=4)
Emailid_Entry.place(x=110,y=170)

password = Label(sub,text='Passsword',font=('Times New Roman',12,'bold'))
password.place(x=25,y=220)
password_Entry = Entry(sub,width=45,font=('arial',10),bd=4,show='*')
password_Entry.place(x=110,y=230)

Enter_btn = Button(sub,text='Enter Details',bg='lightgrey',fg='black',activebackground='lightgrey',bd=0)
Enter_btn.place(x=300,y=270)

showpass_btn = Button(sub,text='Show pass',bg='lightgrey',fg='black',activebackground='lightgrey',bd=0)
showpass_btn.place(x=120,y=270)



sub.mainloop()
