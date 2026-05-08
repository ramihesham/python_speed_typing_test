from tkinter import *
import random
from subprocess import call

i = 0
time_left = 60
correct_paragraph = 0
wrong_paragraph = 0

class level_03:
    def __init__(GUI3):
        # Window Maker
        GUI3.window = Tk()
        GUI3.window.title("<-- لعبة سرعة الكتابة <-- المستوى ٣")
        GUI3.window.iconbitmap("Icon.ico")
        GUI3.window.geometry("900x600+250+50")
        GUI3.window.resizable(0, 0)

        # Cover Image
        background = PhotoImage(file="background.png")
        bg_label = Label(GUI3.window, image=background)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Logo Image
        logo_image = PhotoImage(file="alarm.png")
        logo_label = Label(GUI3.window, image=logo_image, bg="#286ED3")

        # Title
        Title = Label(GUI3.window, text=' الثالث المستوى في بك ومرحبًا ,! تهانينا  ', bg="#286ED3", font=("Comic Sans MS", 25, "bold"), width=35, fg="white")
        Title.place(x=80, y=80)

        # paragraphs To Be Written
        with open("paragraphs_Arabic.txt", "r", encoding = "utf-8") as file: GUI3.paragraphs = file.read().split('\n\n\n')
        GUI3.paragraphs_written = Label(GUI3.window, text=random.choice(GUI3.paragraphs), font=("black copper", 11, "bold"), bg="#286ED3", fg="white")
        GUI3.paragraphs_written.place(x=440, y=380, anchor=CENTER)

        # paragraphs Label
        paragraph_label = Label(GUI3.window, text="الفقرات", font=("Casteller", 28, "bold"), bg="#286ED3", fg="white")
        paragraph_label.place(x=90, y=150)

        # paragraphs Counter
        paragraph_counter = Label(GUI3.window, text=i, font=("Casteller", 28, "bold"), bg="#286ED3", fg="white")
        paragraph_counter.place(x=120, y=220)

        # Time Label
        timer_label = Label(GUI3.window, text="الوقت", font=("Casteller", 28, "bold"), bg="#286ED3", fg="white")
        timer_label.place(x=720, y=150)

        # Timer Counter
        timer_counter = Label(GUI3.window, text=time_left, font=("Casteller", 28, "bold"), bg="#286ED3", fg="white")
        timer_counter.place(x=735, y=220)

        # paragraph Entry Text Box
        text_box = Text(GUI3.window, width=40, height=5, font=("arial", 12, "bold"), bd=8, wrap=WORD)
        text_box.place(x=258, y=450)
        text_box.focus_set()

        # Instructions
        instruction = Label(GUI3.window, text = '   أو للبدء + على اضغط و الفقرة اكتب ENTER جديد سطر للحصول على', font=("Chiller", 20, "bold"), bg="#286ED3", fg="white")
        instruction.place(x=450, y=310, anchor=CENTER)

        # Crying Emoji
        crying_emoji = PhotoImage(file="bad.png")
        
        # Pro Emoji
        pro_emoji = PhotoImage(file="pro.png")
        
        # smile Emoji
        smile_emoji = PhotoImage(file="good.png")
        
        emoji_label_1 = Label(GUI3.window, bg="#286ED3")
        emoji_label_1.place(x=100, y=130)
        
        emoji_label_2 = Label(GUI3.window, bg="#286ED3")
        emoji_label_2.place(x=730, y=130)

        def home():
            GUI3.window.destroy()
            call(["python", "Main_Window.py"])
        
        def retry():
            GUI3.window.destroy()
            call(["python", "Level_03Arabic.py"])
        
        def next_level():
            GUI3.window.destroy()
            call(["python", "END GAME.py"])
        
        # Next Image
        next_image = PhotoImage(file="Next.png")
        # Next Level Button
        next_level_button = Button(GUI3.window, text="التالى", command=next_level, image=next_image, compound=LEFT, bg="White", font=("Comic Sans MS", 15, "bold"), width=100, fg="Black")
        
        # Retry Image
        retry_image = PhotoImage(file="Retry.png")
        # Retry Button
        retry_button = Button(GUI3.window, text="اعادة", command=retry, image=retry_image, compound=RIGHT, bg="White", font=("Comic Sans MS", 15, "bold"), width=100, fg="Black")
        
        # Home Image
        home_image = PhotoImage(file="Home.png")
        # Home Button
        home_button = Button(GUI3.window, text="رجوع", command=home, image=home_image, compound=LEFT, bg="White", font=("Comic Sans MS", 15, "bold"), width=100, fg="Black")
        home_button.place(x=10, y=10)

        def timer():
            global time_left
            if time_left < 11:
                timer_counter.config(fg='red')
            if time_left > 0:
                time_left -= 1
                timer_counter.config(text=time_left)
                timer_counter.after(1000, timer)
            else:
                text_box.destroy()
                paragraph_counter.destroy()
                Title.destroy()
                GUI3.paragraphs_written.destroy()
                paragraph_label.destroy()
                paragraph_counter.destroy()
                timer_label.destroy()
                timer_counter.destroy()

                logo_label.place(x=310, y=10)
                new_title = Label(GUI3.window, text="الوقت انتهى لقد", bg="#286ED3", font=("Comic Sans MS", 50, "bold"), fg="white")
                new_title.place(x=280, y=280)

                result = correct_paragraph - wrong_paragraph
                instruction.config(text = f"{correct_paragraph} :صحيحة فقرات \n {wrong_paragraph} :خاطئة فقرات\n {result} :النهائية النتيجة")
                instruction.place(x=445, y=440, anchor=CENTER)

                if result < 3:
                    emoji_label_1.config(image=crying_emoji)
                    emoji_label_2.config(image=crying_emoji)
                    # Retry Button
                    retry_button.place(x=785, y=10)
                elif result > 5:
                    emoji_label_1.config(image=pro_emoji)
                    emoji_label_2.config(image=pro_emoji)
                    # Next Button
                    next_level_button.place(x=785, y=10)
                else:
                    emoji_label_1.config(image=smile_emoji)
                    emoji_label_2.config(image=smile_emoji)
                    # Next Button
                    next_level_button.place(x=785, y=10)

        def time_start(time_starts_after_pressing_any_key):
            if time_left == 60:
                timer()

        def x(event):
            global i, correct_paragraph, wrong_paragraph

            typed_paragraph = text_box.get("1.0", "end-1c").rstrip('+')

            if not typed_paragraph:
                return
            
            
            i += 1
            paragraph_counter.config(text=i)
            instruction.config(text="")

            typed_paragraph = text_box.get("1.0", "end-1c").rstrip('+')
            if typed_paragraph.lower() == GUI3.paragraphs_written["text"].lower():
                correct_paragraph += 1
            else:
                wrong_paragraph += 1

            random.shuffle(GUI3.paragraphs)
            GUI3.paragraphs_written.config(text=GUI3.paragraphs[0])
            text_box.delete("1.0", "end-1c")

        GUI3.window.bind('<KeyPress>', time_start)
        GUI3.window.bind("<plus>", x)
        GUI3.window.mainloop()

level_03()
