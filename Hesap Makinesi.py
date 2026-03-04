from tkinter import *
import math

HesapMakinesi = Tk()
HesapMakinesi.title("Hesap Makinesi")
HesapMakinesi.geometry("500x100")

########################
def dortislem():
    Dortİslem = Tk()
    Dortİslem.title("Dört İşlem")
    Dortİslem.geometry("500x100")

    ###############################
    def topla():
        Topla = Tk()
        Topla.title("Toplama")
        Topla.geometry("500x100")
    
        def topla():
            sonuct = float(e1.get())+float(e2.get())
            toplaLabel = Label(Topla, text=sonuct).grid(row=2, column=1)

        def C():
            sifirlaLabel = Label(Topla, text="......................................", fg="white", bg="white")
            sifirlaLabel.grid(row=2, column=1)
            e1.delete(0, END)
            e2.delete(0, END)
        
        Label(Topla, text="Birinci Toplanan:").grid(row=0)
        Label(Topla, text="İkinci Toplanan:").grid(row=1)
        Label(Topla, text="Toplam:").grid(row=2)
    
        e1= Entry(Topla)
        e1.grid(row=0, column=1)
        e2= Entry(Topla)
        e2.grid(row=1, column=1)

        arti = Button(Topla,text="+", command=topla)
        arti.grid(row=0, column=2)

        c1 = Button(Topla,text="C", command=C)
        c1.grid(row=0, column=3)
    
    ###############################
    def cikar():
        Cikar = Tk()
        Cikar.title("Çıkarma")
        Cikar.geometry("500x100")
    
        def cikar():
            sonucci = float(e1.get())-float(e2.get())
            cikarLabel = Label(Cikar, text=sonucci).grid(row=2, column=1)

        def C():
            sifirlaLabel = Label(Cikar, text="......................................", fg="white", bg="white")
            sifirlaLabel.grid(row=2, column=1)
            e1.delete(0, END)
            e2.delete(0, END)
        
        Label(Cikar, text="Eksilen:").grid(row=0)
        Label(Cikar, text="Çıkan:").grid(row=1)
        Label(Cikar, text="Sonuç:").grid(row=2)
    
        e1= Entry(Cikar)
        e1.grid(row=0, column=1)
        e2= Entry(Cikar)
        e2.grid(row=1, column=1)
    
        eksi = Button(Cikar,text="-", command=cikar)
        eksi.grid(row=0, column=2)  
    
        c1 = Button(Cikar,text="C", command=C)
        c1.grid(row=0, column=3)
    
    ###############################
    def carp():
        Carp = Tk()
        Carp.title("Çarpma")
        Carp.geometry("500x100")
    
        def carp():
            sonucca = float(e1.get())*float(e2.get())
            carpLabel = Label(Carp, text=sonucca).grid(row=2, column=1)

        def C():
            sifirlaLabel = Label(Carp, text="......................................", fg="white", bg="white")
            sifirlaLabel.grid(row=2, column=1)
            e1.delete(0, END)
            e2.delete(0, END)
        
        Label(Carp, text="Birinci Çarpan:").grid(row=0)
        Label(Carp, text="İkinci Çarpan:").grid(row=1)
        Label(Carp, text="Çarpım:").grid(row=2)
    
        e1= Entry(Carp)
        e1.grid(row=0, column=1)
        e2= Entry(Carp)
        e2.grid(row=1, column=1)
    
        carpi = Button(Carp,text="*", command=carp)
        carpi.grid(row=0, column=2)
    
        c1 = Button(Carp,text="C", command=C)
        c1.grid(row=0, column=3)
        
    ###############################
    def bol():
        Bol = Tk()
        Bol.title("Bölme")
        Bol.geometry("500x100")
    
        def bol():
            sonucb = float(e1.get())/float(e2.get())
            bolLabel = Label(Bol, text=sonucb).grid(row=2, column=1)

        def C():
            sifirlaLabel = Label(Bol, text="......................................", fg="white", bg="white")
            sifirlaLabel.grid(row=2, column=1)
            e1.delete(0, END)
            e2.delete(0, END)
        
        Label(Bol, text="Biölünen:").grid(row=0)
        Label(Bol, text="Bölen:").grid(row=1)
        Label(Bol, text="Sonuç:").grid(row=2)
    
        e1= Entry(Dortİslem)
        e1.grid(row=0, column=1)
        e2= Entry(Dortİslem)
        e2.grid(row=1, column=1)
    
        bolme = Button(Bol,text="/", command=bol)
        bolme.grid(row=0, column=2) 

        c1 = Button(Bol,text="C", command=C)
        c1.grid(row=0, column=3)
    
    ###############################
    dorTisleM = Menu(Dortİslem)
    Dortİslem.config(menu = dorTisleM)
    
    toplA = Menu(dorTisleM)
    cikaR = Menu(dorTisleM)
    carP = Menu(dorTisleM)
    boL = Menu(dorTisleM)
    
    dorTisleM.add_command(label="Toplama", command = topla)
    dorTisleM.add_command(label="Çıkarma", command = cikar)
    dorTisleM.add_command(label="Çarpma", command = carp)
    dorTisleM.add_command(label="Bölme", command = bol)

