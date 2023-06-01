# Gerüst fertig 08.05.2023
# Japanische Eingabe| Timer | Statistik

from germanver import *
from nihonngo import *


fenster = Tk()
fenster.title("Typing Game")
fenster.geometry("700x220")
radio_var = StringVar()

def german():
    GController()
    
def japanese():
    NController()

# Erstelle ein Label
label = Label(fenster, text="Press Space",font=("Arial",48))
label.pack()

# Erstelle ein Entry-Feld
entry = Entry(fenster, font=("Arial",20))
entry.bind('<space>', lambda event: callback())
entry.pack()

# Erstelle ein Label für die Ausgabe
result_label = Label(fenster, text="",font=("Arial",22))
result_label.pack()

# Radiobuttons erstellen
button1 = Button(fenster, text="Deutsch", command=german)
button2 = Button(fenster, text="日本語", command=japanese)

# Radiobuttons im Fenster platzieren
button1.pack()
button2.pack()

fenster.mainloop()
        
if __name__ == "__main__":
    pass
    #GController()

