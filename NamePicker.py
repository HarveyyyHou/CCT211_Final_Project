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
        self.text_content = "Name Picker"
        self.label_content = "Names"
        print("hi1")

    def choose(self):
        pass

    def add_screen(self):
        label = tk.Label(content_frame, text=self.label_content, height=2, width=70)
        label.pack(pady=1)
        textbox = tk.Text(content_frame, height=10, width=50)
        textbox.insert(tk.END, self.text_content)
        textbox.pack(padx=5, pady=5)
        label2 = tk.Label(content_frame, text=self.label_content, height=2, width=70)
        label2.pack(pady=1)
        button1 = tk.Button(content_frame, text="Choose", height=1, width=10, command=get_random_data)
        button1.pack(side = LEFT, padx=3, pady=2)
        button2 = tk.Button(content_frame, text="Settings", height=1, width=10, command=open_settings)
        button2.pack(side= RIGHT, padx=1, pady=2)
        content_frame.pack(fill = "both", expand = True, padx= 5, pady= 5)

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
  print("hi")
  clear_frame()
  namepicker.add_screen()

def open_dice_screen():  
  print("hi2")
  clear_frame()


def clear_frame():
  for contecnt in content_frame.winfo_children():
    contecnt.destroy()    

global mastertk
global namepicker
global content_frame

mastertk = Tk()
mastermenu = Menu(mastertk)
mastermenu.add_cascade(label="Dice", command=open_dice_screen)
mastermenu.add_cascade(label="Number_Generator")
mastermenu.add_cascade(label="NamePicker", command = open_name_picker_screen)

mastertk.geometry("300x300")
mastertk.config(menu=mastermenu)
content_frame = tk.Frame(mastertk)
content_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

namepicker = Name_Pick()
dicepicker = Dice()

mastertk.mainloop()