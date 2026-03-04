from tkinter import *

master = Tk()

master.title("Hesap Makinesi")

def topla():
    sonuct = float(e1.get())+float(e2.get())
    toplaLabel = Label(master, text=sonuct).grid(row=2, column=1)

def cikar():
    sonucci = float(e1.get())-float(e2.get())
    cikarLabel = Label(master, text=sonucci).grid(row=2, column=1)
    
def carp():
    sonucca = float(e1.get())*float(e2.get())
    carpLabel = Label(master, text=sonucca).grid(row=2, column=1)
    
def bol():
    sonucb = float(e1.get())/float(e2.get())
    bolLabel = Label(master, text=sonucb).grid(row=2, column=1)

def yuzde():
    sonucy = float(e1.get())/100
    yuzdeLabel = Label(master, text=sonucy).grid(row=2, column=1)

def us():
    sonucu = float(e1.get())**float(e2.get())
    usLabel = Label(master, text=sonucu).grid(row=2, column=1)

def kok():
    sonuck = float(e1.get())** (1 / float(e2.get()))
    kokLabel = Label(master, text=sonuck).grid(row=2, column=1)

def  faktoriyel():
    sonucf = 1
    for i in range(1, int(e1.get()) + 1):
        sonucf = sonucf * i 
    faktoriyelLabel = Label(master, text=sonucf).grid(row=2, column=1)

def C():
    sifirlaLabel = Label(master, text="..................................................................................................................................", fg="white", bg="white")
    sifirlaLabel.grid(row=2, column=1)
    e1.delete(0, END)
    e2.delete(0, END)

Label(master, text="Birinci Girilen:").grid(row=0)
Label(master, text="İkinci Girilen:").grid(row=1)
Label(master, text="Sonuç:").grid(row=2)

e1= Entry(master)
e2= Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

arti = Button(master,text="+", command=topla)
arti.grid(row=0, column=2)

eksi = Button(master,text="-", command=cikar)
eksi.grid(row=1, column=2)

carpi = Button(master,text="*", command=carp)
carpi.grid(row=2, column=2)

bolme = Button(master,text="/", command=bol)
bolme.grid(row=3, column=2)

yuzde1 = Button(master,text="%", command=yuzde)
yuzde1.grid(row=0, column=3)

us1 = Button(master,text="^", command=us)
us1.grid(row=1, column=3)

kok1 = Button(master,text="√¯", command=kok)
kok1.grid(row=2, column=3)

faktoriyel1 = Button(master,text="!", command=faktoriyel)
faktoriyel1.grid(row=3, column=3)

c = Button(master,text="C", command=C)
c.grid(row=0, column=4)

Label(master, text= "Toplama (+) işleminde birinci ve ikinci girilen toplanandır.").grid(row=3)
Label(master, text= "Çıkarma (-) işleminde birinci girilen eksilen, ikinci girilen çıkandır.").grid(row=4)
Label(master, text= "Çarpma (*) işleminde birinci ve ikinci girilen çarpandır.").grid(row=5)
Label(master, text= "Bölme (/) işleminde birinci girilen bölünen, ikinci girilen bölendir.").grid(row=6)
Label(master, text= "Yüzde alma (%) işleminde birinci girilenin yüzdesi alınır.").grid(row=3, column=1)
Label(master, text= "Üs alma (^) işleminde birinci girilen taban, ikinci girilen üstür.").grid(row=4, column=1)
Label(master, text= "Kök alma (√¯) işleminde birinci girilen kökün içi, ikinci girilen kökün derecesidir.").grid(row=5, column=1)
Label(master, text= "Faktöriyel alma (!) işleminde birinci girilenin faktöriyeli bulunur.").grid(row=6, column=1)

mainloop()
