#from funcs import functions
import os
import tkinter as tk
from tkinter import *
from tkinter.font import Font


def OnPressed1(event):
    But1.config(bg='light grey', fg='black')
    functions.items()



def OnHover1(event):
    But1.config(bg='light grey', fg='white')

def OnLeave1(event):
    But1.config(bg='light grey', fg='black')



def OnPressed2(event):
    But2.config(bg='light grey', fg='black')
    functions.FS()
            



def OnHover2(event):
    But2.config(bg='light grey', fg='white')

def OnLeave2(event):
    But2.config(bg='light grey', fg='black')


def OnPressed3(event):
    But3.config(bg='light grey', fg='black')
    But3.place_forget()
    entry1.place_forget()
    But4.place_forget()
    But1.place(x=20, y=20)
            



def OnHover3(event):
    But3.config(bg='light grey', fg='white')

def OnLeave3(event):
    But3.config(bg='light grey', fg='black')



class functions():
    def FS():
        root.wm_attributes('-fullscreen','true')
        But2.place_forget()
        But5.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)


    def  items():
        But1.place_forget()
        But3.place(rely=1.0, relx=0, x=0, y=0, anchor=SW)
        entry1.place(rely=0.25, relx=0.5, x=0, y=0, anchor="center", height=100, width=200)
        But4.place(rely=0.5, relx=0.5, x=0, y=0, anchor="center")

    def entry():
        textenter = entry1.get()
        f = open("numbers.txt", "w")
        f.write(textenter)
        f.close()
        os.startfile("numbers.txt", 'open')

    def window():
        root.wm_attributes('-fullscreen','false')
        But5.place_forget()
        But2.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
    
    def close_window():
        root.destroy()







root = tk.Tk()

root.title("Test")
root.iconbitmap('icon.ico')
root.resizable(0,0)

root.geometry("1280x720")

root.config(background = "light grey")

myFont = Font(family="Dense", size=50, weight="normal", underline=0)

myFont2 = Font(family="Dense", size=35, weight="bold", underline=0)

myFont3 = Font(family="Dense", size=25, weight="normal", underline=0)



image = PhotoImage(file="exit.png")


But1 = Button(text="T Y P E", border=0, font=myFont, bg="light grey")
But1.place(x=20, y=20)
But1.bind("<Button-1>", OnPressed1)
But1.bind("<Enter>", OnHover1)
But1.bind("<Leave>", OnLeave1)

But2 = Button(text="F u l l s c r e e n  M o d e", border=0, font=myFont2, bg="light grey")
But2.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
But2.bind("<Button-1>", OnPressed2)
But2.bind("<Enter>", OnHover2)
But2.bind("<Leave>", OnLeave2)


But3 = Button(text="B a c k", border=0, font=myFont2, bg="light grey")
But3.bind("<Button-1>", OnPressed3)
But3.bind("<Enter>", OnHover3)
But3.bind("<Leave>", OnLeave3)

But4 = Button(text="E X P O R T", border=0, font=myFont2, bg="grey", fg="white", command=functions.entry)

But5 = Button(text="W i n d o w e d", border=0, font=myFont2, bg="light grey", command=functions.window)

But6 = Button(image=image, border=0, bg="light grey", command=functions.close_window)
But6.place(rely=0.0125, relx=0.9875, x=0, y=20, anchor=NE)





entry1 = tk.Entry(root, border = 0.5, font=myFont3, background="dark grey")



root.mainloop()





