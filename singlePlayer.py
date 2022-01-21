from tkinter import *
from tkinter.ttk import *

class SinglePlayer:
    def __init__(self,root=None):
        if root == None:
            raise Exception("Bade usage of singlePlayer class")
        else:
            self.root=root
            for child in self.root.winfo_children():
                child.destroy()
       
            self.mainframe = Frame(self.root, padding="15 45 15 45")
            self.root.columnconfigure(0, weight=1)
            self.root.rowconfigure(0, weight=1)
            self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        
            Button(self.mainframe, text="Submit").grid(column=1, row=2)
            self.style = Style()
            self.style.theme_use('alt')
            self.style.configure('TButton', background='#A02F40', foreground="#F5DDBC")
            self.style.configure('TFrame', background='#5F2F42')
    def onSubmit():
        pass
