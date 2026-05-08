from tkinter import *
from subprocess import call


class Main_Window:
    # Variables
    sliding_words = ""
    count = 0

    def __init__(GUI0):
        # Window Maker
        GUI0.window0 = Tk()
        GUI0.window0.title("Speed Typing Game")
        GUI0.window0.iconbitmap("Icon.ico")
        GUI0.window0.geometry("900x600+250+50")
        GUI0.window0.resizable(0, 0)

        # Cover Image
        background = PhotoImage(file="background.png")
        bg_label = Label(GUI0.window0, image=background)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title
        GUI0.Title = Label(GUI0.window0, text="", bg="#286ED3", font=("Comic Sans MS", 25, "bold"), width=35,
                           fg="white")
        GUI0.Title.place(x=80, y=90)

        def english():
            GUI0.window0.destroy()
            call(["python", "Level_01English.py"])

        def arabic():
            GUI0.window0.destroy()
            call(["python", "Level_01Arabic.py"])

        def start():
            start_button.destroy()
            english_button = Button(GUI0.window0, text="English", command=english, bg="White",
                                    font=("Comic Sans MS", 25, "bold"), width=10, fg="Black")
            english_button.place(x=150, y=400)
            arabic_button = Button(GUI0.window0, text="Arabic", command=arabic, bg="White",
                                   font=("Comic Sans MS", 25, "bold"), width=10, fg="Black")
            arabic_button.place(x=550, y=400)

        # Start Button
        start_button = Button(GUI0.window0, text="START", command=start, bg="White", font=("Comic Sans MS", 25, "bold"),
                              width=10, fg="Black")
        start_button.place(x=343, y=400)

        GUI0.Tile_Slider()
        GUI0.window0.mainloop()

    def Tile_Slider(GUI0):
        text = "Welcome To The Speed Typing Game"
        if Main_Window.count >= len(text):
            Main_Window.count = 0
            Main_Window.sliding_words = ""
        Main_Window.sliding_words += text[Main_Window.count]
        GUI0.Title.config(text=Main_Window.sliding_words)
        Main_Window.count += 1
        GUI0.window0.after(250, GUI0.Tile_Slider)


Main_Window()