# Gerüst fertig 08.05.2023

import random
from tkinter import *
list = []
file_name = "Woerter.txt"

class View:
    def __init__(self, callback):
        self.fenster = Tk()
        self.fenster.title("Typing Game")
        self.fenster.geometry("700x220")
        self.radio_var = StringVar()
        
        # Erstelle ein Label
        self.label = Label(self.fenster, text="Press Space",font=("Arial",48))
        self.label.pack()

        # Erstelle ein Entry-Feld
        self.entry = Entry(self.fenster, font=("Arial",20))
        self.entry.bind('<space>', lambda event: callback())
        self.entry.pack()

        # Erstelle ein Label für die Ausgabe
        self.result_label = Label(self.fenster, text="",font=("Arial",22))
        self.result_label.pack() 
        
class Model:
    def __init__(self):
        self.zahl = None
    #テキストファイルに入った単語を使用   
    def randomword(self, file_name):
        file_name = "Woerter.txt"
        with open(file_name, 'r') as file:
            words = file.read().split()
            word = random.choice(words)
            return word   
    #入力した単語がテキストファイルに入っているか確認する
    #出力された単語が入力されていなくてもファイルに入っていれば正解になる
    def word_checker(self, word, file_name):
        file_name = "Woerter.txt"
        list.append(word)
        with open(file_name, 'r') as file:
            words = file.read().split()
            if word in words and len(list) != 10:
                return "Richtig"
            elif len(list) != 10:
                return "Falsch"
            else:
                return "ENDE"
        
class GController:
    def __init__(self):
        self.model = Model()
        self.view = View(self.callbackKommando)
        self.view.label.config(text = self.model.randomword(file_name))# 同時に違う単語が選べれるのが問題  
        self.view.fenster.mainloop()
        
    def callbackKommando(self):
        file_name = "Woerter.txt"
        #self.model.word_counter()
        randomword = self.model.randomword(file_name)
        self.view.label.config(text = randomword)
        word = self.view.entry.get()
        word = word.replace(" ","")# スペース入力を無効化
        self.view.entry.delete(0, END)
        result = self.model.word_checker(word, file_name)
        self.view.result_label.config(text = result)
        
        if result == "Richtig":
            self.view.result_label.config(fg="green")
        elif result == "Falsch":
            self.view.result_label.config(fg="red")
        else:
            self.view.label .config(text="Fertig")
            self.view.result_label.config(fg="black")
            self.view.entry.config(state="disabled")
    
              
if __name__ == "__main__":
    GController()
    
        
        
        

