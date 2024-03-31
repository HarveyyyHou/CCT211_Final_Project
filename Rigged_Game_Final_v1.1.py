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

# Screen is 0 by default(which is dice)
# current_screen is a global var that determines what screen the user is on
# clicking on the buttons in the row changes to 0,1,2 respectively
# 0 = dice, 1 = RNG, 2 = name picker
current_screen = 0
def switch_screen(screen):
    global current_screen
    current_screen = screen
    # print(current_screen)

mastertk = Tk()

mastermenu = Menu(mastertk)
mastermenu.add_cascade(label="Dice", command=lambda: switch_screen(0))
mastermenu.add_cascade(label="Number_Generator", command=lambda: switch_screen(1))
mastermenu.add_cascade(label="NamePicker", command=lambda: switch_screen(2))

mastertk.geometry("300x300")
mastertk.config(menu=mastermenu)
mastertk.mainloop()
