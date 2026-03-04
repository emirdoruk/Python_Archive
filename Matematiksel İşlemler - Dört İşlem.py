from tkinter import *
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

Dortİslem.mainloop()
