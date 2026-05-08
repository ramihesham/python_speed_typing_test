from tkinter import *
import random
from subprocess import call

class Level02:

    def start_timer(self, event):
        if self.timeleft == 60:
            self.game_timer()

    def __init__(self):
        #window maker
        self.gui = Tk()  # Change the variable name from boom to gui
        self.gui.geometry('900x600+250+50')
        self.gui.title("<-- لعبة الكتابة السريعة < -- المستوى ٢ ")
        self.gui.iconbitmap('Icon.ico')
        self.gui.resizable(0, 0)

        #Cover Image
        background = PhotoImage(file = "background.png")
        bg_label = Label(self.gui, image = background)
        bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        # Logo Image
        self.logo_image = PhotoImage(file = "alarm.png")
        self.logo_label = Label(self.gui, image = self.logo_image, bg = "#286ED3")

        self.sentences = [
            ' الدالة هي مجموعة من الشيفرة القابلة لإعادة الاستخدام',
            'المتغير هو مكان في الذاكرة محجوز لتخزين البيانات',
            'تُستخدم القوائم لتخزين عدة عناصر في متغير واحد',
            'حمل الولد حقيبته وذهب إلى المدرسة',
            'البرمجة مهارة أساسية لجميع المهندسين',
            'يعيش في المزرعة حيوانات وطيور كثيرة',
            'تستخدم عبارة العودة لإرجاع القيم من الدالة',
            'الثلج يغطي الأرض في فصل الشتاء',
            'ترك العصفور عشه وطار في الجو',
            'الكلب يلعب مع صاحبه في الحديقة',
            'الفتاة تحضر حفلة موسيقية مع صديقتها',
            'الأطفال يلعبون معا في الحديقة',
            'الفريق يفوز بالمباراة الرياضية'
        ]

        self.score = 0
        self.miss = 0
        self.i = 0
        self.timeleft = 60

        self.wordlabel = Label(self.gui, text='', font = ("black copper", 25, "bold"), bg = "#286ED3", fg = "white")
        self.wordlabel.place(x=440, y=400, anchor=CENTER)

        self.title = Label(self.gui, text=' الثاني المستوى في بك ومرحبًا ,! تهانينا  ', bg="#286ED3", font=("Comic Sans MS", 25, "bold"), width=35, fg="white")
        self.title.place(x=80, y=80)

        self.scorelabel = Label(self.gui, text='الجمل', font = ("Casteller", 28, "bold"), bg = "#286ED3", fg = "white")
        self.scorelabel.place(x=90, y=150)

        self.scorelabelcount = Label(self.gui, text=self.i, font = ("Casteller", 28, "bold"), bg = "#286ED3", fg = "white")
        self.scorelabelcount.place(x=110, y=220)

        self.timelabel = Label(self.gui, text='الوقت', font = ("Casteller", 28, "bold"), bg = "#286ED3", fg = "white")
        self.timelabel.place(x=735, y=150)

        self.timelabelcount = Label(self.gui, text=self.timeleft, font = ("Casteller", 28, "bold"), bg = "#286ED3", fg = "white")
        self.timelabelcount.place(x=750, y=220)

        self.gameplay_detaillabel = Label(self.gui, text='   للبدء ENTER  على اضغط و الجملة اكتب', font = ("Chiller", 25, "bold"), bg = "#286ED3", fg = "white")
        self.gameplay_detaillabel.place(x = 445, y = 320, anchor = CENTER)

        self.wordEntry = Entry(self.gui, font=('arial', 25), bd='8', justify=CENTER)
        self.wordEntry.place(x = 258, y = 450)
        self.wordEntry.focus_set()

        self.badpic = PhotoImage(file='bad.png')
        self.goodpic = PhotoImage(file='good.png')
        self.propic = PhotoImage(file='pro.png')

        self.wowLabel = Label(self.gui, bg='#286ED3')
        self.wowLabel.place(x=100, y=130)

        self.wow1Label = Label(self.gui, bg='#286ED3')
        self.wow1Label.place(x=730, y=130)

        def home():
            self.gui.destroy()
            call(["python", "Main_Window.py"])
        
        def retry():
            self.gui.destroy()
            call(["python", "Level_02Arabic.py"])
        
        def next_level():
            self.gui.destroy()
            call(["python", "Level_03Arabic.py"])
        
        #Next Image
        self.next_image = PhotoImage(file="Next.png")
        #Next Level Button
        self.next_level_button = Button(self.gui, text = "التالى", command = next_level, image = self.next_image, compound=RIGHT, bg="White", font=("Comic Sans MS", 15, "bold"), width=100, fg="Black")
        
        #Retry Image
        self.retry_image = PhotoImage(file="Retry.png")
        #Retry Button
        self.retry_button = Button(self.gui, text = "اعادة", command = retry, image = self.retry_image, compound=RIGHT, bg="White", font=("Comic Sans MS", 15, "bold"), width=100, fg="Black")
        
        #Home Image
        home_image = PhotoImage(file="Home.png")
        #Home Button
        home_button = Button(self.gui, text = "رجوع", command = home, image = home_image, compound=LEFT, bg="White", font=("Comic Sans MS", 15, "bold"), width=100, fg="Black")
        home_button.place(x = 10, y = 10)

        self.gui.bind('<KeyPress>', self.start_timer)
        self.gui.bind('<Return>', self.play_game)  # Binding 'Enter' key to play_game function
        self.gui.protocol("closing", self.gui.destroy)  # Handle window close event#
        self.start_game()
        self.gui.mainloop()

    def start_game(self):
        random.shuffle(self.sentences)
        self.wordlabel.config(text=self.sentences[0])

    def game_timer(self):
        if self.timeleft < 11:
            self.timelabelcount.config(fg='red')
        if self.timeleft > 0:
            self.timeleft -= 1
            self.timelabelcount.config(text=self.timeleft)
            self.timelabelcount.after(1000, self.game_timer)
        else:
            self.scorelabel.destroy()
            self.scorelabelcount.destroy()
            self.timelabel.destroy()
            self.timelabelcount.destroy()
            self.wordEntry.destroy()
            self.wordlabel.destroy()
            self.title.destroy()
            
            self.logo_label.place(x = 310, y = 1)
            
            self.new_title = Label(self.gui, text = "الوقت انتهى لقد", bg = "#286ED3", font = ("Comic Sans MS", 50, "bold"), fg = "white")
            self.new_title.place(x = 280, y = 255)
            
            
            result = self.score - self.miss
            self.gameplay_detaillabel.config(text=f'الجمل الصحيحة= {self.score} \nالجمل الخاطئة= {self.miss}\nالنتيجة النهائية= {result}')
            self.gameplay_detaillabel.place(x=445, y=430, anchor=CENTER)
            
            if result < 5:
                self.wowLabel.config(image=self.badpic)
                self.wow1Label.config(image=self.badpic)
                
                self.retry_button.place(x = 785, y = 10)
            elif result >= 8:
                self.wowLabel.config(image=self.propic)
                self.wow1Label.config(image=self.propic)
                
                self.next_level_button.place(x = 785, y = 10)
            else:
                self.wowLabel.config(image=self.goodpic)
                self.wow1Label.config(image=self.goodpic)
                
                self.next_level_button.place(x = 785, y = 10)

    def play_game(self, event):
        user_input = self.wordEntry.get()
        if user_input:  # Check if user input is not empty
            self.i += 1
            self.scorelabelcount.config(text=self.i)
            self.gameplay_detaillabel.config(text='')
            correct_sentence = self.wordlabel['text']
            if user_input.lower() == correct_sentence.lower():
                self.score += 1
            else:
                self.miss += 1
            random.shuffle(self.sentences)
            self.wordlabel.config(text=self.sentences[0])
            self.wordEntry.delete(0, END)

Level02()
