from tkinter import *
from tkinter import ttk,messagebox
import webbrowser
from bs4 import BeautifulSoup





def click_amazon():
    webbrowser.open('https://www.amazon.com/')

def click_flipkart():
    webbrowser.open('https://www.flipkart.com/')

def click_croma():
    webbrowser.open('https://www.croma.com/')

def click_reliance():
    webbrowser.open('https://www.reliancedigital.in/')

def click_vijay():
    webbrowser.open('https://www.vijaysales.com/')











win = Tk()
win.geometry("1000x2000")
win.title("India's Most Efficient Price Comparison System")
win.config(bg = 'white')
name_label = Label(win, text = "CompareBapu",
                   font=("Helvetica",20,"bold"),fg="red",bg="white")

name_label.place(x = 275,y=50,height = 50, width = 200)
questionField=Entry(win,width=45,font=('arial',14,),bd=3,relief=SUNKEN)
questionField.place(x = 500,y = 50,height= 50 )


micImage=PhotoImage(file='C:/Users/admin/finalmic.png')
resized_mic = micImage.subsample(12, 12)

micButTon=Button(win,image=resized_mic,bg='white',bd=0,cursor='hand2',activebackground='lightgrey'
                 )
micButTon.place(x = 965,y = 50)

searchImage = PhotoImage(file="C:/Users/admin/search.png")
resized_search = searchImage.subsample(13, 13)

searchButTon=Button(win,image=resized_search,bg='white',bd=0,cursor='hand2',activebackground='lightgrey'
                 )
searchButTon.place(x = 1020,y = 50)

amazon_img = PhotoImage(file="C:/Users/admin/Amazon-Logo.png")
resized_amazon = amazon_img.subsample(40,40)


Amazon_btn = Button(win,image=resized_amazon,bg='white',bd=0,cursor='hand2',activebackground='white',command=click_amazon)
Amazon_btn.place(x=345,y=150)

flipkart_img = PhotoImage(file="C:/Users/admin/flipkart.png")
resized_flipkart = flipkart_img.subsample(40,40)


Flipkart_btn = Button(win,image=resized_flipkart,bg='white',bd=0,cursor='hand2',activebackground='white',command=click_flipkart)
Flipkart_btn.place(x=500,y=150)

croma_img = PhotoImage(file="C:/Users/admin/croma.png")
resized_croma = croma_img.subsample(4,4)


croma_btn = Button(win,image=resized_croma,bg='white',bd=0,cursor='hand2',activebackground='white',command=click_croma)
croma_btn.place(x=680,y=140)

reliance_img = PhotoImage(file="C:/Users/admin/reliance.png")
resized_reliance = reliance_img.subsample(20,20)


reliance_btn = Button(win,image=resized_reliance,bg='white',bd=0,cursor='hand2',activebackground='white',command=click_reliance)
reliance_btn.place(x=850,y=140)

vijay_img = PhotoImage(file="C:/Users/admin/vijaysales.png")
resized_vijay = vijay_img.subsample(2,2)


vijay_btn = Button(win,image=resized_vijay,bg='white',bd=0,cursor='hand2',activebackground='white',command=click_vijay)
vijay_btn.place(x=950,y=150)

login_btn = Button(win,text='Login',cursor='hand2',bg='red',fg='white',bd=0)
login_btn.place(x = 1200,y = 45,height=20,width=50)

signup_btn = Button(win,text='Signup',cursor='hand2',bg='red',fg='white',bd=0)
signup_btn.place(x = 1200,y = 75,height=20,width=50)

subscribe_btn = Button(win,text='Subscribe',cursor='hand2',bg='red',fg='white',bd=0)
subscribe_btn.place(x = 1300,y = 45,height=20,width=60)

Amazon_Label = Label(win,text='Amazon Price: ',font=('Times New Roman',15,'bold'))






win.mainloop()

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

Email_btn = Button(log,text='Enter',bg='lightgrey',fg='black',activebackground='red',bd=0)
Email_btn.place(x=450,y=50)

PW_btn = Button(log,text='Enter',bg='lightgrey',fg='black',activebackground='red',bd=0)
PW_btn.place(x=450,y=110)

PW_show = Button(log,text='Show Pass',bg='lightgrey',fg='black',activebackground='red',bd=0)
PW_show.place(x=120,y=150,height=20,width=60)


log.mainloop()
