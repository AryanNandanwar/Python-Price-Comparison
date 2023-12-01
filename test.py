from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
from tkinter import messagebox
import mysql.connector
from bs4 import BeautifulSoup
import requests
import webbrowser

window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')
window.resizable(0, 0)
window.title('Indias most efficient Price Comparison System')

#=== Defining Header ====#
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}



#Database Connectivity

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="15adn/2003",
  database="subscribers"
)

#LoginConnectivity#
def check_credentials():
    # retrieve the entered username and password
      Email = email_entry.get()
      Password = password_entry1.get()

    # query the database to check if the entered credentials are valid
      cursor = mydb.cursor()
      cursor.execute("SELECT * FROM subs WHERE Email=%s AND Password=%s", (Email, Password))
      result = cursor.fetchone()

    # if the query returns a row, the credentials are valid
      if result is not None:
        show_frame(FavouritePage)
      else:
        messagebox.showinfo("Login Status","Invalid Email or Password!")

#=====Subscribe Connectivity====#
def insert():
    
    name = name_entry.get()
    email = email_entry1.get()
    contact = contact_entry.get()
    password = password_entry.get()
    
    if(name==""or email=="" or contact== "" or password==""):
        messagebox.showinfo("Insert Status","All Fields Required")
        
    else:
        conn = mysql.connector.connect(host="localhost",user="root",password="15adn/2003",database="subscribers")
        cursor = conn.cursor()
        cursor.execute("insert into subs values('"+name+"','"+email+"','"+contact+"','"+password+"')")        
        cursor.execute("commit")
        name_entry.delete(0,'end')
        email_entry1.delete(0,'end')
        contact_entry.delete(0,'end')
        password_entry.delete(0,'end')
        messagebox.showinfo("Insert Status","Inserted Successsfully")
        conn.close()

#=====Favourite Connectivity=====#





LoginPage = Frame(window)
RegistrationPage = Frame(window)
MainPage = Frame(window)
FavouritePage = Frame(window)

for frame in (LoginPage, RegistrationPage,MainPage,FavouritePage):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(MainPage)




# =====================================================================================================================
# =====================================================================================================================
# ==================== LOGIN PAGE =====================================================================================
# =====================================================================================================================
# =====================================================================================================================

