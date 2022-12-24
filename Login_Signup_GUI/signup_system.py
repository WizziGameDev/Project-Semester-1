
import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import string

# Display apps
root = tk.Tk()
root.configure(background='grey')
root.geometry('450x600')
root.resizable(False, False)
root.title(' Dolanan Apps')

# Variabel Pendukung
USERNAME = tk.StringVar()
PASSWORD = tk.StringVar()
CHECKBUTTON = tk.IntVar()

# Fungsi

templateDatabase = {
    'username' : 'none',
    'password' : 'none',
}

dataBase = {}

def signUp():
    if CHECKBUTTON.get() == 1:    
        data = dict.fromkeys(templateDatabase.keys())

        data['username'] = USERNAME.get() # mengambil username input apps kemudian di taruh di dictionary
        data['password'] = PASSWORD.get() # mengambil password input apps kemudian di taruh di dictionary
        
        # Bagian update KEY biar terjadi update didalamnya
        KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
        dataBase.update({KEY:data})

        print(f"\n {'KEY':<6} {'Username':<20} {'Password':<8}")
        print('','-'* 36)

        for data in dataBase:
            KEY = data
            DATAUSERKU = dataBase [KEY] ['username']
            DATAPASSKU = dataBase [KEY] ['password']
            print(f" {KEY:<6} {DATAUSERKU:<20} {DATAPASSKU:<8}")
    else:
        print(' Anda gagal Sign Up')

# Awal Komponen
sign = tk.Frame(root)
sign.pack(padx=50, pady=60, expand=True, fill='both')

# Label Sign Up
judul = ttk.Label(sign, text='Sign Up System', font=('Roboto', 20))
judul.pack(pady=20, fill='y')

# Entry Username
UsernameLabel = ttk.Label(sign, text='Username', font=('Roboto',10))
UsernameLabel.pack(padx=25, pady=5, fill='x')

UsernameEntry = ttk.Entry(sign, textvariable=USERNAME)
UsernameEntry.pack(padx=25, fill='x')

# Entry Password
PasswordLabel = ttk.Label(sign, text='Password', font=('Roboto', 10))
PasswordLabel.pack(padx=25, pady=5, fill='x')

PasswordEntry = ttk.Entry(sign, textvariable=PASSWORD)
PasswordEntry.pack(padx=25, fill='x')

checkBox = Checkbutton(sign, onvalue=1, offvalue=0, text='condition and tems',font=('Roboto', 8), variable=CHECKBUTTON)
checkBox.pack(pady=15, fill='x')

signUpButton = Button(sign, text='Sign Up', command=signUp, activebackground='grey', background='green', width=10, height=1, border='1',font=('Roboto', 10), foreground='white')
signUpButton.pack(pady=10)

# logInButton = Button(sign, text='Log In', command=hide_sign_up, activebackground='grey',background='green', width=10, height=1, border='1', font=('Roboto', 10), foreground='white')
# logInButton.pack()

root.mainloop()