from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.title("ctOS")
root.resizable(False, False)
root.geometry("290x540")
root.configure(bg="black")


def c_prompt():
    james = os.getlogin()
    ps = os.getpid()
    ll = os.getcwd()
    print(james, ps, ll)


btn_1 = Button(text="CMD", command=c_prompt, bg="white").grid(row=0, column=0)
root.mainloop()
