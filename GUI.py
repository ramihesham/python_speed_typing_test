import tkinter as tk
from tkinter import *
import random

n = 0
time_left = 60


class expertlevel:

    def __init__(gui3):
        gui3.window = tk.Tk()
        gui3.window.iconbitmap('icon.ico')
        gui3.window.geometry('1000x600+250+125')
        gui3.window.resizable(0, 0)
        gui3.window.title("speed typing application  (expert level) ")
        gui3.window.config(bg='cyan3')
        gui3.paragraphs = open('text.txt', 'r').read().split('*')
        gui3.paragraph_to_be_written = tk.Label(gui3.window, text=random.choice(gui3.paragraphs),
                                                font=('Arial', 14, 'italic bold'), bg='cyan3', fg='DeepSkyBlue4')
        gui3.paragraph_to_be_written.place(x=40, y=150)
        textbox = Text(gui3.window, width=60, height=10, font=('Arial', 14, 'italic bold'), bg='cyan1',
                       fg='DeepSkyBlue4')
        textbox.place(x=25, y=300)
        textbox.focus_set()
        timepic = PhotoImage(file='time.png')
        timelabel = Label(gui3.window, image=timepic, bg='cyan3')
        timelabel.place(x=750, y=150)
        header = Label(gui3.window, text='WELCOME BACK! (ARE YOU READY FOR THE EXPERT LEVEL ?)', bg='cyan3',
                       font=('Comic Sans MS', 20, 'bold'), fg='Green')
        header.place(x=80, y=20)
        timer = Label(gui3.window, text='TIMER', bg='cyan3', font=('Comic Sans MS', 24, 'bold'), fg='Green')
        timer.place(x=700, y=80)
        time_counter = Label(gui3.window, text='60', bg='cyan3', font=('Comic Sans MS', 24, 'bold'), fg='Green')
        time_counter.place(x=850, y=80)
        paragraphs = Label(gui3.window, text='Paragraphs', bg='cyan3', font=('Comic Sans MS', 24, 'bold'), fg='Green')
        paragraphs.place(x=165, y=80)
        instruction = Label(gui3.window, text=' The time starts once you start typing, press (+) to count what you wrote and display new paragraph', bg='cyan3', font=('chiller', 22, 'bold'), fg='Green')
        instruction.place(x=10, y=550)
        paragraphs_counter = Label(gui3.window, text=n, bg='cyan3', font=('Comic Sans MS', 24, 'bold'), fg='Green')
        paragraphs_counter.place(x=400, y=80)
        def time():
            global time_left
            if time_left > 0:
                time_left -= 1
                time_counter.config(text=time_left)
                time_counter.after(1000, time)
                instruction.config(text='')
            else:
                textbox.config(state=DISABLED)

        def time_start(time_starts_after_pressing_any_key):
            if time_left == 60:
                time()
        def start(starting):
            global n
            n += 1
            paragraphs_counter.config(text=n)
            random.shuffle(gui3.paragraphs)
            gui3.paragraph_to_be_written.config(text=gui3.paragraphs[0])
            textbox.delete(1.0, END)

        gui3.window.bind('<KeyPress>', time_start)
        gui3.window.bind('<plus>', start)
        gui3.window.mainloop()

expertlevel()
