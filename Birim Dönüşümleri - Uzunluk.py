from tkinter import *

Uzunluk  = Tk()

Uzunluk.title("Uzunluk Dönüşümleri")
Uzunluk.geometry("500x100")

########################
def KMhm():
    sonucKMhm = float(entryUzunluk.get())*10
    KMhmLabel = Label(Uzunluk, text= sonucKMhm).grid(row=1, column=1)
    
def KMdam():
    sonucKMdam = float(entryUzunluk.get())*100
    KMdamLabel = Label(Uzunluk, text= sonucKMdam).grid(row=1, column=1)
    
def KMm():
    sonucKMm = float(entryUzunluk.get())*1000
    KMmLabel = Label(Uzunluk, text= sonucKMm).grid(row=1, column=1)
def KMdm():
    sonucKMdm = float(entryUzunluk.get())*10000
    KMdmLabel = Label(Uzunluk, text= sonucKMdm).grid(row=1, column=1)
    
def KMcm():
    sonucKMcm = float(entryUzunluk.get())*100000
    KMcmLabel = Label(Uzunluk, text= sonucKMcm).grid(row=1, column=1)
    
def KMmm():
    sonucKMmm = float(entryUzunluk.get())*1000000
    KMmmLabel = Label(Uzunluk, text= sonucKMmm).grid(row=1, column=1)
    
#
def HMkm():
    sonucHMkm = float(entryUzunluk.get())/10
    HMkmLabel = Label(Uzunluk, text= sonucHMkm).grid(row=1, column=1)
    
def HMdam():
    sonucHMdam = float(entryUzunluk.get())*10
    HMdamLabel = Label(Uzunluk, text= sonucHMdam).grid(row=1, column=1)
    
def HMm():
    sonucHMm = float(entryUzunluk.get())*100
    HMmLabel = Label(Uzunluk, text= sonucHMm).grid(row=1, column=1)
    
def HMdm():
    sonucHMdm = float(entryUzunluk.get())*1000
    HMdmLabel = Label(Uzunluk, text= sonucHMdm).grid(row=1, column=1)
    
def HMcm():
    sonucHMcm = float(entryUzunluk.get())*10000
    HMcmLabel = Label(Uzunluk, text= sonucHMcm).grid(row=1, column=1)
    
def HMmm():
    sonucHMmm = float(entryUzunluk.get())*100000
    HMmmLabel = Label(Uzunluk, text= sonucHMmm).grid(row=1, column=1)
    
#
def DAMkm():
    sonucDAMkm = float(entryUzunluk.get())/100
    DAMkmLabel = Label(Uzunluk, text= sonucDAMkm).grid(row=1, column=1)
    
def DAMhm():
    sonucDAMhm = float(entryUzunluk.get())/10
    DAMhmLabel = Label(Uzunluk, text= sonucDAMhm).grid(row=1, column=1)
    
def DAMm():
    sonucDAMm = float(entryUzunluk.get())*10
    DAMmLabel = Label(Uzunluk, text= sonucDAMm).grid(row=1, column=1)
    
def DAMdm():
    sonucDAMdm = float(entryUzunluk.get())*100
    DAMdmLabel = Label(Uzunluk, text= sonucDAMdm).grid(row=1, column=1)
    
def DAMcm():
    sonucDAMcm = float(entryUzunluk.get())*1000
    DAMcmLabel = Label(Uzunluk, text= sonucDAMcm).grid(row=1, column=1)
    
def DAMmm():
    sonucDAMmm = float(entryUzunluk.get())*10000
    DAMmmLabel = Label(Uzunluk, text= sonucDAMmm).grid(row=1, column=1)
    
#
def Mkm():
    sonucMkm= float(entryUzunluk.get())/1000
    MkmLabel = Label(Uzunluk, text= sonucMkm).grid(row=1, column=1)
    
def Mhm():
    sonucMhm= float(entryUzunluk.get())/100
    MhmLabel = Label(Uzunluk, text= sonucMhm).grid(row=1, column=1)
    
def Mdam():
    sonucMdam= float(entryUzunluk.get())/10
    MdamLabel = Label(Uzunluk, text= sonucMdam).grid(row=1, column=1)
    
