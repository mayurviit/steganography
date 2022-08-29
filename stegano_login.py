import random as r          
from datetime import date
#print(dir(datetime))
today=date.today()
today=str(today)
for i in today:
    if(i=="-"):
        today=today.replace("-","")
#print(today)
ppassword=str(int(today)-20010701)
vpassword=str(int(today)-20020811)
mpassword=str(int(today)-20040515)
vipassword=str(int(today)-20031204)
prpassword=str(int(today)-20030717)
#print(ppassword)
#print(vpassword)
#print(mpassword)
#print(vipassword)
#print(prpassword)
import getpass
database = {"parth.22110808@viit.ac.in":ppassword,"viraj.22110792@viit.ac.in":vpassword,
                   "mayur.22110824@viit.ac.in":mpassword,"vinay.22110856@viit.ac.in":vipassword,
                   "prajwal.22110517@viit.ac.in":prpassword}
strtemp=""
from tkinter import *
#defining login function
def login():
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
        for i in database.keys():
            if uname==i:
                if pwd==database[i]:
                    message.set("Login success")
                    strtemp="Login Success"
                    break
                
                else:
                    message.set("Wrong username or password!!!")
                    strtemp="Wrong username or password "
                    break
        if strtemp=="Login Success":

            login_screen.destroy()
            import Stengano_final_graphics
#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Login Form")
    #setting height and width of screen
    login_screen.geometry("300x250")
    #declaring variable
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Username Label
    Label(login_screen, text="Username * ").place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username).place(x=90,y=42)
    #Password Label
    Label(login_screen, text="Password * ").place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
    login_screen.mainloop()
#calling function Loginform
Loginform()


     
