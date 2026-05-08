from tkinter import *
from subprocess import call

class Main_Window:
    def __init__(GUI0):
        # Window Maker
        GUI0.window0 = Tk()
        GUI0.window0.title("Speed Typing Game")
        GUI0.window0.iconbitmap("Icon.ico")
        GUI0.window0.geometry("900x600+250+50")
        GUI0.window0.resizable(0, 0)

        #Cover Image
        background = PhotoImage(file = "background.png")
        bg_label = Label(GUI0.window0, image = background)
        bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        # Title
        Title = Label(GUI0.window0, text = "Congrats,You Have Made It|", bg = "#286ED3", font = ("Comic Sans MS", 40, "bold"), width = 23, fg = "white")
        Title.place(x = 90, y = 145)

        # Logo Image
        logo_image = PhotoImage(file="star.png")
        logo_label = Label(GUI0.window0, image=logo_image, bg="#286ED3")
        logo_label.place(x = 310, y = 221)

        def home():
            GUI0.window0.destroy()
            call(["python", "Main_Window.py"])
        
        # Home Image
        home_image = PhotoImage(file="Home.png")
        # Home Button
        home_button = Button(GUI0.window0, text="Home", command=home, image=home_image, compound=LEFT, bg="White", font=("Comic Sans MS", 15, "bold"), width=100, fg="Black")
        home_button.place(x=10, y=10)

        GUI0.window0.mainloop()

Main_Window()
