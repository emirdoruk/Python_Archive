from tkinter import *
import math 
Alan = Tk()

Alan.title("Alan Hesaplama")
Alan.geometry("500x100")

########################
def AEskenarUcgen():
    EskenarUcgen = Tk()
    EskenarUcgen.title("Eşkenar Üçgen")
    EskenarUcgen.geometry("500x100")

    def Ceskenarucgen():
        CeskenarucgenLabel = Label(EskenarUcgen, text="............................................", fg="white", bg="white")
        CeskenarucgenLabel.grid(row=1, column=1)
        entryEskenarUcgen.delete(0, END)

    def Heskenarucgen():
        sonucEKU= int(entryEskenarUcgen.get()) ** 2 * (3 ** 1/2) / 4 
        EKULabel = Label(EskenarUcgen, text= sonucEKU).grid(row=1, column=1)
        
    Label(EskenarUcgen, text="Kenar Uzunluğu:").grid(row=0)
    Label(EskenarUcgen, text="Sonuç:").grid(row=1)

    entryEskenarUcgen= Entry(EskenarUcgen)
    entryEskenarUcgen.grid(row=0, column=1)

    cEskenarUcgen= Button(EskenarUcgen, text="C", command= Ceskenarucgen)
    cEskenarUcgen.grid(row=0, column=3)

    hEskenarUcgen= Button(EskenarUcgen, text="=", command= Heskenarucgen)
    hEskenarUcgen.grid(row=0, column=2)
    
def AİkizKenarUcgen():
    İkizKenarUcgen = Tk()
    İkizKenarUcgen.title("İkiz Kenar Üçgen")
    İkizKenarUcgen.geometry("500x100")

    def Cikizkenarucgen():
        CikizkenarucgenLabel = Label(İkizKenarUcgen, text="............................................", fg="white", bg="white")
        CikizkenarucgenLabel.grid(row=2, column=1)
        entryİkizKenarUcgen1.delete(0, END)
        entryİkizKenarUcgen2.delete(0, END)

    def Hikizkenarucgen():
        sonucİKU= ((int(entryİkizKenarUcgen1.get()) ** 2 - (int(entryİkizKenarUcgen2.get()) / 2) ** 2)  ** 1/2) *  (int(entryİkizKenarUcgen2.get()) / 2 )
        İKULabel = Label(İkizKenarUcgen, text= sonucİKU).grid(row=2, column=1)
        
    Label(İkizKenarUcgen, text="İkiz Kenar Uzunluğu:").grid(row=0)
    Label(İkizKenarUcgen, text="Taban Uzunluğu:").grid(row=1)
    Label(İkizKenarUcgen, text="Sonuç:").grid(row=2)

    entryİkizKenarUcgen1= Entry(İkizKenarUcgen)
    entryİkizKenarUcgen1.grid(row=0, column=1)
    entryİkizKenarUcgen2= Entry(İkizKenarUcgen)
    entryİkizKenarUcgen2.grid(row=1, column=1)
    
    cİkizKenarUcgen= Button(İkizKenarUcgen, text="C", command= Cikizkenarucgen)
    cİkizKenarUcgen.grid(row=0, column=3)

    hİkizKenarUcgen= Button(İkizKenarUcgen, text="=", command= Hikizkenarucgen)
    hİkizKenarUcgen.grid(row=0, column=2)
    
def ACesitKenarUcgen():
    CesitKenarUcgen = Tk()
    CesitKenarUcgen.title("Üçgende Yükseklik ile Alan")
    CesitKenarUcgen.geometry("500x100")

    def Acesitkenarucgen():
        CcesitkenarucgenLabel = Label(CesitKenarUcgen, text="............................................", fg="white", bg="white")
        CcesitkenarucgenLabel.grid(row=2, column=1)
        entryCesitKenarUcgen1.delete(0, END)
        entryCesitKenarUcgen2.delete(0, END)

    def Acesitkenarucgen():
        sonucCKU= int(entryCesitKenarUcgen1.get()) + int(entryCesitKenarUcgen2.get()) + int(entryCesitKenarUcgen3.get())
        CKULabel = Label(CesitKenarUcgen, text= sonucCKU).grid(row=2, column=1)
        
    Label(CesitKenarUcgen, text="Kenar Uzunluğu:").grid(row=0)
    Label(CesitKenarUcgen, text="Kenara Ait Yüksekliğin Uzunluğu:").grid(row=1)
    Label(CesitKenarUcgen, text="Sonuç:").grid(row=2)

    entryCesitKenarUcgen1= Entry(CesitKenarUcgen)
    entryCesitKenarUcgen1.grid(row=0, column=1)
    entryCesitKenarUcgen2= Entry(CesitKenarUcgen)
    entryCesitKenarUcgen2.grid(row=1, column=1)
    
    cCesitKenarUcgen= Button(CesitKenarUcgen, text="C", command= Ccesitkenarucgen)
    cCesitKenarUcgen.grid(row=0, column=3)

    hCesitKenarUcgen= Button(CesitKenarUcgen, text="=", command= Hcesitkenarucgen)
    hCesitKenarUcgen.grid(row=0, column=2)

