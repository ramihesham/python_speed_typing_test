import tkinter as tk
class TypeSpeedGUI:
    def __init__(self):
        self.window= tk.Tk()
        self.window.iconbitmap('icon.ico')
        self.window.geometry('1000x600+250+125')
        self.window.resizable(0, 0)
        self.window.title("speed typing application  (expert level) ")
        self.window.config(bg='cyan3')
        self.window.mainloop()
TypeSpeedGUI()
