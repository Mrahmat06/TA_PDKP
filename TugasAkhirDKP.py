# buat make GUI
from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox 
from userService import userService


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

# perulangan buat bg warna
    j=0
    r=200
    for i in range(5):
        c=str(994422+r)
        Label(register_screen,width=200 ,height=200 ,bg="#"+c).place(x=j,y=0)
        j=j+100
        r=r+1000
 
    Label(register_screen, text="Username & Password Required").pack(pady = 20)
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack(pady = 10)
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack(pady = 10)
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack(pady = 10)
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack(pady = 10)
    Button(register_screen, text="Register", width=10, height=1, command = register_user).pack()

    
   
 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please Login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 

def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

 #disini ada if else
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=ok).pack()

def ok():
    global kpop_store
    global stringnama
    global stringalamat
    global radio
    kpop_store = Toplevel(login_success_screen)
    kpop_store.title("Album Online Store - Personal Identity")
    kpop_store.geometry("300x200")
    Label(kpop_store, text="Please Enter your Personal Identity").pack()
    lbnama = Label(kpop_store, text = "Name\t:").place(x = 30, y = 30)    
    lbalamat = Label(kpop_store, text = "Address\t:").place(x = 30, y = 80)
    stringnama = StringVar()
    stringalamat = StringVar()
    inama = Entry(kpop_store, width = 20, textvariable=stringnama).place(x = 110, y = 30) 
    ialamat = Entry(kpop_store, width = 20, textvariable=stringalamat).place(x = 110, y = 80) 
    radio = IntVar()
    btn1 = Button(kpop_store, command = submit, text="SUBMIT").place(x=120,y=170)

def submit():
    global kpop_store_item
    global radio_item
    kpop_store_item = Toplevel(kpop_store)
    kpop_store_item.geometry("350x950")
    kpop_store_item.title("Album Online Store - Item")
    Label(kpop_store_item, text="Choose Album you want to buy").pack()
    radio_item = IntVar()
    R1 = Radiobutton(kpop_store_item, text="Harry Styles - Harry's House (2022)", variable=radio_item, value=1).place(x=75, y=50) 
    lb1 = Label(kpop_store_item, text = "$20").place(x = 75,y = 80)  
    R2 = Radiobutton(kpop_store_item, text="Harry Styles - Fine Line (2019)", variable=radio_item, value=2).place(x=75, y=150) 
    lb1 = Label(kpop_store_item, text = "$20").place(x = 75,y = 180) 
    R3 = Radiobutton(kpop_store_item, text="Harry Styles - Harry Styles (2017)", variable=radio_item, value=3).place(x=75, y=250) 
    lb1 = Label(kpop_store_item, text = "$25").place(x = 75,y = 280)
    btn2 = Button(kpop_store_item, command = struk, text="SUBMIT").place(x=150,y=855)

def struk():
    global strukanda
    strukanda = Toplevel(kpop_store_item)
    strukanda.geometry("700x450")
    strukanda.title("Payment Receipt")
    Label(strukanda, text="Your Reseipt").pack()

    struk_stringnama = stringnama.get()
    struk_stringalamat = stringalamat.get()
    radio_radio      = radio.get()
    r_item      = radio_item.get()

    if len(struk_stringnama) == 0:
        messagebox.showerror("Error","You have not filled in your name")
        return
    if len(struk_stringalamat) == 0:
        messagebox.showerror("Error","You have not filled in your Address")
        return
    if radio_item.get() == 1:
         item1 ="Harry Styles - Harry's House (2022)"
         item2 ="the price for this album is $20" 
         item3 ="Shipping Cost (World Wide) : $10"
         item4 ="$30"
    if radio_item.get() == 2:
         item1 ="Harry Styles - Fine Line (2019)"
         item2 ="the price for this album is $20"
         item3 ="Shipping Cost (World Wide) : $10"
         item4 ="$30"
    if radio_item.get() == 3:
         item1 ="Harry Styles - Harry Styles (2017)"
         item2 ="the price for this album is 25"
         item3 ="Shipping Cost (World Wide) : $10"
         item4 ="$35"


 
    Label(strukanda, text="Data Pemesan").place(x=30,y=50)
    Label(strukanda, text="Nama      :  " + struk_stringnama).place(x=30,y=70)
    Label(strukanda, text="Alamat     :  " + struk_stringalamat).place(x=30,y=90)

    Label(strukanda, text="Item yang dipesan").place(x=30,y=150)
    Label(strukanda, text=item1).place(x=30,y=170)
    Label(strukanda, text=item2).place(x=30,y=190)
    Label(strukanda, text=item3).place(x=30,y=210)

    Label(strukanda, text="Total Price = "+ item4).place(x=30,y=250)
    Label(strukanda, text="Please transfer to Zalazar Inc. at Umbrella Corp Bank (4736251) \n Thanks for Purcasing").place(x=30,y=280)
  



def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 

def del_login_screen():
    login_screen.destroy()
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login and Register Album Online Store")
    Label(text="Album Online Store", bg="cyan", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()