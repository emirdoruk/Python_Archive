from tkinter import *

Sicaklik = Tk()

Sicaklik.title("Sıcaklık Dönüşümleri")
Sicaklik.geometry("500x100")

########################
def Cf():
    sonucCf= float(entrySicaklik.get()) * 9 / 5 + 32
    CfLable = Label(Sicaklik, text=sonucCf).grid(row=1, column=1)
    
def Ck():
    sonucCk= float(entrySicaklik.get()) + 273
    CkLable = Label(Sicaklik, text=sonucCk).grid(row=1, column=1)
    
#
def Fc():
    sonucFc= (float(entrySicaklik.get()) - 32) * 5 / 9 
    FcLable = Label(Sicaklik, text=sonucFc).grid(row=1, column=1)
    
def Fk():
    sonucFk= (float(entrySicaklik.get()) - 32) * 5 / 9 + 273
    FkLable = Label(Sicaklik, text=sonucFk).grid(row=1, column=1)

#
def Kc():
    sonucKc= float(entrySicaklik.get()) - 273
    KcLable = Label(Sicaklik, text=sonucKc).grid(row=1, column=1)

def Kf():
    sonucKf= (float(entrySicaklik.get()) - 273) * 9 / 5 + 32
    KfLable = Label(Sicaklik, text=sonucKf).grid(row=1, column=1)

#
def Csicaklik():
    CsicaklikLabel = Label(Sicaklik, text="............................................", fg="white", bg="white")
    CsicaklikLabel.grid(row=1, column=1)
    entrySicaklik.delete(0, END)

########################
sicaklik = Menu(Sicaklik)
Sicaklik.config(menu = sicaklik)

celcius = Menu(sicaklik)
fahrenheit = Menu(sicaklik)
kelvin = Menu(sicaklik)

#
Label(Sicaklik, text="Girilen:").grid(row=0)
Label(Sicaklik, text="Sonuç:").grid(row=1)

entrySicaklik= Entry(Sicaklik)
entrySicaklik.grid(row=0, column=1)

cSicaklik= Button(Sicaklik, text="C", command= Csicaklik)
cSicaklik.grid(row=0, column=2)

#
sicaklik.add_cascade(label="Celcius", menu= celcius)
sicaklik.add_cascade(label="Fahrenheit", menu= fahrenheit)
sicaklik.add_cascade(label="Kelvin", menu= kelvin)

#Celcius Dönüşümleri
celcius.add_command(label="Fahrenheit", command = Cf)
celcius.add_command(label="Kelvin", command = Ck)

#Fahrenheit Dönüşümleri
fahrenheit.add_command(label="Celcius", command = Fc)
fahrenheit.add_command(label="Kelvin", command = Fk)

#Kelvin Dönüşümleri
kelvin.add_command(label="Celcius", command = Kc)
kelvin.add_command(label="Fahrenheit", command = Kf)

Sicaklik.mainloop()
