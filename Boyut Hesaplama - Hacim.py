from tkinter import *
import math

Alan = Tk()

Alan.title("Alan Hesaplama")
Alan.geometry("500x100")

########################
def HKup():
    Kare = Tk()
    Kare.title("Küp")
    Kare.geometry("500x100")

    def Ckare():
        CkareLabel = Label(Kare, text="............................................", fg="white", bg="white")
        CkareLabel.grid(row=3, column=1)
        entryKare.delete(0, END)

    def Hkare():
        sonucK= int(entryKare.get()) ** 3
        KLabel = Label(Kare, text= sonucK).grid(row=1, column=1)
        
    Label(Kare, text="Kenar Uzunluğu:").grid(row=0)
    Label(Kare, text="Sonuç:").grid(row=1)

    entryKare = Entry(Kare)
    entryKare.grid(row=0, column=1)

    cKare= Button(Kare, text="C", command= Ckare)
    cKare.grid(row=0, column=3)

    hKare= Button(Kare, text="=", command= Hkare)
    hKare.grid(row=0, column=2)

def HKarePrizma():
    Dikdortgen = Tk()
    Dikdortgen.title("Kare Prizma")
    Dikdortgen.geometry("500x100")

    def Cdikdortgen():
        CdikdortgenLabel = Label(Dikdortgen, text="............................................", fg="white", bg="white")
        CdikdortgenLabel.grid(row=2, column=1)
        entryDikdortgen1.delete(0, END)
        entryDikdortgen2.delete(0, END)

    def Hdikdortgen():
        sonucD= int(entryDikdortgen1.get()) * int(entryDikdortgen2.get())
        DLabel = Label(Dikdortgen, text= sonucD).grid(row23, column=1)
        
    Label(Dikdortgen, text="Taban Kenarı Uzunluğu:").grid(row=0)
    Label(Dikdortgen, text="Yüksekliğin Uzunluğu:").grid(row=1)
    Label(Dikdortgen, text="Sonuç:").grid(row=2)

    entryDikdortgen1 = Entry(Dikdortgen)
    entryDikdortgen1.grid(row=0, column=1)
    entryDikdortgen2 = Entry(Dikdortgen)
    entryDikdortgen2.grid(row=1, column=1)

    cDikdortgen= Button(Dikdortgen, text="C", command= Cdikdortgen)
    cDikdortgen.grid(row=0, column=3)

    hDikdortgen= Button(Dikdortgen, text="=", command= Hdikdortgen)
    hDikdortgen.grid(row=0, column=2)

def HDikdörtgenPrizma():
    Paralelkenar = Tk()
    Paralelkenar.title("Dikdörtgen Prizma")
    Paralelkenar.geometry("500x100")

    def Cparalelkenar():
        CparalelkenarLabel = Label(Paralelkenar, text="............................................", fg="white", bg="white")
        CparalelkenarLabel.grid(row=3, column=1)
        entryParalelkenar1.delete(0, END)
        entryParalelkenar2.delete(0, END)
        entryParalelkenar3.delete(0, END)     

    def Hparalelkenar():
        sonucP= int(entryParalelkenar1.get()) * int(entryParalelkenar2.get()) * int(entryParalelkenar3.get()) 
        PLabel = Label(Paralelkenar, text= sonucP).grid(row=3, column=1)
        
    Label(Paralelkenar, text="Birinci Taban Kenarı Uzunluğu:").grid(row=0)
    Label(Paralelkenar, text="İkinci Taban Kenarı Uzunluğu:").grid(row=1)
    Label(Paralelkenar, text="Yüksekliğin Uzunluğu:").grid(row=2)
    Label(Paralelkenar, text="Sonuç:").grid(row=3)

    entryParalelkenar1 = Entry(Paralelkenar)
    entryParalelkenar1.grid(row=0, column=1)
    entryParalelkenar2 = Entry(Paralelkenar)
    entryParalelkenar2.grid(row=1, column=1)
    entryParalelkenar3 = Entry(Paralelkenar)
    entryParalelkenar3.grid(row=2, column=1)   

    cParalelkenar= Button(Paralelkenar, text="C", command= Cparalelkenar)
    cParalelkenar.grid(row=0, column=3)

    hParalelkenar= Button(Paralelkenar, text="=", command= Hparalelkenar)
    hParalelkenar.grid(row=0, column=2)