########################
def usluifade():
    Usluİfadeler = Tk()
    Usluİfadeler.title("Dört İşlem")
    Usluİfadeler.geometry("500x100")

    ###############################
    def us():
        Us = Tk()
        Us.title("Üslü İfade")
        Us.geometry("500x100")
    
        def topla():
            sonuct = float(e1.get())**float(e2.get())
            toplaLabel = Label(Us, text=sonuct).grid(row=2, column=1)

        def C():
            sifirlaLabel = Label(Us, text="......................................", fg="white", bg="white")
            sifirlaLabel.grid(row=2, column=1)
            e1.delete(0, END)
            e2.delete(0, END)
        
        Label(Us, text="Taban:").grid(row=0)
        Label(Us, text="Üs:").grid(row=1)
        Label(Us, text="Sonuç:").grid(row=2)
    
        e1= Entry(Us)
        e1.grid(row=0, column=1)
        e2= Entry(Us)
        e2.grid(row=1, column=1)

        arti = Button(Us,text="^", command=topla)
        arti.grid(row=0, column=2)

        c1 = Button(Us,text="C", command=C)
        c1.grid(row=0, column=3)
    
###############################
    def kare():
        Kare = Tk()
        Kare.title("'a'nın Karesi")
        Kare.geometry("500x100")
    
        def cikar():
           sonucci = float(e1.get())**2
           cikarLabel = Label(Kare, text=sonucci).grid(row=1, column=1)

        def C():
            sifirlaLabel = Label(Kare, text="......................................", fg="white", bg="white")
            sifirlaLabel.grid(row=1, column=1)
            e1.delete(0, END)
        
        Label(Kare, text="a:").grid(row=0)
        Label(Kare, text="Sonuç:").grid(row=1)
    
        e1= Entry(Kare)
        e1.grid(row=0, column=1)
    
        eksi = Button(Kare,text="^2", command=cikar)
        eksi.grid(row=0, column=2)  
    
        c1 = Button(Kare,text="C", command=C)
        c1.grid(row=0, column=3)
    
    ###############################
    def kup():
        Kup = Tk()
        Kup.title("'a'nın Kübü")
        Kup.geometry("500x100")
    
        def carp():
            sonucca = float(e1.get())**3
            carpLabel = Label(Kup, text=sonucca).grid(row=2, column=1)

        def C():
            sifirlaLabel = Label(Kup, text="......................................", fg="white", bg="white")
            sifirlaLabel.grid(row=2, column=1)
            e1.delete(0, END)
        
        Label(Kup, text="a:").grid(row=0)
        Label(Kup, text="Sonuç:").grid(row=2)
    
        e1= Entry(Kup)
        e1.grid(row=0, column=1)
    
        carpi = Button(Kup,text="^3", command=carp)
        carpi.grid(row=0, column=2)
    
        c1 = Button(Kup,text="C", command=C)
        c1.grid(row=0, column=3)
    
    ###############################
    uslUifadeleR = Menu(Usluİfadeler)
    Usluİfadeler.config(menu = uslUifadeleR)

    uS = Menu(uslUifadeleR)
    karE = Menu(uslUifadeleR)
    kuP = Menu(uslUifadeleR)

    uslUifadeleR.add_command(label="Üslü İfade", command = us)
    uslUifadeleR.add_command(label="'a'nın Karesi", command = kare)
    uslUifadeleR.add_command(label="'a'nın Kübü", command = kup)

