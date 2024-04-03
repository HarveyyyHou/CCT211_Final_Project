from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import tkinter.ttk as ttk
import Random

class Dice:
    def __init__(self):
        pass

    def roll(self):
        pass
class Random_Number:

    "Randomly selects a Number"

    def __init__(self):
        self.rigged = None

        self.Spin_Button = Button(mastertk, text='Spin', activebackground="blue",
                                 activeforeground="blue", command=self.spin)
        self.Spin_Button.place(anchor=CENTER,relx=0.7,rely=0.4)

        self.Rigged = Button(mastertk, text="Settings",
                           command=self.rigged)
        self.Rigged.place(anchor=CENTER,relx=0.9,rely=0.9)

        self.Save = Button(mastertk, text="Save to History",
                           command=self.history)
        self.Save.place(anchor=CENTER,relx=0.5,rely=0.8)

        self.ChosenLabel = Label(mastertk, text="Chosen Number")
        self.ChosenLabel.place(anchor=CENTER,relx=0.2,rely=0.1)

        self.helplabel = Label(mastertk, text="to")
        self.helplabel.place(anchor=CENTER, relx=0.7, rely=0.3)
        self.ResultFrame = Frame(mastertk, width=125, height=125, relief='raised', borderwidth=5)
        self.ResultFrame.place(x=0, y=50)

        self.RangeLabel = Label(mastertk, text="Select integer range")
        self.RangeLabel.place(anchor=CENTER,relx=0.7,rely=0.1)
        self.validation = mastertk.register(self.number_or_no)
        self.front = tk.Entry(mastertk, validate="key", validatecommand=(self.validation, '%P'), width=5)
        self.front.place(anchor=CENTER,relx=0.55,rely=0.3)
        self.end = tk.Entry(mastertk, validate="key", validatecommand=(self.validation, '%P'), width=5)
        self.end.place(anchor=CENTER,relx=0.85,rely=0.3)


    def spin(self):
        if self.rigged == None:
            frontnum = int(self.front.get())
            endnum = int(self.end.get())
            MyNum = str(random.randint(frontnum,endnum))
            Numberlabel = Label(self.ResultFrame, text=MyNum)
            Numberlabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            Mylabel = Label(mastertk, text=self.rigged)
            Mylabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    def number_or_no(self,myint):
        if myint.isnumeric():
            return True
        # Allows backspace to first character
        elif myint == "":
            return True
        else:
            return False

    def rigged(self):
        pass
    def history(self):
        print("not implemented yet")
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
    if current_screen==1:
        my_random = Random_Number()

mastertk = Tk()

mastermenu = Menu(mastertk)
mastermenu.add_cascade(label="Dice", command=lambda: switch_screen(0))
mastermenu.add_cascade(label="Number_Generator", command=lambda: switch_screen(1))
mastermenu.add_cascade(label="NamePicker", command=lambda: switch_screen(2))

mastertk.geometry("300x300")
mastertk.config(menu=mastermenu)
mastertk.mainloop()