def HSilindir():
    EskenarDortgen = Tk()
    EskenarDortgen.title("Silindir")
    EskenarDortgen.geometry("500x100")

    def Ceskenardortgen():
        CeskenardortgenLabel = Label(EskenarDortgen, text="............................................", fg="white", bg="white")
        CeskenardortgenLabel.grid(row=2, column=1)
        entryEskenarDortgen1.delete(0, END)
        entryEskenarDortgen2.delete(0, END)

    def Heskenardortgen():
        sonucED= (int(entryEskenarDortgen1.get()) ** 2) * int(entryEskenarDortgen2.get()) * math.pi
        EDLabel = Label(EskenarDortgen, text= sonucED).grid(row=2, column=1)
        
    Label(EskenarDortgen, text="Açıortay Uzunluğu:").grid(row=0)
    Label(EskenarDortgen, text="Yüksekliğin Uzunluğu:").grid(row=1)
    Label(EskenarDortgen, text="Sonuç:").grid(row=2)

    entryEskenarDortgen1 = Entry(EskenarDortgen)
    entryEskenarDortgen1.grid(row=0, column=1)

    cEskenarDortgen= Button(EskenarDortgen, text="C", command= Ceskenardortgen)
    cEskenarDortgen.grid(row=0, column=3)

    hEskenarDortgen= Button(EskenarDortgen, text="=", command= Heskenardortgen)
    hEskenarDortgen.grid(row=0, column=2)
    
def HKüre():
    Yamuk = Tk()
    Yamuk.title("Küre")
    Yamuk.geometry("500x100")

    def Cyamuk():
        CyamukLabel = Label(Yamuk, text="............................................", fg="white", bg="white")
        CyamukLabel.grid(row=1, column=1)
        entryYamuk1.delete(0, END)
        
    def Hyamuk():
        sonucY= (int(entryYamuk1.get()) ** 3) * 4/3 * math.pi
        YLabel = Label(Yamuk, text= sonucY).grid(row=1, column=1)
        
    Label(Yamuk, text="Yarıçap Uzunluğu:").grid(row=0)
    Label(Yamuk, text="Sonuç:").grid(row=1)

    entryYamuk1 = Entry(Yamuk)
    entryYamuk1.grid(row=0, column=1)

    cYamuk= Button(Yamuk, text="C", command= Cyamuk)
    cYamuk.grid(row=0, column=3)

    hYamuk= Button(Yamuk, text="=", command= Hyamuk)
    hYamuk.grid(row=0, column=2)   

def HKoni():
    Cember = Tk()
    Cember.title("Koni")
    Cember.geometry("500x100")

    def Ccember():
        CcemberLabel = Label(Cember, text="............................................", fg="white", bg="white")
        CcemberLabel.grid(row=2, column=1)
        entryCember.delete(0, END)
        entryCemberr.delete(0, END)

    def Hcember():
        sonucC= (float(entryCember.get()) ** 2) * math.pi * float(entryCemberr.get()) / 3
        CLabel = Label(Cember, text= sonucC).grid(row=2, column=1)
        
    Label(Cember, text="Yarı Çap Uzunluğu:").grid(row=0)
    Label(Cember, text="Yüksekliğin Uzunluğu:").grid(row=1)
    Label(Cember, text="Sonuç:").grid(row=2)

    entryCember = Entry(Cember)
    entryCember.grid(row=0, column=1)
    entryCemberr = Entry(Cember)
    entryCemberr.grid(row=1, column=1)

    cCember= Button(Cember, text="C", command= Ccember)
    cCember.grid(row=0, column=3)

    hCember= Button(Cember, text="=", command= Hcember)
    hCember.grid(row=0, column=2)
    
def HPiramit():
    Elips = Tk()
    Elips.title("Piramit")
    Elips.geometry("500x100")

    def Celips():
        CelipsLabel = Label(Elips, text="............................................", fg="white", bg="white")
        CelipsLabel.grid(row=2, column=1)
        entryElips1.delete(0, END)
        entryElips2.delete(0, END)

    def Helips():
        sonucE= int(entryElips1.get()) * int(entryElips2.get()) / 3  
        ELabel = Label(Elips, text= sonucE).grid(row=2, column=1)
        
    Label(Elips, text="Taban Alanı:").grid(row=0)
    Label(Elips, text="Yüksekliğin Uzunluğu:").grid(row=1)
    Label(Elips, text="Sonuç:").grid(row=2)

    entryElips1= Entry(Elips)
    entryElips1.grid(row=0, column=1)
    entryElips2= Entry(Elips)
    entryElips2.grid(row=1, column=1)
    
    cElips= Button(Elips, text="C", command= Celips)
    cElips.grid(row=0, column=3)

    hElips= Button(Elips, text="=", command= Helips)
    hElips.grid(row=0, column=2)
    
########################
alan = Menu(Alan)
Alan.config(menu = alan)

#
alan.add_command(label="Küp", command= HKup) 
alan.add_command(label="Kare Prizma", command= HKarePrizma)
alan.add_command(label="Dikdörtgen Prizma", command=HDikdörtgenPrizma)
alan.add_command(label="Silindir", command= HSilindir)
alan.add_command(label="Küre", command= HKüre)
alan.add_command(label="Koni", command= HKoni)
alan.add_command(label="Piramit", command= HPiramit)

