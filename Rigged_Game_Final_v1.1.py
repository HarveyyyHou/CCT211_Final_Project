from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from random import choices
import random
import pandas as pd


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
class Random_Number:

    "Randomly selects a Number"

    def __init__(self):
        self.rigged = []
        self.MyNum = None
        self.frontnum = None
        self.endnum = None
        self.screencontrol = False


    def changescreen(self):
        # if cur screen is normal.
        if self.screencontrol==True :
            self.get_current_values()
            self.rigged=[]
            self.rigfunction()

        #if rig screen
        else:
            entrytext = self.Rigbox.get()
            entrytext = entrytext.split(",")
            for myint in entrytext:
                myint = int(myint)
                if self.front.get() == "" or self.end.get() == "":
                    break
                elif int(self.front.get()) <= myint <= int(self.end.get()):
                    self.rigged.append(myint)
                else:
                    self.rigged = []
            self.Rigbox.pack_forget()
            self.Instruction1.pack_forget()
            self.main_screen()

    def main_screen(self):
        self.screencontrol = True
        self.Spin_Button = Button(mastertk, text='Spin', activebackground="blue",
                                 activeforeground="blue", command=self.spin)
        self.Spin_Button.place(anchor=CENTER,relx=0.7,rely=0.4)

        self.Rigged = Button(mastertk, text="Settings",
                           command=self.changescreen)
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
        if self.frontnum != None:
            self.front.insert(END,self.frontnum)
        if self.endnum != None:
            self.end.insert(END,self.endnum)

    def get_current_values(self):
        if self.front.get()!="":
            self.frontnum = int(self.front.get())
        if self.end.get()!="":
            self.endnum = int(self.end.get())

    def spin(self):
        if self.front.get()=="" or self.end.get()=="":
            return
        elif len(self.rigged)==0:
            self.frontnum = int(self.front.get())
            self.endnum = int(self.end.get())
            self.MyNum = str(random.randint(self.frontnum, self.endnum))
            Numberlabel = Label(self.ResultFrame, text=self.MyNum)
            Numberlabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            myselection = random.choice(self.rigged)
            Numberlabel = Label(self.ResultFrame, text=myselection)
            Numberlabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    def number_or_no(self,myint):
        if myint.isnumeric():
            return True
        # Allows backspace to first character
        elif myint == "":
            return True
        else:
            return False

    def digitorcomma(self,myinput):
        if len(myinput)==0:
            return True
        elif myinput[-1].isdigit() or (","==myinput[-1] and len(myinput)!=1 and myinput[-2]!=","):
            return True
        else:
            return False

    def rigfunction(self):
        self.screencontrol = False
        self.RangeLabel.place_forget()
        self.front.place_forget()
        self.end.place_forget()
        self.ResultFrame.place_forget()
        self.Spin_Button.place_forget()
        self.Save.place_forget()
        self.helplabel.place_forget()
        self.ChosenLabel.place_forget()
        self.Instruction1 = Label(mastertk, text="Enter rigged values in range, seperated by comma.")
        self.Instruction1.pack()
        self.validate_rig = mastertk.register(self.digitorcomma)
        self.Rigbox = Entry(mastertk, width=32, validate="key",validatecommand=(self.validate_rig, '%P'))
        self.Rigbox.pack()



    def history(self):
        print("not implemented yet")
        #last chosen num
        self.myNum
        #last front
        self.frontnum
        #last end
        self.endnum
        pass


