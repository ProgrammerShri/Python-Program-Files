from tkinter import *

app = Tk()
Label(app,text = "Enter Password :  ").pack()

e = Entry(app,show ='*')
e.pack()

def get():
    print("Password : ",e.get())

Button(app,text = "Get", command = get).pack()

app.mainloop()