design_frame1 = Listbox(LoginPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame1.place(x=0, y=0)

design_frame2 = Listbox(LoginPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame2.place(x=676, y=0)

design_frame3 = Listbox(LoginPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame3.place(x=75, y=106)

design_frame4 = Listbox(LoginPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame4.place(x=676, y=106)

# ====== Email ====================
email_entry = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                    )
email_entry.place(x=134, y=170, width=256, height=34)
email_entry.config(highlightbackground="black", highlightcolor="black")
email_label = Label(design_frame4, text='• Email account', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
email_label.place(x=130, y=140)

# ==== Password ==================
password_entry1 = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                        )
password_entry1.place(x=134, y=250, width=256, height=34)
password_entry1.config(highlightbackground="black", highlightcolor="black")
password_label = Label(design_frame4, text='• Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
password_label.place(x=130, y=220)


# function for show and hide password
def password_command():
    if password_entry1.cget('show') == '•':
        password_entry1.config(show='')
    else:
        password_entry1.config(show='•')


# ====== checkbutton ==============
checkButton = Checkbutton(design_frame4, bg='#f8f8f8', command=password_command, text='show password')
checkButton.place(x=140, y=288)

# ========= Buttons ===============
SignUp_button = Button(LoginPage, text='Subscribe', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=1100, y=175)


# ===== Welcome Label ==============
welcome_label = Label(design_frame4, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=250, y=15)

# ======= top Login Button =========
login_button = Button(LoginPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', cursor='hand2',command=lambda: show_frame(MainPage))
login_button.place(x=845, y=175)

login_line = Canvas(LoginPage, width=60, height=5, bg='#1b87d2')
login_line.place(x=840, y=203)

# ==== LOGIN  down button ============
loginBtn1 = Button(design_frame4, fg='#f8f8f8', text='Login', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: check_credentials())
loginBtn1.place(x=133, y=340, width=256, height=50)


# ===== Left Side Picture ============









# =====================================================================================================================
# =====================================================================================================================
# ==================== REGISTRATION PAGE ==============================================================================
# =====================================================================================================================
# =====================================================================================================================

design_frame5 = Listbox(RegistrationPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame5.place(x=0, y=0)

design_frame6 = Listbox(RegistrationPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame6.place(x=676, y=0)

design_frame7 = Listbox(RegistrationPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame7.place(x=75, y=106)

design_frame8 = Listbox(RegistrationPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame8.place(x=676, y=106)

# ==== Full Name =======
name_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                   )
name_entry.place(x=284, y=150, width=286, height=34)
name_entry.config(highlightbackground="black", highlightcolor="black")
name_label = Label(design_frame8, text='•Full Name', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
name_label.place(x=280, y=120)

# ======= Email ===========
email_entry1 = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                    )
email_entry1.place(x=284, y=220, width=286, height=34)
email_entry1.config(highlightbackground="black", highlightcolor="black")
email_label1 = Label(design_frame8, text='•Email', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
email_label1.place(x=280, y=190)

# ====== Password =========
password_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                       )
password_entry.place(x=284, y=295, width=286, height=34)
password_entry.config(highlightbackground="black", highlightcolor="black")
password_label = Label(design_frame8, text='• Password', fg="#89898b", bg='#f8f8f8',
                       font=("yu gothic ui", 11, 'bold'))
password_label.place(x=280, y=265)


def password_command2():
    if password_entry.cget('show') == '•':
        password_entry.config(show='')
    else:
        password_entry.config(show='•')


checkButton = Checkbutton(design_frame8, bg='#f8f8f8', command=password_command2, text='show password')
checkButton.place(x=290, y=330)


# ====== Confirm Password =============
contact_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                              )
contact_entry.place(x=284, y=385, width=286, height=34)
contact_entry.config(highlightbackground="black", highlightcolor="black")
contact_label = Label(design_frame8, text='• Contact No', fg="#89898b", bg='#f8f8f8',
                              font=("yu gothic ui", 11, 'bold'))
contact_label.place(x=280, y=355)

# ========= Buttons ====================
SignUp_button = Button(RegistrationPage, text='Subscribe', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(MainPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=1100, y=175)

Home_button = Button( LoginPage, text='Home', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b", borderwidth=0, activebackground='#1b87d2', cursor='hand2',command=lambda: show_frame(MainPage))
Home_button.place(x=965, y=175)

SignUp_line = Canvas(RegistrationPage, width=60, height=5, bg='#1b87d2')
SignUp_line.place(x=1100, y=203)

Home_button = Button( RegistrationPage, text='Home', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b", borderwidth=0, activebackground='#1b87d2', cursor='hand2',command=lambda: show_frame(MainPage))
Home_button.place(x=965, y=175)
# ===== Welcome Label ==================
welcome_label = Label(design_frame8, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=250, y=15)

# ========= Login Button =========
login_button = Button(RegistrationPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', command=lambda: show_frame(LoginPage), cursor='hand2')
login_button.place(x=845, y=175)



# ==== SIGN UP down button ============
signUp2 = Button(design_frame8, fg='#f8f8f8', text='Subscribe', bg='#1b87d2', font=("yu gothic ui bold", 15),
                 cursor='hand2', activebackground='#1b87d2',command=lambda: insert())
signUp2.place(x=285, y=435, width=286, height=50)




# ========================Home Page ================================================= #

design_frame9 = Listbox(MainPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame9.place(x=0, y=0)

design_frame10 = Listbox(MainPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame10.place(x=676, y=0)

design_frame11 = Listbox(MainPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame11.place(x=75, y=106)

design_frame12 = Listbox(MainPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame12.place(x=676, y=106)

#Entry and Label

main_entry = Entry(design_frame12, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                    )
main_entry.place(x=134, y=170, width=256, height=34)
main_entry.config(highlightbackground="black", highlightcolor="black")
main_label = Label(design_frame12, text='Find Products', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
main_label.place(x=130, y=140)

#SearchImage

searchImage = PhotoImage(file="C:/Users/admin/search.png")
resized_search = searchImage.subsample(17, 17)

searchButTon=Button(MainPage,image=resized_search,bg='white',bd=0,cursor='hand2',activebackground='lightgrey',command=lambda: search_prices(name = main_entry.get()))
                 
searchButTon.place(x =1080,y = 276)

#Login and Signup and Home

login_button = Button(MainPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', command=lambda: show_frame(LoginPage), cursor='hand2')
login_button.place(x=845, y=175)

SignUp_button = Button(MainPage, text='Subscribe', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=1100, y=175)

Home_button = Button( MainPage, text='Home', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b", borderwidth=0, activebackground='#1b87d2', cursor='hand2')
Home_button.place(x=965, y=175)

#Welcome

welcome_label = Label(design_frame12, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=250, y=15)

#====Labels====#

AmazonLabel = Label(design_frame12, text='', font=('Arial', 10, 'bold'), bg='#f8f8f8')
AmazonLabel.place(x=50, y=230)

AmazonNameLabel = Label(design_frame12, text='', font=('Arial', 10, 'bold'), bg='#f8f8f8')
AmazonNameLabel.place(x=50, y=250)

AmazonPriceLabel = Label(design_frame12, text='', font=('Arial', 10, 'bold'), bg='#f8f8f8')
AmazonPriceLabel.place(x=50, y=270)

AmazonNoneLabel = Label(design_frame12, text='', font=('Arial', 10, 'bold'), bg='#f8f8f8')
AmazonNoneLabel.place(x=50, y=290)

AmazonURLLabel = Label(design_frame12, text='', font=('Arial', 10, 'bold'), bg='#f8f8f8')
AmazonURLLabel.place(x=50, y=305)


FlipkartLabel = Label(design_frame12, text='', font=('Arial', 10, 'bold'), bg='#f8f8f8')
FlipkartLabel.place(x=50, y=330)

FlipkartNameLabel = Label(design_frame12, text='', font=('Arial', 10, 'bold'), bg='#f8f8f8')
FlipkartNameLabel.place(x=50, y=350)

FlipkartPriceLabel = Label(design_frame12, text='', font=('Arial', 10, 'bold'), bg='#f8f8f8')
FlipkartPriceLabel.place(x=50, y=370)

FlipkartNoneLabel = Label(design_frame12, text='', font=('Arial', 10, 'bold'), bg='#f8f8f8')
FlipkartNoneLabel.place(x=50, y=390)

FlipkartURLLabel = Label(design_frame12, text='', font=('Arial', 10, 'bold'), bg='#f8f8f8')
FlipkartURLLabel.place(x=50, y=410)



#Compare button#
def open_amazon_url(event):
    webbrowser.open(amazon_url)

def open_flipkart_url(event):
    webbrowser.open(flipkart_url)


#======= Amazon and Flipkart Functions ===================#
#===Flipkart===#

def flipkart(name):
  try:
    name = main_entry.get()
    
    global flipkart_url
    name1 = name.replace(" ","+")
    flipkart_url=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
    res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)


        
    soup = BeautifulSoup(res.text,'html.parser')
        
    if(soup.select('._4rR01T')):
            flipkart_name = soup.select('._4rR01T')[0].getText().strip().upper()
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('._30jeq3')[0].getText().strip()
                flipkart_name = soup.select('._4rR01T')[0].getText().strip()
                print("Flipkart:")
                FlipkartLabel.config(text="Flipkart:")
                print(flipkart_name)
                FlipkartNameLabel.config(text=f"{flipkart_name}")
                print(flipkart_price.encode('utf-8').decode('cp1252'))
                FlipkartPriceLabel.config(text=f"{flipkart_price}")
                print(flipkart_url)
                FlipkartURLLabel.config(text=f"{flipkart_url}")
                FlipkartURLLabel.bind("<Button-1>", open_flipkart_url)
                
    elif(soup.select('.s1Q9rs')):
            flipkart_name = soup.select('.s1Q9rs')[0].getText().strip()
            flipkart_name = flipkart_name.upper()
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('._30jeq3')[0].getText().strip()
                flipkart_name = soup.select('.s1Q9rs')[0].getText().strip()
                print("Flipkart:")
                FlipkartLabel.config(text="Flipkart:")
                print(flipkart_name)
                FlipkartNameLabel.config(text=f"{flipkart_name}")
                print(flipkart_price.encode('utf-8').decode('cp1252'))
                FlipkartPriceLabel.config(text=f"{flipkart_price}")
                print(flipkart_url)
                FlipkartURLLabel.config(text=f"{flipkart_url}")
                FlipkartURLLabel.bind("<Button-1>", open_flipkart_url)  # Bind the label to the function
                
    else:
            flipkart_price='0'
            messagebox.showinfo("Flipkart","No product found!") 
            
    return flipkart_price 
  except:
    messagebox.showinfo("Flipkart","No product found!") 
    
    
     
amazon_url = ''
flipkart_url = ''
        
#===Amazon===#
def amazon(name):
    name = main_entry.get()
    global amazon_url
    name1 = name.replace(" ","-")
    name2 = name.replace(" ","+")
    amazon_url=f'https://www.amazon.in/{name1}/s?k={name2}'
    res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    amazon_page = soup.select('.a-color-base.a-text-normal')
    amazon_page_length = int(len(amazon_page))
    amazon_price = '0'  # Define the variable outside the if-else blocks with a default value
    for i in range(0,amazon_page_length):
        name = name.upper()
        amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
        if name in amazon_name:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip()
                amazon_name = amazon_name.encode('utf-8').decode('cp1252', 'ignore')

                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
                print("Amazon:")
                AmazonLabel.config(text="Amazon:")
                print(amazon_name)
                AmazonNameLabel.config(text=f"{amazon_name}")
                print(amazon_price.encode('utf-8').decode('cp1252'))
                AmazonPriceLabel.config(text=f"{amazon_price}")
                print(amazon_url)
                AmazonURLLabel.config(text=f"{amazon_url}")
                AmazonURLLabel.bind("<Button-2>", open_amazon_url)  # Bind the label to the function
                break
        else:
                i+=1
                i=int(i)
                if i==amazon_page_length:
                    print("amazon : No product found!") 
                    messagebox.showinfo("Amazon","No product found!")                   
                    break
    return amazon_price  # Return the variable after the for loop

  
  #===Defining Search Function===#
  
def search_prices(name):
  name = main_entry.get()
  amazon(name)
  flipkart(name)
  name = ' '

# =====================================================================================================================
# =====================================================================================================================
# ==================== FAVOURITE =====================================================================================
# =====================================================================================================================
# =====================================================================================================================
    
design_frame13 = Listbox(FavouritePage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame13.place(x=0, y=0)

design_frame14 = Listbox(FavouritePage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame14.place(x=676, y=0)

design_frame15 = Listbox(FavouritePage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame15.place(x=75, y=106)

design_frame16 = Listbox(FavouritePage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame16.place(x=676, y=106)

login_button = Button(FavouritePage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', command=lambda: show_frame(LoginPage), cursor='hand2')
login_button.place(x=845, y=175)

SignUp_button = Button(FavouritePage, text='Subscribe', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=1100, y=175)

Home_button = Button( FavouritePage, text='Home', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b", borderwidth=0, activebackground='#1b87d2', cursor='hand2',command=lambda: show_frame(MainPage))
Home_button.place(x=965, y=175)

Favourite_button = Button(FavouritePage, text='Favourite', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
Favourite_button.place(x=715, y=175)

welcome_label = Label(design_frame16, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=250, y=15)

#=====Favourite Connectivity====#
def connects():
    
    Name = fav_entry.get()
    
    
    if(Name==""):
        messagebox.showinfo("Insert Status","Please Enter Product!")
        
    else:
        conn = mysql.connector.connect(host="localhost",user="root",password="15adn/2003",database="subscribers")
        cursor = conn.cursor()
        cursor.execute("insert into products values('"+Name+"')")        
        cursor.execute("commit")
        name_entry.delete(0,'end')
        email_entry1.delete(0,'end')
        contact_entry.delete(0,'end')
        password_entry.delete(0,'end')
        messagebox.showinfo("Insert Status","Product added to favourite list")
        conn.close()

#Entry and Label

fav_entry = Entry(design_frame16, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                    )
fav_entry.place(x=134, y=170, width=256, height=34)
fav_entry.config(highlightbackground="black", highlightcolor="black")
fav_label = Label(design_frame16, text='Enter Favourite Products', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
fav_label.place(x=130, y=140)

#SearchImage

signUp2 = Button(design_frame16, fg='#f8f8f8', text='Enter', bg='#1b87d2', font=("yu gothic ui bold", 15),
                 cursor='hand2', activebackground='#1b87d2',command=lambda: connects())
signUp2.place(x=285, y=435, width=286, height=50)
                 

  

window.mainloop()
mydb.close()