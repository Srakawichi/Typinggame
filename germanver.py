# Gerüst fertig 08.05.2023

from random import randint
from tkinter import *
list = []

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
        self.word_list = self.word_list = [
    "Arbeiterunfallversicherungsgesetz",
    "Gesetzesentwurf",
    "Popcorn",
    "Schmetterling",
    "Gummibaerchen",
    "Tischtennis",
    "Donnerstag",
    "Zimt",
    "Krokodil",
    "Kaktus",
    "Wolke",
    "Jeans",
    "Laub",
    "Trompete",
    "Aprikose",
    "Limonade",
    "Zebra",
    "Feuerzeug",
    "Kiefer",
    "Mandarine",
    "Kaese",
    "Schneeflocke",
    "Tornado",
    "Loewe",
    "Karamell",
    "Leuchtturm",
    "Tafel",
    "Kastanie",
    "Pirat",
    "Tukan",
    "Diamant",
    "Gletscher",
    "Spaghetti",
    "Rhabarber",
    "Sanduhr",
    "Kamille",
    "Computer",
    "Narzisse",
    "Waffel",
    "Rakete",
    "Schokolade",
    "Moewe",
    "Schreibmaschine",
    "Pflaume",
    "Briefmarke",
    "Kaffeemaschine",
    "Kirschbluete",
    "Regenbogen",
    "Palme",
    "Eule",
    "Seestern",
    "Salamander",
    "Erdbeere",
    "Perle",
    "Banane",
    "Schraubenzieher",
    "Kaenguru",
    "Reis",
    "Maiskolben",
    "Schnuersenkel",
    "Edelstein",
    "Espresso",
    "Giesskanne",
    "Windmuehle",
    "Fuchs",
    "Ananas",
    "Honigbiene",
    "Gurke",
    "Harfe",
    "Tuba",
    "Wasserfall",
    "Flamingo",
    "Kaefer",
    "Koffer",
    "Kamin",
    "Floeote",
    "Pfau",
    "Bumerang",
    "Delfin",
    "Schleife",
    "Rucksack",
    "Salbei",
    "Schildkroete",
    "Stift",
    "Taucherbrille",
    "Zucchini",
    "Fossil",
    "Schaufel",
    "Hubschrauber",
    "Flieder",
    "Fledermaus",
    "Schmetterlingsnetz",
    "Grill",
    "Kuckucksuhr",
    "Holunder",
    "Zahnrad",
    "Blume",
    "Kaefig",
    "Pinguin",
    "Schere",
    "Teekanne",
    "Kuerbis"
]

    def randomword(self):
        word = self.word_list[(randint(0,99))]
        return word
    
    def word_checker(self, word):
        list.append(word)
        print(len(list))
        if word in self.word_list and len(list) != 10:
            return "Richtig"
        elif len(list) != 10:
            return "Falsch"
        else:
            return "Geschafft"
        
#     def word_counter(self):
#         if len(list) == 10:
#             print(len(list))
        
        
class GController:
    def __init__(self):
        self.model = Model()
        self.view = View(self.callbackKommando)
        self.view.label.config(text = self.model.randomword())# 同時に違う単語が選べれるのが問題  
        self.view.fenster.mainloop()
        
    def callbackKommando(self):
        #self.model.word_counter()
        randomword = self.model.randomword()
        self.view.label.config(text = randomword)
        word = self.view.entry.get()
        word = word.replace(" ","")# スペース入力を無効化
        self.view.entry.delete(0, END)
        result = self.model.word_checker(word)
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
    
        
        
        