def Mdm():
    sonucMdm= float(entryUzunluk.get())*10
    MdmLabel = Label(Uzunluk, text= sonucMdm).grid(row=1, column=1)
  
def Mcm():
    sonucMcm= float(entryUzunluk.get())*100
    McmLabel = Label(Uzunluk, text= sonucMcm).grid(row=1, column=1)
    
def Mmm():
    sonucMmm= float(entryUzunluk.get())*1000
    MmmLabel = Label(Uzunluk, text= sonucMmm).grid(row=1, column=1)
    
#
def DMkm():
    sonucDMkm= float(entryUzunluk.get())/10000
    DMkmLabel = Label(Uzunluk, text= sonucDMkm).grid(row=1, column=1)
  
def DMhm():
    sonucDMhm= float(entryUzunluk.get())/1000
    DMhmLabel = Label(Uzunluk, text= sonucDMhm).grid(row=1, column=1)
  
def DMdam():
    sonucDMdam= float(entryUzunluk.get())/100
    DMdamLabel = Label(Uzunluk, text= sonucDMdam).grid(row=1, column=1)
  
def DMm():
    sonucDMm= float(entryUzunluk.get())/10
    DMmLabel = Label(Uzunluk, text= sonucDMm).grid(row=1, column=1)

def DMcm():
    sonucDMcm= float(entryUzunluk.get())*10
    DMcmLabel = Label(Uzunluk, text= sonucDMcm).grid(row=1, column=1)
  
def DMmm():
    sonucDMmm= float(entryUzunluk.get())*100
    DMmmLabel = Label(Uzunluk, text= sonucDMmm).grid(row=1, column=1)
  
#
def CMkm():
    sonucCMkm= float(entryUzunluk.get())/100000
    CMkmLabel = Label(Uzunluk, text= sonucCMkm).grid(row=1, column=1)
  
def CMhm():
    sonucCMhm= float(entryUzunluk.get())/10000
    CMhmLabel = Label(Uzunluk, text= sonucCMhm).grid(row=1, column=1)
    
def CMdam():
    sonucCMdam= float(entryUzunluk.get())/1000
    CMdamLabel = Label(Uzunluk, text= sonucCMdam).grid(row=1, column=1)
    
def CMm():
    sonucCMm= float(entryUzunluk.get())/100
    CMmLabel = Label(Uzunluk, text= sonucCMm).grid(row=1, column=1)
  
def CMdm():
    sonucCMdm= float(entryUzunluk.get())/10
    CMdmLabel = Label(Uzunluk, text= sonucCMdm).grid(row=1, column=1)
  
def CMmm():
    sonucCMmm= float(entryUzunluk.get())*10
    CMmmLabel = Label(Uzunluk, text= sonucCMmm).grid(row=1, column=1)
  
#
def MMkm():
    sonucMMkm= float(entryUzunluk.get())/1000000
    MMkmLabel = Label(Uzunluk, text= sonucMMkm).grid(row=1, column=1)
  
def MMhm():
    sonucMMhm= float(entryUzunluk.get())/100000
    MMhmLabel = Label(Uzunluk, text= sonucMMhm).grid(row=1, column=1)
  
def MMdam():
    sonucMMdam= float(entryUzunluk.get())/10000
    MMdamLabel = Label(Uzunluk, text= sonucMMdam).grid(row=1, column=1)
  
def MMm():
    sonucMMm= float(entryUzunluk.get())/1000
    MMmLabel = Label(Uzunluk, text= sonucMMm).grid(row=1, column=1)
  
def MMdm():
    sonucMMdm= float(entryUzunluk.get())/100
    MMdmLabel = Label(Uzunluk, text= sonucMMdm).grid(row=1, column=1)
  
def MMcm():
    sonucMMcm= float(entryUzunluk.get())/10
    MMcmLabel = Label(Uzunluk, text= sonucMMcm).grid(row=1, column=1)
  
#
def Cuzunluk():
    CuzunlukLabel = Label(Uzunluk, text="............................................", fg="white", bg="white")
    CuzunlukLabel.grid(row=1, column=1)
    entryUzunluk.delete(0, END)

