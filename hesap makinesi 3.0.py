import math
from tkinter import *

root = Tk()

root.title("Hesap Makinesi")
root.geometry("600x200")

########################

def topla():
    sonucTopla = float(e1.get())+float(e2.get())
    toplaLabel = Label(root, text=sonucTopla).grid(row=3, column=1)

def cikar():
    sonucCikar = float(e1.get())-float(e2.get())
    cikarLabel = Label(root, text=sonucCikar).grid(row=3, column=1)
    
def carp():
    sonucca = float(e1.get())*float(e2.get())
    carpLabel = Label(root, text=sonucca).grid(row=3, column=1)
    
def bol():
    sonucb = float(e1.get())/float(e2.get())
    bolLabel = Label(root, text=sonucb).grid(row=3, column=1)

def yuzde():
    sonucy = float(e1.get())/100
    yuzdeLabel = Label(root, text=sonucy).grid(row=3, column=1)

def us():
    sonucu = float(e1.get())**float(e2.get())
    usLabel = Label(root, text=sonucu).grid(row=3, column=1)

def kok():
    sonuck = float(e1.get())** (1 / float(e2.get()))
    kokLabel = Label(root, text=sonuck).grid(row=3, column=1)

def  faktoriyel():
    sonucf = math.factorial(int(e1.get()))
    faktoriyelLabel = Label(root, text=sonucf).grid(row=3, column=1)

def kare():
    sonucka = float(e1.get())**2
    kareLabel = Label(root, text=sonucka).grid(row=3, column=1)

def kup():
    sonucku = float(e1.get())**3
    kupLabel = Label(root, text=sonucku).grid(row=3, column=1)
    
def karekok():
    sonuckk = float(e1.get())** (1 / 2)
    karekokLabel = Label(root, text=sonuckk).grid(row=3, column=1)

def C():
    Clabel = Label(root).grid(row=3, column=1)
    Clabel.grid_forget()
    e1.delete(0, END)
    e2.delete(0, END)

################################

Label(root, text="İşlemler").grid(row=0)
Label(root, text="Birinci Girilen:").grid(row=1)
Label(root, text="İkinci Girilen:").grid(row=2)
Label(root, text="Sonuç:").grid(row=3)

e1= Entry(root)
e1.grid(row=1, column=1)
e2= Entry(root)
e2.grid(row=2, column=1)
c1 = Button(root,text="C", command=C)
c1.grid(row=0, column=2)

#

###############################

myMenu = Menu(root)
root.config(menu = myMenu)

dortİslem = Menu(myMenu)
digerİslemler = Menu(myMenu)
info = Menu(myMenu)

myMenu.add_cascade(label="Dört İşlem", menu=dortİslem)
myMenu.add_cascade(label="Diğer İşlemler", menu=digerİslemler)
myMenu.add_cascade(label="Açıklama", menu=info)

#

dortİslem.add_command(label="Toplama (+)", command = topla)
dortİslem.add_command(label="Çıkarma (-)", command = cikar)
dortİslem.add_command(label="Çarpma (*)", command = carp)
dortİslem.add_command(label="Bölme (/)", command = bol)

#

digerİslemler.add_command(label="Üs (^)", command = us)
digerİslemler.add_command(label="Kök (√¯)", command = kok)
digerİslemler.add_command(label="Faktöriyel (!)", command = faktoriyel)
digerİslemler.add_command(label="Yüzde (%)", command = yuzde)
digerİslemler.add_command(label="Kare (^2)", command = kare)
digerİslemler.add_command(label="Küp (^3)", command = kup)
digerİslemler.add_command(label="Karekök (2√¯)", command = karekok)

#

info.add_command(label="Toplama (+) işleminde birinci ve ikinci girilen toplanandır.")
info.add_command(label="Çıkarma (-) işleminde birinci girilen eksilen, ikinci girilen çıkandır.")
info.add_command(label="Çarpma (*) işleminde birinci ve ikinci girilen çarpandır.")
info.add_command(label="Bölme (/) işleminde birinci girilen bölünen, ikinci girilen bölendir.")
info.add_command(label="Yüzde alma (%) işleminde birinci girilenin yüzdesi alınır.")
info.add_command(label="Üs alma (^) işleminde birinci girilen taban, ikinci girilen üstür.")
info.add_command(label="Kök alma (√¯) işleminde birinci girilen kökün içi, ikinci girilen kökün derecesidir.")
info.add_command(label="Faktöriyel alma (!) işleminde birinci girilenin faktöriyeli bulunur.")
info.add_command(label="Kare alma (^2) işleminde birinci girilenin karesi alınır.")
info.add_command(label="Küp alma (^3) işleminde birinci girilenin kübü alınır.")
info.add_command(label="Karekök alma (2√¯) işleminde birinci girilenin karekökü alınır.")

root.mainloop()