class Name_Pick:

    def __init__(self):
        self.text_content = "Name Picker"
        self.label_content = "Names"

        self.userinput = ""
        self.choosen_name = ""

        self.label_names = None
        self.textbox_userinput = None
        self.label_choosen_name = None
        self.textbox_choosen_name = None
        self.button_choose = None
        self.button_settings = None

        self.rigged_names = ""

        self.label_rigged_names = None
        self.textbox_rigged_names = None

     def add_main_screen(self):
        self.label_names = tk.Label(content_frame, text=self.label_content, height=2, width=20)
        self.label_names.pack(pady=1)
        self.textbox_userinput = tk.Text(content_frame, height=10, width=150)
        self.textbox_userinput.insert(tk.END, self.userinput)
        self.textbox_userinput.pack(padx=15, pady=15)
        self.label_choosen_name = tk.Label(content_frame, text="Choosen last name", height=2, width=20)
        self.label_choosen_name.pack(side= LEFT, pady=1)
        self.textbox_choosen_name = tk.Text(content_frame, height=5, width=25)
        self.textbox_choosen_name.insert(tk.END, self.choosen_name)
        #self.textbox_choosen_name.config(state=DISABLED)
        self.textbox_choosen_name.pack(side= LEFT)
        self.button_choose = tk.Button(content_frame, text="Choose", height=5, width=10, command=self.get_random_data)
        self.button_choose.pack(side = LEFT, padx=100, pady=5)
        self.button_settings = tk.Button(content_frame, text="Settings", height=1, width=10, command=self.open_settings_screen)
        self.button_settings.pack(side=BOTTOM, anchor="e", padx=5, pady=5)
        content_frame.pack(fill = "both", expand = True, padx= 5, pady= 5)

    def add_settings_screen(self):
        self.label_rigged_names = tk.Label(content_frame, text="Enter names for rigged outcomes", height=2, width=40)
        self.label_rigged_names.pack(pady=1)
        self.textbox_rigged_names = tk.Text(content_frame, height=10, width=150)
        self.textbox_rigged_names.insert(tk.END, self.rigged_names)
        self.textbox_rigged_names.pack(padx=15, pady=15)
        self.button_return = tk.Button(content_frame, text="Return", height=1, width=10, command=self.open_main_screen)
        self.button_return.pack(side=BOTTOM, anchor="e", padx=5, pady=5)
        content_frame.pack(fill = "both", expand = True, padx= 5, pady= 5)

    def get_settings_screen_existing_values(self):
        if self.textbox_rigged_names:
            self.rigged_names = self.textbox_rigged_names.get("1.0",END)

    def get_main_screen_existing_values(self):
        if self.textbox_userinput and self.textbox_choosen_name:
            self.userinput = self.textbox_userinput.get("1.0",END)
            self.choosen_name = self.textbox_choosen_name.get("1.0",END)

    def open_main_screen(self):
        self.get_settings_screen_existing_values()
        clear_frame()
        self.add_main_screen()

    def open_settings_screen(self):
        self.get_main_screen_existing_values()
        clear_frame()
        self.add_settings_screen()

    def get_random_data(self):
        self.get_main_screen_existing_values()
        rigged = self.rigged_names.strip().split(",")
        userinput_names = self.userinput.strip().split(",")
        if len(userinput_names)==0 or userinput_names[0] == "":
            return
        picked_name = None
        if len(rigged)!=0 and self.rigged_names!=" " and rigged[0]!="":
            picked_name = rigged[0]
            self.textbox_choosen_name.delete("1.0",END)
            self.textbox_choosen_name.insert(END, picked_name)
            rigged = rigged[1:]
            self.rigged_names = ",".join(rigged)
            userinput_names = self.userinput.strip().split(",")
            for i in range (len(userinput_names)):
                userinput_names[i] = userinput_names[i].strip()
            if picked_name in userinput_names:
                userinput_names.remove(picked_name)
                self.textbox_userinput.delete("1.0",END)
                self.textbox_userinput.insert(END, ", ".join(userinput_names))
        else:
            picked_name = ""
            userinput_names = self.userinput.strip().split(",")
            for i in range (len(userinput_names)):
                userinput_names[i] = userinput_names[i].strip()
            if len(userinput_names) != 0 and userinput_names[0]!='':
                index = random.randint(0,len(userinput_names)-1)
                picked_name = userinput_names[index]
                userinput_names.remove(picked_name)
                self.textbox_userinput.delete("1.0",END)
                self.textbox_userinput.insert(END, ", ".join(userinput_names))
            else:
                self.textbox_userinput.delete("1.0",END)
            self.textbox_choosen_name.delete("1.0",END)
            self.textbox_choosen_name.insert(END, picked_name)
            
    def choose(self):
        pass

class Rigged(tk.Frame):
    def __init__(self):
        pass

class Generate_History:
    '''
    Save the current settings in History via Panda
    '''
def csv_display():
    myfields = ['Game_Type', 'Rigged_Settings','Normal_Settings','Results']
    myrecord = pd.read_csv('Game_History.csv',skipinitialspace=True, usecols=myfields)
    Game_list = myrecord.Game_Type.tolist()
    Rigged_list = myrecord.Game_Type.tolist()
    Normal_list = myrecord.Normal_Setting.tolist()
    Results_list = myrecord.Results.tolist()

# Screen is 0 by default(which is dice)
# current_screen is a global var that determines what screen the user is on
# clicking on the buttons in the row changes to 0,1,2 respectively
# 0 = dice, 1 = RNG, 2 = name picker, 3=History
current_screen = 0
def switch_screen(screen):
    global current_screen
    if screen==current_screen==1:
        pass
    elif screen==1:
        Random_Number().main_screen()
    if screen==3:
        csv_display()
    current_screen = screen

mastertk = Tk()

mastermenu = Menu(mastertk)
mastermenu.add_cascade(label="Dice", command=lambda: switch_screen(0))
mastermenu.add_cascade(label="Number_Generator", command=lambda: switch_screen(1))
mastermenu.add_cascade(label="NamePicker", command=lambda: switch_screen(2))

mastertk.geometry("300x300")
mastertk.config(menu=mastermenu)

dice = Dice()
dice.defaultscreen()
namepicker = Name_Pick()

mastertk.mainloop()
