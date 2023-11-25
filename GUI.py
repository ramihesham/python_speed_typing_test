import tkinter as tk
from tkinter import *
import random
class expertlevel:
    def __init__(gui3):
        gui3.window = tk.Tk()
        gui3.window.iconbitmap('icon.ico')
        gui3.window.geometry('1000x600+250+125')
        gui3.window.resizable(0, 0)
        gui3.window.title("speed typing application  (expert level) ")
        gui3.window.config(bg='cyan3')
        gui3.paragraphs = open('text.txt', 'r').read().split('*')
        gui3.paragraph_to_be_written = tk.Label(gui3.window, text=random.choice(gui3.paragraphs), font=('black cpper', 12, 'italic bold'),  bg='cyan3', fg='DeepSkyBlue4')
        gui3.paragraph_to_be_written.grid(padx=40, pady=140)
        timepic = PhotoImage(file='time.png')
        timelabel = Label(gui3.window, image=timepic, bg='cyan3')
        timelabel.place(x=725, y=125)
        header = Label(gui3.window, text='WELCOME BACK! (ARE YOU READY FOR THE EXPERT LEVEL ?)', bg='cyan3',
                       font=('Comic Sans MS', 20, 'bold'), fg='Green')
        header.place(x=80, y=50)
        gui3.window.mainloop()
expertlevel()
