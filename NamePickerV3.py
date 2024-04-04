from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import tkinter.ttk as ttk
import random

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

def get_random_data():
    pass

def open_settings():
    pass

class Rigged(tk.Frame):
    def __init__(self):
        pass


class Generate_History:
    '''
    Save the current settings in History via Panda
    '''

def open_name_picker_screen():  
    namepicker.open_main_screen()

def open_dice_screen():  
  clear_frame()


def clear_frame():
  for contecnt in content_frame.winfo_children():
    contecnt.destroy()    

global mastertk
global namepicker
global content_frame

mastertk = Tk()
mastermenu = Menu(mastertk)
mastermenu.add_cascade(label="Dice", command = open_dice_screen)
mastermenu.add_cascade(label="Number_Generator")
mastermenu.add_cascade(label="NamePicker", command = open_name_picker_screen)

mastertk.geometry("800x800")
mastertk.config(menu=mastermenu)
content_frame = tk.Frame(mastertk)
content_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

namepicker = Name_Pick()
dicepicker = Dice()

mastertk.mainloop()