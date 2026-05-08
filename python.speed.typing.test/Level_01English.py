from tkinter import *
import random
from subprocess import call

class Level01:

    def start_timer(GUI1, event):
            if GUI1.time_left == 60:
                GUI1.timer()

    def __init__(GUI1):
        # Variables
        GUI1.i = 0
        GUI1.time_left = 60
        GUI1.correct_word = 0
        GUI1.wrong_word = 0

        # Window Maker
        GUI1.window = Tk()
        GUI1.window.title("Speed Typing Game <-- level 01 -->")
        GUI1.window.iconbitmap("Icon.ico")
        GUI1.window.geometry("900x600+250+50")
        GUI1.window.resizable(0, 0)

        # Cover Image
        background = PhotoImage(file="background.png")
        bg_label = Label(GUI1.window, image=background)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Logo Image
        GUI1.logo_image = PhotoImage(file="alarm.png")
        GUI1.logo_label = Label(GUI1.window, image=GUI1.logo_image, bg="#286ED3")

        # Title
        GUI1.Title = Label(GUI1.window, text="--- Welcome To level 01 ---", bg="#286ED3", font=("Comic Sans MS", 25, "bold"), width=35, fg="white")
        GUI1.Title.place(x=80, y=90)

        # Words To Be Written
        GUI1.words = open("Words_English.txt", "r").read().split("\n")
        GUI1.words_written = Label(GUI1.window, text=random.choice(GUI1.words), font=("black copper", 35, "bold"), bg="#286ED3", fg="white")
        GUI1.words_written.place(x=440, y=400, anchor=CENTER)

        # Words Label
        GUI1.word_label = Label(GUI1.window, text="Words", font=("Casteller", 28, "bold"), bg="#286ED3", fg="white")
        GUI1.word_label.place(x=80, y=150)

        # Words Counter
        GUI1.word_counter = Label(GUI1.window, text=GUI1.i, font=("Casteller", 28, "bold"), bg="#286ED3", fg="white")
        GUI1.word_counter.place(x=120, y=220)

        # Timer Label
        GUI1.timer_label = Label(GUI1.window, text="Timer", font=("Casteller", 28, "bold"), bg="#286ED3", fg="white")
        GUI1.timer_label.place(x=728, y=150)

        # Timer Counter
        GUI1.timer_counter = Label(GUI1.window, text=GUI1.time_left, font=("Casteller", 28, "bold"), bg="#286ED3", fg="white")
        GUI1.timer_counter.place(x=760, y=220)

        # Word Entry Text Box
        GUI1.text_box = Entry(GUI1.window, font=("arial", 25, "bold"), bd=8, justify=CENTER)
        GUI1.text_box.place(x=258, y=450)
        GUI1.text_box.focus_set()

        # Instructions
        GUI1.instruction = Label(GUI1.window, text="Type in the word and press ENTER", font=("Chiller", 28, "bold"), bg="#286ED3", fg="white")
        GUI1.instruction.place(x=445, y=320, anchor=CENTER)

        # Crying Emoji
        GUI1.crying_emoji = PhotoImage(file="bad.png")
        
        # Pro Emoji
        GUI1.pro_emoji = PhotoImage(file="pro.png")
        
        # Smile Emoji
        GUI1.smile_emoji = PhotoImage(file="good.png")
        
        GUI1.score_label_1 = Label(GUI1.window, bg="#286ED3")
        GUI1.score_label_1.place(x=100, y=130)
        
        GUI1.score_label_2 = Label(GUI1.window, bg="#286ED3")
        GUI1.score_label_2.place(x=730, y=130)

        def home():
            GUI1.window.destroy()
            call(["python", "Main_Window.py"])
        
        def retry():
            GUI1.window.destroy()
            call(["python", "Level_01English.py"])
        
        def next_level():
            GUI1.window.destroy()
            call(["python", "Level_02English.py"])
        
        # Next Image
        GUI1.next_image = PhotoImage(file="Next.png")
        # Next Level Button
        GUI1.next_level_button = Button(GUI1.window, text="NEXT", command=next_level, image=GUI1.next_image, compound=LEFT, bg="White", font=("Comic Sans MS", 15, "bold"), width=100, fg="Black")
        
        # Retry Image
        GUI1.retry_image = PhotoImage(file="Retry.png")
        # Retry Button
        GUI1.retry_button = Button(GUI1.window, text="Retry", command=retry, image=GUI1.retry_image, compound=RIGHT, bg="White", font=("Comic Sans MS", 15, "bold"), width=100, fg="Black")
        
        # Home Image
        home_image = PhotoImage(file="Home.png")
        # Home Button
        home_button = Button(GUI1.window, text="Home", command=home, image=home_image, compound=LEFT, bg="White", font=("Comic Sans MS", 15, "bold"), width=100, fg="Black")
        home_button.place(x=10, y=10)
        
        GUI1.window.bind("<KeyPress>", GUI1.start_timer)
        GUI1.window.bind("<Return>", GUI1.x)
        GUI1.window.mainloop()

    def timer(GUI1):
        if GUI1.time_left <= 11:
            GUI1.timer_counter.config(fg='red')
        if GUI1.time_left > 0:
            GUI1.time_left -= 1
            GUI1.timer_counter.config(text=GUI1.time_left)
            GUI1.timer_counter.after(1000, GUI1.timer)
        else:
            GUI1.text_box.destroy()
            GUI1.Title.destroy()
            GUI1.words_written.destroy()
            GUI1.word_label.destroy()
            GUI1.word_counter.destroy()
            GUI1.timer_label.destroy()
            GUI1.timer_counter.destroy()
            
            GUI1.logo_label.place(x=310, y=1)
            
            new_title = Label(GUI1.window, text="TIME IS UP", bg="#286ED3", font=("Comic Sans MS", 50, "bold"), fg="white")
            new_title.place(x=240, y=255)
            
            result = GUI1.correct_word - GUI1.wrong_word
            
            GUI1.instruction.config(text=f"Correct Words: {GUI1.correct_word}\n Wrong Words: {GUI1.wrong_word}\n Final Score: {result}")
            GUI1.instruction.place(x=445, y=430, anchor=CENTER)
            
            if result < 9:
                GUI1.score_label_1.config(image=GUI1.crying_emoji)
                GUI1.score_label_2.config(image=GUI1.crying_emoji)
                # Retry Button
                GUI1.retry_button.place(x=785, y=10)
            elif result > 19:
                GUI1.score_label_1.config(image=GUI1.pro_emoji)
                GUI1.score_label_2.config(image=GUI1.pro_emoji)
                # Next Level Button
                GUI1.next_level_button.place(x=785, y=10)
            else:
                GUI1.score_label_1.config(image=GUI1.smile_emoji)
                GUI1.score_label_2.config(image=GUI1.smile_emoji)
                # Next Level Button
                GUI1.next_level_button.place(x=785, y=10)

    def x (GUI1, event):
        user_input = GUI1.text_box.get()
        
        if user_input:
            GUI1.i += 1
            GUI1.word_counter.config(text=GUI1.i)
            GUI1.instruction.config(text='')
            correct_words = GUI1.words_written["text"]
            
            if user_input.lower() == correct_words.lower():
                GUI1.correct_word += 1
            else:
                GUI1.wrong_word += 1
            
            random.shuffle(GUI1.words)
            GUI1.words_written.config(text=GUI1.words[0])
            GUI1.text_box.delete(0, END)

Level01()
