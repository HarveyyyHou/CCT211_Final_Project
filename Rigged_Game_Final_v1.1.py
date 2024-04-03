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

    "Randomly selects a Number"

    def __init__(self):
        #tk.Frame.__init__(self)
        self.front = 0
        self.rigged = None
        self.end = 10

        self.Spin_Button = Button(mastertk, text='Spin', activebackground="blue",
                                 activeforeground="blue", command=self.spin)
        self.Spin_Button.grid(row=10, column=6)

        self.Rigged = Button(mastertk, text="Settings",
                           command=self.rigged)
        self.Rigged.grid(row=11, column=8)

        self.Save = Button(mastertk, text="Save to History",
                           command=self.history)
        self.Save.grid(row=4, column=5)

        self.ChosenLabel = Label(mastertk, text="Chosen Number")
        self.ChosenLabel.grid(row=0, column=0)

        self.ResultFrame = Frame(mastertk, width=100, height=100, relief='raised', borderwidth=5)
        self.ResultFrame.grid(row=1, column=0)

        self.RangeLabel = Label(mastertk, text="Random integer range")
        self.validation = mastertk.register(self.number_or_no)
        #self.RangeLabel.grid(row=)
        #Ask for int entry in front frame, refer to lab8exercise3
        self.front = Entry(mastertk, validate="key", validatecommand=(self.validation, '%P'))
        self.front.grid(row=1, column=0)

    def spin(self):
        if self.rigged == None:
            MyNum = str(random.randint(self.front, self.end))
            Numberlabel = Label(self.ResultFrame, text=MyNum)
            Numberlabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            Mylabel = Label(mastertk, text=self.rigged)
            Mylabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    def number_or_no(myint):
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
    # print(current_screen)
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
