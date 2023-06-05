# 日本語入力完成　31.05.23


from random import randint
from tkinter import *
list = []

class View:
    def __init__(self, callback):
        self.fenster = Tk()
        self.fenster.title("Typing Game")
        self.fenster.geometry("900x220")
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
        self.word_list = [
    "労働災害補償保険法: roudousaigaihoshouhokenhou",
    "法案: houann",
    "ポップコーン: poppuko-nn",
    "蝶々: chouchou",
    "グミベア: gumibea",
    "卓球: takkyuu",
    "木曜日: mokuyoubi",
    "シナモン: shinamon",
    "ワニ: wani",
    "サボテン: saboten",
    "雲: kumo",
    "ジーンズ: ji-nzu",
    "落ち葉: ochiba",
    "トランペット: toranpetto",
    "アプリコット: apurikotto",
    "レモネード: remone-do",
    "シマウマ: shimauma",
    "ライター: raita-",
    "松: matsu",
    "みかん: mikan",
    "チーズ: chi-zu",
    "雪の結晶: yukinokesshou",
    "トルネード: torune-do",
    "ライオン: raion",
    "キャラメル: kyarameru",
    "灯台: toutou",
    "黒板: kokuban",
    "栗: kuri",
    "海賊: kaizoku",
    "オウム: oumu",
    "ダイヤモンド: daiyamondo",
    "氷河: hyouga",
    "スパゲッティ: supagetti",
    "ルバーブ: ruba-bu",
    "砂時計: sunadokei",
    "カモミール: kamomi-ru",
    "コンピュータ: konpyu-ta",
    "水仙: suisen",
    "ワッフル: waffuru",
    "ロケット: roketto",
    "チョコレート: chokore-to",
    "カモメ: kamome",
    "タイプライター: taipuraita-",
    "プラム: puramu",
    "切手: kitte",
    "コーヒーメーカー: ko-hi-me-ka-",
    "桜: sakura",
    "虹: niji",
    "ヤシの木: yashinoki",
    "フクロウ: fukurou",
    "ヒトデ: hitode",
    "サンショウウオ: sanshouuo",
    "イチゴ: ichigo",
    "パール: pa-ru",
    "バナナ: banana",
    "ドライバー: doraiba-",
    "カンガルー: kangaru-",
    "ライス: raisu",
    "とうもろこし: toumorokoshi",
    "シューレース: shu-re-su",
    "宝石: houseki"]
    
        self.tanngo = [
    "roudousaigaihoshouhokenhou",
    "houann",
    "poppuko-nn",
    "chouchou",
    "gumibea",
    "takkyuu",
    "mokuyoubi",
    "shinamon",
    "wani",
    "saboten",
    "kumo",
    "ji-nzu",
    "ochiba",
    "toranpetto",
    "apurikotto",
    "remone-do",
    "shimauma",
    "raita-",
    "matsu",
    "mikan",
    "chi-zu",
    "yukinokesshou",
    "torune-do",
    "raion",
    "kyarameru",
    "toutou",
    "kokuban",
    "kuri",
    "kaizoku",
    "oumu",
    "daiyamondo",
    "hyouga",
    "supagetti",
    "ruba-bu",
    "sunadokei",
    "kamomi-ru",
    "konpyu-ta",
    "suisen",
    "waffuru",
    "roketto",
    "chokore-to",
    "kamome",
    "taipuraita-",
    "puramu",
    "kitte",
    "ko-hi-me-ka-",
    "sakura",
    "niji",
    "yashi no ki",
    "fukurou",
    "hitode",
    "sanshouuo",
    "ichigo",
    "pa-ru",
    "banana",
    "doraiba-",
    "kangaru-",
    "raisu",
    "toumorokoshi",
    "shu-re-su",
    "houseki",
    "esupu"
]


    def randomword(self):
        word = self.word_list[(randint(0,60))]
        return word
    
    def word_checker(self, word):
        list.append(word)
        print(len(list))
        if word in self.tanngo and len(list) != 10:
            return "正解"
        elif len(list) != 10:
            return "誤字"
        else:
            return "終了"
        
    def word_counter(self):
        if len(list) <= 10:
            return len(list)
        
class NController:
    def __init__(self):
        self.model = Model()
        self.view = View(self.callbackKommando)
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
        
        if result == "正解":
            self.view.result_label.config(fg="green")
        elif result == "誤字":
            self.view.result_label.config(fg="red")
        else:
            self.view.label.config(text="終了")
            self.view.result_label.config(fg="black")
            self.view.entry.config(state="disabled")
            
    
              
if __name__ == "__main__":
    NController()
