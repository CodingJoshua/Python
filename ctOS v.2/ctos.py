from tkinter import *
import os
import sys

ctOS = Tk()
ctOS.geometry("280x540")
ctOS.title("ctOS Application")
ctOS.resizable(False, False)
ctOS.configure(bg="#292929")

cwd = os.getcwd()

def new_window():
    window = Toplevel(ctOS)
    window.title("ctOS Application")
    window.geometry("280x540")
    window.resizable(False, False)
    window.configure(bg="#292929")

    exit = Button(window, command=window.destroy, text="Exit", font=('Consolas', 10))
    exit.grid(row=6, column=0)
    

def sub_feature():
    new_window()
    

sub_feature()

ctOS.mainloop()