def AKare():
    Kare = Tk()
    Kare.title("Kare")
    Kare.geometry("500x100")

    def Ckare():
        CkareLabel = Label(Kare, text="............................................", fg="white", bg="white")
        CkareLabel.grid(row=3, column=1)
        entryKare.delete(0, END)

    def Hkare():
        sonucK= int(entryKare.get()) ** 2
        KLabel = Label(Kare, text= sonucK).grid(row=1, column=1)
        
    Label(Kare, text="Kenar Uzunluğu:").grid(row=0)
    Label(Kare, text="Sonuç:").grid(row=1)

    entryKare = Entry(Kare)
    entryKare.grid(row=0, column=1)

    cKare= Button(Kare, text="C", command= Ckare)
    cKare.grid(row=0, column=3)

    hKare= Button(Kare, text="=", command= Hkare)
    hKare.grid(row=0, column=2)

def ADikdortgen():
    Dikdortgen = Tk()
    Dikdortgen.title("Dikdortgen")
    Dikdortgen.geometry("500x100")

    def Cdikdortgen():
        CdikdortgenLabel = Label(Dikdortgen, text="............................................", fg="white", bg="white")
        CdikdortgenLabel.grid(row=2, column=1)
        entryDikdortgen1.delete(0, END)
        entryDikdortgen2.delete(0, END)

    def Hdikdortgen():
        sonucD= int(entryDikdortgen1.get()) * int(entryDikdortgen2.get())
        DLabel = Label(Dikdortgen, text= sonucD).grid(row=2, column=1)
        
    Label(Dikdortgen, text="Kısa Kenar Uzunluğu:").grid(row=0)
    Label(Dikdortgen, text="Uzun Kenar Uzunluğu:").grid(row=1)
    Label(Dikdortgen, text="Sonuç:").grid(row=2)

    entryDikdortgen1 = Entry(Dikdortgen)
    entryDikdortgen1.grid(row=0, column=1)
    entryDikdortgen2 = Entry(Dikdortgen)
    entryDikdortgen2.grid(row=1, column=1)

    cDikdortgen= Button(Dikdortgen, text="C", command= Cdikdortgen)
    cDikdortgen.grid(row=0, column=3)

    hDikdortgen= Button(Dikdortgen, text="=", command= Hdikdortgen)
    hDikdortgen.grid(row=0, column=2)

def AParalelkenar():
    Paralelkenar = Tk()
    Paralelkenar.title("Paralelkenar")
    Paralelkenar.geometry("500x100")

    def Cparalelkenar():
        CparalelkenarLabel = Label(Paralelkenar, text="............................................", fg="white", bg="white")
        CparalelkenarLabel.grid(row=2, column=1)
        entryParalelkenar1.delete(0, END)
        entryParalelkenar2.delete(0, END)

    def Hparalelkenar():
        sonucP= int(entryParalelkenar1.get()) * int(entryParalelkenar2.get())
        PLabel = Label(Paralelkenar, text= sonucP).grid(row=2, column=1)
        
    Label(Paralelkenar, text="Kenar Uzunluğu:").grid(row=0)
    Label(Paralelkenar, text="Kenara Ait Yüksekliğin Uzunluğu:").grid(row=1)
    Label(Paralelkenar, text="Sonuç:").grid(row=2)

    entryParalelkenar1 = Entry(Paralelkenar)
    entryParalelkenar1.grid(row=0, column=1)
    entryParalelkenar2 = Entry(Paralelkenar)
    entryParalelkenar2.grid(row=1, column=1)

    cParalelkenar= Button(Paralelkenar, text="C", command= Cparalelkenar)
    cParalelkenar.grid(row=0, column=3)

    hParalelkenar= Button(Paralelkenar, text="=", command= Hparalelkenar)
    hParalelkenar.grid(row=0, column=2)