########################
uzunluk = Menu(Uzunluk)
Uzunluk.config(menu = uzunluk)

kilometre = Menu(uzunluk)
hektometre = Menu(uzunluk)
dekametre = Menu(uzunluk)
metre = Menu(uzunluk)
desimetre = Menu(uzunluk)
santimetre = Menu(uzunluk)
milimetre = Menu(uzunluk)

#
Label(Uzunluk, text="Girilen:").grid(row=0)
Label(Uzunluk, text="Sonuç:").grid(row=1)

entryUzunluk= Entry(Uzunluk)
entryUzunluk.grid(row=0, column=1)

cUzunluk= Button(Uzunluk, text="C", command= Cuzunluk)
cUzunluk.grid(row=0, column=2)

#
uzunluk.add_cascade(label="Kilometre", menu= kilometre)
uzunluk.add_cascade(label="Hektometre", menu= hektometre)
uzunluk.add_cascade(label="Dekametre", menu= dekametre)
uzunluk.add_cascade(label="Metre", menu= metre)
uzunluk.add_cascade(label="Desimetre", menu= desimetre)
uzunluk.add_cascade(label="Santimetre", menu= santimetre)
uzunluk.add_cascade(label="Milimetre", menu= milimetre)

#Kilometre Dönüşümleri
kilometre.add_command(label="Hektometre", command = KMhm)
kilometre.add_command(label="Dekametre", command = KMdam)
kilometre.add_command(label="Metre", command = KMm)
kilometre.add_command(label="Desimetre", command = KMdm)
kilometre.add_command(label="Santimetre", command = KMcm)
kilometre.add_command(label="Milimetre", command = KMmm)

#Hektometre Dönüşümleri
hektometre.add_command(label="Kilometre", command = HMkm)
hektometre.add_command(label="Dekametre", command = HMdam)
hektometre.add_command(label="Metre", command = HMm)
hektometre.add_command(label="Desimetre", command = HMdm)
hektometre.add_command(label="Santimetre", command = HMcm)
hektometre.add_command(label="Milimetre", command = HMmm)

#Dekametre Dönüşümleri
dekametre.add_command(label="Kilometre", command = DAMkm)
dekametre.add_command(label="Hektometre", command = DAMhm)
dekametre.add_command(label="Metre", command = DAMm)
dekametre.add_command(label="Desimetre", command = DAMdm)
dekametre.add_command(label="Santimetre", command = DAMcm)
dekametre.add_command(label="Milimetre", command = DAMmm)

#Metre Dönüşümleri
metre.add_command(label="Kilometre", command = Mkm)
metre.add_command(label="Hektometre", command = Mhm)
metre.add_command(label="Dekametre", command = Mdam)
metre.add_command(label="Desimetre", command = Mdm)
metre.add_command(label="Santimetre", command = Mcm)
metre.add_command(label="Milimetre", command = Mmm)

#Desimetre Dönüşümleri
desimetre.add_command(label="Kilometre", command = DMkm)
desimetre.add_command(label="Hektometre", command = DMhm)
desimetre.add_command(label="Dekametre", command = DMdam)
desimetre.add_command(label="Metre", command = DMm)
desimetre.add_command(label="Santimetre", command = DMcm)
desimetre.add_command(label="Milimetre", command = DMmm)

#Santimetre Dönüşümleri
santimetre.add_command(label="Kilometre", command = CMkm)
santimetre.add_command(label="Hektometre", command = CMhm)
santimetre.add_command(label="Dekametre", command = CMdam)
santimetre.add_command(label="Metre", command = CMm)
santimetre.add_command(label="Desimetre", command = CMdm)
santimetre.add_command(label="Milimetre", command = CMmm)

#Milimetre Dönüşümleri
milimetre.add_command(label="Kilometre", command = MMkm)
milimetre.add_command(label="Hektometre", command = MMhm)
milimetre.add_command(label="Dekametre", command = MMdam)
milimetre.add_command(label="Metre", command = MMm)
milimetre.add_command(label="Desimetre", command = MMdm)
milimetre.add_command(label="Santimetre", command = MMcm)

Uzunluk.mainloop()
