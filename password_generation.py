#imports
import random
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

#set variable
master = Tk()

# functions
def validate(a, b, c):
    if len(length.get()) < 3 and length.get().isdigit() and int(length.get()) >= 6 and int(length.get()) <= 20:
        el.config(bg = 'green')
        
    else:
        el.config(bg = 'red')


def getpass():
    if length.get() == '':
        messagebox.showerror('error!','Enter your password length')
    elif var1.get() == 0 and var2.get() == 0 and var3.get() == 0:
        messagebox.showerror('error!','Select your password difficulity')
    elif int(length.get()) > 30:
        messagebox.showerror('Error!','Your password length is not allowed')
    else:
        passlen = int(length.get())
        lowwer = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        symbols = '~`!@#$%^&*()_-+={[}]|\:;<,>.?/'
        numbers = '0123456789'

        if var1.get() == 1:
            simple = lowwer + numbers
            r = random.sample(simple, passlen)
            s = ''.join(r)
            password.set(s)

        if var2.get() == 1:
            hard = lowwer + numbers + upper
            r = random.sample(hard, passlen)
            s = ''.join(r)
            password.set(s)

        if var3.get() == 1:
            difficult = lowwer + numbers + upper + symbols
            r = random.sample(difficult, passlen)
            s = ''.join(r)
            password.set(s)

#create GUI
font = Font(family="Verdana", size=13)
Label(master, text = 'set length of your password', font=font).grid(row=0, column=0)
Label(master, text = '(from 6 to 20)', font=font).grid(row=1, column=0)
length = StringVar()
length.trace('w', validate)
el = Entry(master, textvariable=length, font=font)
el.grid(row=2, column=0)
Label(master, text = 'your password :', font=font).grid(row=3, column=0)
password = StringVar()
Label(master, textvariable=password, font=font).grid(row=4, column=0)
Button(master, text = 'Get your password', font=font, relief=GROOVE, command=getpass).grid(row=5, column=0)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
Checkbutton(master, text = "Simple", font=font, variable=var1, onvalue = 1, offvalue = 0).grid(row=0, column=1, rowspan=4, sticky=W)
Checkbutton(master, text = "Hard", font=font, variable=var2, onvalue = 1, offvalue = 0).grid(row=1, column=1, rowspan=4, sticky=W)
Checkbutton(master, text = "Difficult", font=font, variable=var3, onvalue = 1, offvalue = 0).grid(row=2, column=1, rowspan=4, sticky=W)

master.mainloop()