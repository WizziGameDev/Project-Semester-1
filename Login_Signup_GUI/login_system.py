import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import * 

root = tk.Tk()
root.geometry('450x600')
root.resizable(False,False)
root.configure(background='Grey')

USERNAME = tk.StringVar()
PASSWORD = tk.StringVar()
CHECKBUTTON = tk.IntVar()

# Fungsi untuk mengolah data
def login():
    
    if USERNAME.get() == 'admin' and int(PASSWORD.get()) == 123 and CHECKBUTTON.get() == 1:
        print(' Anda berhasil login')

    else:
        print(' Anda gagal login')

def TestBox():
    print(f' Ngetest checkbox = {CHECKBUTTON.get()}')


# Display semua komponen login
app = ttk.Frame(root)
app.pack(padx=50, pady=60, expand=True, fill='both')

title = ttk.Label(app, font=('Roboto', 20), text='Login System')
title.pack(pady=20, fill='y')

usernameTitle = ttk.Label(app, font=('Roboto', 10), text='Username')
usernameTitle.pack(padx=25, pady=5, fill='x')

usernameInput = ttk.Entry(app, textvariable=USERNAME)
usernameInput.pack(padx=25, pady=0, fill='x')

passwordTitle = ttk.Label(app, font=('Roboto', 10), text='Password')
passwordTitle.pack(padx=25, pady=5, fill='x')

passwordInput = ttk.Entry(app, textvariable=PASSWORD)
passwordInput.pack(padx=25, pady=0, fill='x')

checkBox = tk.Checkbutton(app, text='Check Rules', font=('Roboto', 8), onvalue=1, offvalue=0 ,command=TestBox, variable=CHECKBUTTON)
checkBox.pack(pady=15, fill='y')

loginButton = Button(app, text='Log in', command=login, activebackground='grey',background='green', width=10, height=1, border='1', font=('Roboto', 10), foreground='white')
loginButton.pack(pady=10)

# signButton = Button(app, text='Sign Up', command=open_sign_up, activebackground='grey',background='green', width=10, height=1, border='1', font=('Roboto', 10), foreground='white')
# signButton.pack()

# Looping
root.mainloop()