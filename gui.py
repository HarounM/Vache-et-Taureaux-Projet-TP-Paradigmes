#!/usr/bin/env python3 

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Vache et Taureaux")

mainframe = Frame(root, padding="15 45 15 45")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


mainframe.columnconfigure(0,weight=1)
mainframe.columnconfigure(1,weight=3)
mainframe.columnconfigure(2,weight=1)

mainframe.rowconfigure(0,weight=1)
mainframe.rowconfigure(1,weight=3)
mainframe.rowconfigure(2,weight=1)
mainframe.rowconfigure(3,weight=1)
mainframe.rowconfigure(4,weight=1)


Button(mainframe, text="Single Player").grid(column=1, row=2)
Button(mainframe, text="Multiplayer").grid(column=1,row=3)
Button(mainframe, text="Quit",command=exit).grid(column=1,row=4)


style = Style()
style.theme_use('alt')
style.configure('TButton', background='#A02F40', foreground="#F5DDBC")
style.configure('TFrame', background='#5F2F42')


root.mainloop()