def AEskenarDortgen():
    EskenarDortgen = Tk()
    EskenarDortgen.title("Eşkenar Dörtgen")
    EskenarDortgen.geometry("500x100")

    def Ceskenardortgen():
        CeskenardortgenLabel = Label(EskenarDortgen, text="............................................", fg="white", bg="white")
        CeskenardortgenLabel.grid(row=2, column=1)
        entryEskenarDortgen1.delete(0, END)
        entryEskenarDortgen2.delete(0, END)

    def Heskenardortgen():
        sonucED= int(entryEskenarDortgen1.get()) * int(entryEskenarDortgen2.get()) / 2
        EDLabel = Label(EskenarDortgen, text= sonucED).grid(row=2, column=1)
        
    Label(EskenarDortgen, text="Birinci Açıortay Uzunluğu:").grid(row=0)
    Label(EskenarDortgen, text="İkinci Açıortay Uzunluğu:").grid(row=1)
    Label(EskenarDortgen, text="Sonuç:").grid(row=2)

    entryEskenarDortgen1 = Entry(EskenarDortgen)
    entryEskenarDortgen1.grid(row=0, column=1)

    cEskenarDortgen= Button(EskenarDortgen, text="C", command= Ceskenardortgen)
    cEskenarDortgen.grid(row=0, column=3)

    hEskenarDortgen= Button(EskenarDortgen, text="=", command= Heskenardortgen)
    hEskenarDortgen.grid(row=0, column=2)
    
def AYamuk():
    Yamuk = Tk()
    Yamuk.title("Yamuk")
    Yamuk.geometry("500x100")

    def Cyamuk():
        CyamukLabel = Label(Yamuk, text="............................................", fg="white", bg="white")
        CyamukLabel.grid(row=3, column=1)
        entryYamuk1.delete(0, END)
        entryYamuk2.delete(0, END)
        entryYamuk3.delete(0, END)
        
    def Hyamuk():
        sonucY= (int(entryYamuk1.get()) + int(entryYamuk2.get())) * int(entryYamuk3.get()) / 2 
        YLabel = Label(Yamuk, text= sonucY).grid(row=3, column=1)
        
    Label(Yamuk, text="Birinci Paralel Kenar Uzunluğu:").grid(row=0)
    Label(Yamuk, text="İkinci Paralel Kenar Uzunluğu:").grid(row=1)
    Label(Yamuk, text="Yüksekliğin Uzunluğu:").grid(row=2)
    Label(Yamuk, text="Sonuç:").grid(row=3)

    entryYamuk1 = Entry(Yamuk)
    entryYamuk1.grid(row=0, column=1)
    entryYamuk2 = Entry(Yamuk)
    entryYamuk2.grid(row=1, column=1)
    entryYamuk3 = Entry(Yamuk)
    entryYamuk3.grid(row=2, column=1)

    cYamuk= Button(Yamuk, text="C", command= Cyamuk)
    cYamuk.grid(row=0, column=3)

    hYamuk= Button(Yamuk, text="=", command= Hyamuk)
    hYamuk.grid(row=0, column=2)   

def ACember():
    Cember = Tk()
    Cember.title("Daire")
    Cember.geometry("500x100")

    def Ccember():
        CcemberLabel = Label(Cember, text="............................................", fg="white", bg="white")
        CcemberLabel.grid(row=1, column=1)
        entryCember.delete(0, END)

    def Hcember():
        sonucC= (float(entryCember.get()) ** 2) * math.pi
        CLabel = Label(Cember, text= sonucC).grid(row=1, column=1)
        
    Label(Cember, text="Yarı Çap Uzunluğu:").grid(row=0)
    Label(Cember, text="Sonuç:").grid(row=1)

    entryCember = Entry(Cember)
    entryCember.grid(row=0, column=1)

    cCember= Button(Cember, text="C", command= Ccember)
    cCember.grid(row=0, column=3)

    hCember= Button(Cember, text="=", command= Hcember)
    hCember.grid(row=0, column=2)
    
def AElips():
    Elips = Tk()
    Elips.title("Elips")
    Elips.geometry("500x100")

    def Celips():
        CelipsLabel = Label(Elips, text="............................................", fg="white", bg="white")
        CelipsLabel.grid(row=2, column=1)
        entryElips1.delete(0, END)
        entryElips2.delete(0, END)

    def Helips():
        sonucE= int(entryElips1.get()) * int(entryElips2.get()) * math.pi 
        ELabel = Label(Elips, text= sonucE).grid(row=2, column=1)
        
    Label(Elips, text="Birinci Yarı Çap Uzunluğu:").grid(row=0)
    Label(Elips, text="İkinci Yarı Çap Uzunluğu:").grid(row=1)
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
alan.add_command(label="Eşkenar Üçgen", command = AEskenarUcgen)
alan.add_command(label="İkizkenar Üçgen", command= AİkizKenarUcgen)
alan.add_command(label="Çeşit Kenar Üçgen", command= ACesitKenarUcgen)
alan.add_command(label="Kare", command= AKare)
alan.add_command(label="Dikdörtgen", command= ADikdortgen)
alan.add_command(label="Paralelkenar", command= AParalelkenar)
alan.add_command(label="Eşkenar Dörtgen", command= AEskenarDortgen)
alan.add_command(label="Yamuk", command= AYamuk)
alan.add_command(label="Çember", command= ACember)
alan.add_command(label="Elips", command= AElips)

