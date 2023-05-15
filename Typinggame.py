# Gerüst fertig 08.05.2023
# Japanische Eingabe| Timer | Statistik

from random import randint
from tkinter import *
list = []

class View:
    def __init__(self, callback, on_radio_select):
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
        
        # Radiobuttons erstellen
        self.raido1 = Radiobutton(self.fenster, text="Deutsch", variable=self.radio_var, value="german", command=on_radio_select)
        self.raido2 = Radiobutton(self.fenster, text="日本語", variable=self.radio_var, value="japanese", command=on_radio_select)
    
        # Radiobuttons im Fenster platzieren
        self.raido1.pack()
        self.raido2.pack()         
        
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
        if word in self.word_list:
            return "Richtig"
        else:
            return "Falsch"
        
    def word_counter(self):
        if len(list) <= 10:
            return len(list)
        
    def language(self, option):
        if option == "japanese":
            self.word_list = self.word_list = [
                "労働災害補償保険法",
                "法案",
                "ポップコーン",
                "蝶々",
                "グミベア",
                "卓球",
                "木曜日",
                "シナモン",
                "ワニ",
                "サボテン",
                "雲",
                "ジーンズ",
                "落ち葉",
                "トランペット",
                "アプリコット",
                "レモネード",
                "シマウマ",
                "ライター",
                "松",
                "みかん",
                "チーズ",
                "雪の結晶",
                "トルネード",
                "ライオン",
                "キャラメル",
                "灯台",
                "黒板",
                "栗",
                "海賊",
                "オウム",
                "ダイヤモンド",
                "氷河",
                "スパゲッティ",
                "ルバーブ",
                "砂時計",
                "カモミール",
                "コンピュータ",
                "水仙",
                "ワッフル",
                "ロケット",
                "チョコレート",
                "カモメ",
                "タイプライター",
                "プラム",
                "切手",
                "コーヒーメーカー",
                "桜",
                "虹",
                "ヤシの木",
                "フクロウ",
                "ヒトデ",
                "サンショウウオ",
                "イチゴ",
                "パール",
                "バナナ",
                "ドライバー",
                "カンガルー",
                "ライス",
                "とうもろこし",
                "シューレース",
                "宝石",
                "エスプレッソ",
                "ジョウロ",
                "風車",
                "キツネ",
                "パイナップル",
                "ミツバチ",
                "キュウリ",
                "ハープ",
                "チューバ",
                "滝",
                "フラミンゴ",
                "カブトムシ",
                "スーツケース",
                "暖炉",
                "フルート",
                "クジャク",
                "ブーメラン",
                "イルカ",
                "リボン",
                "リュックサック",
                "セージ",
                "カメ",
                "ペン",
                "ダイビングマスク",
                "ズッキーニ",
                "化石",
                "シャベル",
                "ヘリコプター",
                "セイヨウリンドウ",
                "コウモリ",
                "虫取り網",
                "グリル",
                "鳩時計",
                "エルダーフラワー",
                "鶴鷲鷺鷹鹿麒麓麟麿黎黛鼎亀",
                ]
        else:
            self.word_list = self.word_list = [
    "Arbeiterunfallversicherungsgesetz",
    "Gesetzesentwurf",
    "Popcorn",
    "Schmetterling",
    "Gummibärchen",
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
    "Käse",
    "Schneeflocke",
    "Tornado",
    "Löwe",
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
    "Möwe",
    "Schreibmaschine",
    "Pflaume",
    "Briefmarke",
    "Kaffeemaschine",
    "Kirschblüte",
    "Regenbogen",
    "Palme",
    "Eule",
    "Seestern",
    "Salamander",
    "Erdbeere",
    "Perle",
    "Banane",
    "Schraubenzieher",
    "Känguru",
    "Reis",
    "Maiskolben",
    "Schnürsenkel",
    "Edelstein",
    "Espresso",
    "Gießkanne",
    "Windmühle",
    "Fuchs",
    "Ananas",
    "Honigbiene",
    "Gurke",
    "Harfe",
    "Tuba",
    "Wasserfall",
    "Flamingo",
    "Käfer",
    "Koffer",
    "Kamin",
    "Flöte",
    "Pfau",
    "Bumerang",
    "Delfin",
    "Schleife",
    "Rucksack",
    "Salbei",
    "Schildkröte",
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
    "Käfig",
    "Pinguin",
    "Schere",
    "Teekanne",
    "Kürbis"
]
        
        
class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self.callbackKommando, self.on_radio_select)
        self.view.label.config(text = self.model.randomword())# 同時に違う単語が選べれるのが問題  
        self.view.fenster.mainloop()
        
    def callbackKommando(self):
        self.model.word_counter()
        randomword = self.model.randomword()
        self.view.label.config(text = randomword)
        word = self.view.entry.get()
        word = word.replace(" ","")# スペース入力を無効化
        self.view.entry.delete(0, END)
        result = self.model.word_checker(word)
        self.view.result_label.config(text = result)
        
        if result == "Richtig":
            self.view.result_label.config(fg="green")
        else:
            self.view.result_label.config(fg="red")
            
    def on_radio_select(self):
        selected_option = self.view.radio_var.get()
        #print(selected_option)
        self.model.language(selected_option)
        
            
    
              
if __name__ == "__main__":
    Controller()
    
        
        
        
