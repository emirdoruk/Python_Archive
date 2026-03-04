from tkinter import *

Zaman = Tk()

Zaman.title("Zaman Dönüşümleri")
Zaman.geometry("500x100")

########################
def Hdk():
    sonucHdk= int(entryZaman.get()) * 60
    HdkLable = Label(Zaman, text=sonucHdk).grid(row=1, column=1)

def Hs():
    sonucHs= int(entryZaman.get()) * 3600
    HsLable = Label(Zaman, text=sonucHs).grid(row=1, column=1)

#
def DKh():
    sonucDKh= int(entryZaman.get()) / 60
    DKhLable = Label(Zaman, text=sonucDKh).grid(row=1, column=1)

def DKs():
    sonucDKs= int(entryZaman.get()) * 60
    DKsLable = Label(Zaman, text=sonucDKs).grid(row=1, column=1)

#
def Sh():
    sonucSh= int(entryZaman.get()) / 3600
    ShLable = Label(Zaman, text=sonucSh).grid(row=1, column=1)

def Sdk():
    sonucSDK= int(entryZaman.get()) / 60
    SDKLable = Label(Zaman, text=sonucSDK).grid(row=1, column=1)

#
def Czaman():
    CzamanLabel = Label(Zaman, text="............................................", fg="white", bg="white")
    CzamanLabel.grid(row=1, column=1)
    entryZaman.delete(0, END)

########################
zaman = Menu(Zaman)
Zaman.config(menu = zaman)

saat = Menu(zaman)
dakika = Menu(zaman)
saniye = Menu(zaman)

#
Label(Zaman, text="Girilen:").grid(row=0)
Label(Zaman, text="Sonuç:").grid(row=1)

entryZaman= Entry(Zaman)
entryZaman.grid(row=0, column=1)

cZaman= Button(Zaman, text="C", command= Czaman)
cZaman.grid(row=0, column=2)

#
zaman.add_cascade(label="Saat", menu= saat)
zaman.add_cascade(label="Dakika", menu= dakika)
zaman.add_cascade(label="Saniye", menu= saniye)

#Saat Dönüşümleri
saat.add_command(label="Dakika", command = Hdk)
saat.add_command(label="Saniye", command = Hs)

#Dakika Dönüşümleri
dakika.add_command(label="Saat", command = DKh)
dakika.add_command(label="Saniye", command = DKs)

#Saniye Dönüşümleri
saniye.add_command(label="Saat", command = Sh)
saniye.add_command(label="Dakika", command = Sdk)

Zaman.mainloop()
