#!/usr/bin/env python3 

from tkinter import *
from tkinter.ttk import *
from singlePlayer import *
class Homepage:
    def __init__(self,root=None):
        if (root==None):            
            self.root = Tk()
            self.root.title("Vache et Taureaux")
            self.mainframe = Frame(self.root, padding="15 45 15 45")
            self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
            self.root.columnconfigure(0, weight=1)
            self.root.rowconfigure(0, weight=1)


            self.mainframe.columnconfigure(0,weight=1)
            self.mainframe.columnconfigure(1,weight=3)
            self.mainframe.columnconfigure(2,weight=1)

            self.mainframe.rowconfigure(0,weight=1)
            self.mainframe.rowconfigure(1,weight=3)
            self.mainframe.rowconfigure(2,weight=1)
            self.mainframe.rowconfigure(3,weight=1)
            self.mainframe.rowconfigure(4,weight=1)


            Button(self.mainframe, text="Single Player",command=self.singlePlayer).grid(column=1, row=2)
            Button(self.mainframe, text="Multiplayer").grid(column=1,row=3)
            Button(self.mainframe, text="Quit",command=exit).grid(column=1,row=4)


            self.style = Style()
            self.style.theme_use('alt')
            self.style.configure('TButton', background='#A02F40', foreground="#F5DDBC")
            self.style.configure('TFrame', background='#5F2F42')
        else:
            self.root=root
    def singlePlayer(self):
        SinglePlayer(self.root)
    def show(self):
        self.root.mainloop()

homepage = Homepage()
homepage.show()
