from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import tkinter.ttk as ttk
import random
from PIL import ImageTk, Image
from random import choices

class Dice:
    def __init__(self):
        # declare the variables needed for the Dice screen
        self.dicepiclist = []

        self.visiblerig = False

        #image variable
        self.dicepic = None

        #the labels for the interface
        self.dicelabel = None

        self.spinbutton = None

        self.settingsbutton = None

        self.listdicelbl = []
        self.listdicetxt = []

    def defaultscreen(self):
        # declare the variables needed for the Dice screen
        self.dicepiclist = []
        for picnum in range(1, 7):
            self.dicepiclist.append(ImageTk.PhotoImage(Image.open(f"dice{picnum}.png").resize((150, 150))))

        self.visiblerig = False

        #image variable
        self.dicepic = self.dicepiclist[0]

        #the labels for the interface

        self.dicelabel = Label(mastertk, image=self.dicepic, justify=CENTER)
        self.dicelabel.place(relx = 0.28, rely = 0.5, anchor = 'center')

        self.spinbutton = Button(mastertk, text = "SPIN!", borderwidth=5, relief="raised", justify=CENTER, font=("impact",20), width = 7, command = self.roll)
        self.spinbutton.place(relx = 0.77, rely = 0.65, anchor='center')

        self.settingsbutton = Button(mastertk, text = "SETTINGS", borderwidth=3, relief='ridge', justify=CENTER, font=("impact", 10), width = 10, command=self.displaysettings)
        self.settingsbutton.place(relx = 1, rely = 1, anchor = tk.SE)

        self.validation = mastertk.register(self.validatenum)

        self.listdicelbl = []
        self.instructionlabel = Label(text = "Input percentage of chance.\nOrders 1 - 6")
        self.listprelabelnum = []
        self.listpercentage = []

        for num in range(1, 7):
            self.listdicelbl.append(Entry(mastertk, validate="key", validatecommand=(self.validation, '%P'), width=5))
            self.listprelabelnum.append(Label(text = str(num) + "."))
            self.listpercentage.append(Label(text="%"))

    def validatenum(self,myint):
        if myint.isdigit():
            if int(myint)>=0:
                return True
            else:
                return False
        # Allows backspace to first character
        elif myint == "":
            return True
        else:
            return False


    def displaysettings(self):
        tempy = 0.1

        if not self.visiblerig:
            for num in range(0, 6):
                self.listdicelbl[num].place(relx = 0.66, rely = tempy)
                self.instructionlabel.place(relx = 0.02, rely=0.08)
                self.listprelabelnum[num].place(relx = 0.6, rely = tempy)
                self.listpercentage[num].place(relx = 0.78, rely = tempy)
                tempy += 0.07

                self.visiblerig = True

        else:
            for num in range(0, 6):
                self.listdicelbl[num].place_forget()
                self.instructionlabel.place_forget()
                self.listprelabelnum[num].place_forget()
                self.listpercentage[num].place_forget()
                self.visiblerig = False


    def changeimage(self, num):
        self.dicepic = self.dicepiclist[num-1]

        #output the image
        self.dicelabel.config(image=self.dicepic)

    def roll(self):
        #if there are no rigs at all just roll randomly
        #if there is only some rigged
        #if there is all rigged
        listrignum = []
        countvalues = 0
        validcheck = True
        for myentry in self.listdicelbl:
            #if there is nothing in the textbox just put 0 in the list
            if myentry.get() == '0':
                listrignum.append(0)
                #txtbox.config(bg = "blue")
            elif myentry.get() == "" or myentry.get() == '':
                # print("!!!??")
                myentry.insert(0,"0")
                listrignum.append(0)
            #if there is a number in the textbox put the number in the list
            else:
                myprob = int(myentry.get())
                listrignum.append(myprob)
                #txtbox.config(bg = "blue")
                countvalues += myprob



        numcount = 0

            #if all the numbers are just 0 then it's an equal spin
        # print(listrignum)
        #if the values are over 100 it is false and it if is below 0 it is false
        if countvalues > 100 or countvalues < 0:
            # print('not good')
            validcheck = False

        numcount = 0
        #do the actual calculation
        if validcheck:
            #if all the numbers are just 0 then it's an equal spin
            for num in range(len(listrignum)):
                if listrignum[num] != 0:
                    numcount += 1

            if numcount == 0:
                self.changeimage(random.randint(1,6))
            else:
                mychoice = choices([1,2,3,4,5,6],listrignum)
                self.changeimage(mychoice[0])


        #check the list of all the stuff

    def displayrig(self):
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

#global current_screen
dice = Dice()
dice.defaultscreen()

mastertk.mainloop()