########################
def kokluifade():
    Kokluİfadeler = Tk()
    Kokluİfadeler.title("Dört İşlem")
    Kokluİfadeler.geometry("500x100")

    ###############################
    def kok():
        Kok = Tk()
        Kok.title("Üslü İfade")
        Kok.geometry("500x100")
    
        def topla():
            sonuct = float(e1.get())** (1 / float(e2.get()))
            toplaLabel = Label(Kok, text=sonuct).grid(row=2, column=1)

        def C():
            sifirlaLabel = Label(Kok, text="......................................", fg="white", bg="white")
            sifirlaLabel.grid(row=2, column=1)
            e1.delete(0, END)
            e2.delete(0, END)
        
        Label(Kok, text="Kökün İçi:").grid(row=0)
        Label(Kok, text="Kökün Derecesi:").grid(row=1)
        Label(Kok, text="Sonuç:").grid(row=2)
    
        e1= Entry(Kok)
        e1.grid(row=0, column=1)
        e2= Entry(Kok)
        e2.grid(row=1, column=1)

        arti = Button(Kok,text="√¯", command=topla)
        arti.grid(row=0, column=2)

        c1 = Button(Kok,text="C", command=C)
        c1.grid(row=0, column=3)
    
    ###############################
    def karekok():
        Karekok = Tk()
        Karekok.title("'a'nın Karekökü")
        Karekok.geometry("500x100")
    
        def cikar():
            sonucci = float(e1.get())** (1 / 2)
            cikarLabel = Label(Karekok, text=sonucci).grid(row=1, column=1)

        def C():
            sifirlaLabel = Label(Karekok, text="......................................", fg="white", bg="white")
            sifirlaLabel.grid(row=1, column=1)
            e1.delete(0, END)
        
        Label(Karekok, text="a:").grid(row=0)
        Label(Karekok, text="Sonuç:").grid(row=1)
    
        e1= Entry(Karekok)
        e1.grid(row=0, column=1)
    
        eksi = Button(Karekok,text="√¯^2", command=cikar)
        eksi.grid(row=0, column=2)  
    
        c1 = Button(Karekok,text="C", command=C)
        c1.grid(row=0, column=3)
    
    ###############################
    koklUifadeleR= Menu(Kokluİfadeler)
    Kokluİfadeler.config(menu = koklUifadeleR)

    koK = Menu(koklUifadeleR)
    karEkoK = Menu(koklUifadeleR)

    koklUifadeleR.add_command(label="Köklü İfade", command = kok)
    koklUifadeleR.add_command(label="'a'nın Karekökü", command = karekok)

########################
def yuzde():
    Yuzde=Tk()
    Yuzde.title("Yüzdelik Hesaplama")
    Yuzde.geometry("500x100")
    
    def  faktoriyel():
        sonucf = int(e1.get()) / 100
        faktoriyelLabel = Label(Yuzde, text=sonucf).grid(row=1, column=1)

    def C():
        sifirlaLabel = Label(Yuzde, text="...............................", fg="white", bg="white")
        sifirlaLabel.grid(row=1, column=1)
        e1.delete(0, END)

    Label(Yuzde, text="Girilen:").grid(row=0)
    Label(Yuzde, text="Sonuç:").grid(row=1)

    e1= Entry(Yuzde)
    e1.grid(row=0, column=1)

    faktoriyel1 = Button(Yuzde,text="%", command=faktoriyel)
    faktoriyel1.grid(row=0, column=2)

    c = Button(Yuzde,text="C", command=C)
    c.grid(row=0, column=3)


########################
def faktoriyel():
    Faktoriyel =Tk()
    Faktoriyel.title("Faktöriyel Hesapalama")
    Faktoriyel.geometry("500x100")
    
    def  faktoriyel():
        sonucf = math.factorial(int(e1.get()))
        faktoriyelLabel = Label(Faktoriyel, text=sonucf).grid(row=1, column=1)

    def C():
        sifirlaLabel = Label(Faktoriyel, text="...............................", fg="white", bg="white")
        sifirlaLabel.grid(row=1, column=1)
        e1.delete(0, END)

    Label(Faktoriyel, text="Girilen:").grid(row=0)
    Label(Faktoriyel, text="Sonuç:").grid(row=1)

    e1= Entry(Faktoriyel)
    e1.grid(row=0, column=1)

    faktoriyel1 = Button(Faktoriyel,text="!", command=faktoriyel)
    faktoriyel1.grid(row=0, column=2)

    c = Button(Faktoriyel,text="C", command=C)
    c.grid(row=0, column=3)

########################
hesapmakinesi = Menu(HesapMakinesi)
HesapMakinesi.config(menu = hesapmakinesi)

dortisleM = Menu(hesapmakinesi)
usluifadE = Menu(hesapmakinesi)
kokluifadE = Menu(hesapmakinesi)
yuzdE = Menu(hesapmakinesi)
faktoriyeL = Menu(hesapmakinesi)

hesapmakinesi.add_command(label="Dört İşlem", command = dortislem)
hesapmakinesi.add_command(label="Üslü İfade", command = usluifade)
hesapmakinesi.add_command(label="Köklü İfade", command = kokluifade)
hesapmakinesi.add_command(label="Yüzde Hesaplama", command = yuzde)
hesapmakinesi.add_command(label="Faktöriyel Hesaplama", command = faktoriyel)

HesapMakinesi.mainloop()
