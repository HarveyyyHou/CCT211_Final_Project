from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import tkinter.ttk as ttk

class Dice:
    def __init__(self):
        pass

    def roll(self):
        pass
class Random_Number:

    def __init__(self):
        pass

    def spin(self):
        pass

class Name_Pick:

    def __init__(self):
        pass
    def choose(self):
        pass

class Rigged(tk.Frame):
    def __init__(self):
        pass

class Generate_History:
    '''
    Save the current settings in History via Panda
    '''

mastertk = Tk()

mastermenu = Menu(mastertk)
mastermenu.add_cascade(label="Dice")
mastermenu.add_cascade(label="Number_Generator")
mastermenu.add_cascade(label="NamePicker")

mastertk.geometry("300x300")
mastertk.config(menu=mastermenu)
mastertk.mainloop()