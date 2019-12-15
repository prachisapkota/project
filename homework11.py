#for not registered user
from termcolor import colored
from stegano import exifHeader
def signup():
    name=input(colored("enter your name",'blue'))
    age=input(colored("enter your age", 'blue'))
    while age.isnumeric()==False or int(age)<18 or int(age)>50:
        age=input(colored("invalid age input", 'red'))
    password=input(colored("enter the password for spychat", 'red'))
    while len(password)<8 or len(password)>15:
        password=input(colored("invalid password length", 'red'))
#for registered user
y ='12345678'
def login():
    a=input(colored("enter your 8 digits password", 'blue'))
    while a!=y:
        a=input(colored("enter the valid password",'blue'))
def valid():
    b=input(colored("if you are registered user then write y for yes otherwise write n for no"))
    if b=='n':
        signup()
    elif b=='y':
        login()
    else:
        valid()

        print("WELCOME TO SPYCHAT")
valid()

from stegano import lsb
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as msBox
import datetime
import re
root=Tk()
root.title("Spychat")
root.geometry("700x300")
root.config(background="black")
root.resizable(0,0)
tab=ttk.Notebook(root)
tab1=ttk.Frame(tab)
tab2=ttk.Frame(tab)
tab.add(tab1, text="Encoding")
tab.add(tab2, text="Decoding")
tab.pack(expand=1, fill="both")
#encoding
def browse(path):
    filename=filedialog.askopenfilename()
    if re.search('\.jpg$', filename) or re.search('\.png$', filename):

        path.set(filename)

    else:
        msBox.showinfo("you have choosen a wrong file, it is neither jpg nor png")



def hide_msg(path,message):
    message_time = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    new_img='Secret_pic'+message_time+'.jpg'
    exifHeader.hide(path.get(), new_img, secret_message=message.get())
    msBox.showinfo("saved", "image has been saved with name "+new_img)
path=StringVar()
path_entry=Entry(tab1,width=30, borderwidth=2,textvariable=path)
path_entry.place(relx=0.35, rely=0.15)
but1=Button(tab1, text="Search Image", fg='blue', bg='red',width=20, command=lambda:browse(path))
but1.place(relx=0.4, rely=0.02)



message=Label(tab1, text="your message here", fg='blue', bg='sky blue', font=(" ", 15))
message.place(relx=0.35, rely=0.30)
msg=StringVar()
msg_entry=Entry(tab1,width=30, borderwidth=2,textvariable=msg)

msg_entry.place(relx=0.35, rely=0.43)
ency=Button(tab1, text="Encode", fg='sky blue', bg='black',command=lambda:hide_msg(path,msg))
ency.place(relx=0.4, rely=0.85)

#for decoding



def decode(path):
    print('path is ',path.get())
    print(exifHeader.reveal(path.get()))

def view(path):
    sms=exifHeader.reveal(path.get())
    msBox.showinfo("Revealed!!!", "Messasge is  " + sms.decode('UTF-8'))


path2=StringVar()
but2=Button(tab2, text="Add Image", fg="sky blue", bg='red', width=10, command=lambda:browse(path2))
but2.place(relx=0.25, rely=0.02)
path_entry1=Entry(tab2, width=30, borderwidth=2, textvariable=path2)
path_entry1.place(relx=0.25, rely=0.15)

but3=Button(tab2, text=" View message", fg="sky blue", bg='red', font=(" ", 15),command=lambda : view(path2))
but3.place(relx=0.25, rely=0.30)
root.mainloop()