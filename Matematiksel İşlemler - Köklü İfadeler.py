from tkinter import *
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

Kokluİfadeler.mainloop()
