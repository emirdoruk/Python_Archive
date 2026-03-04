from tkinter import *

Kutle  = Tk()

Kutle.title("Kütle Dönüşümleri")
Kutle.geometry("500x100")

########################

def Tkg():
    sonucTkg = float(entryKutle.get())*10
    TkgLabel = Label(Kutle, text= sonucTkg).grid(row=1, column=1)
    
def Thg():
    sonucThg = float(entryKutle.get())*100
    ThgLabel = Label(Kutle, text= sonucThg).grid(row=1, column=1)
     
def Tdag():
    sonucTdag = float(entryKutle.get())*1000
    TdagLabel = Label(Kutle, text= sonucTdag).grid(row=1, column=1)
     
def Tg():
    sonucTg = float(entryKutle.get())*10000
    TgLabel = Label(Kutle, text= sonucTg).grid(row=1, column=1)
   
def Tdg():
    sonucTdg = float(entryKutle.get())*100000
    TdgLabel = Label(Kutle, text= sonucTdg).grid(row=1, column=1)
     
def Tcg():
    sonucTcg = float(entryKutle.get())*1000000
    TcgLabel = Label(Kutle, text= sonucTcg).grid(row=1, column=1)
   
def Tmg():
    sonucTmg = float(entryKutle.get())*10000000
    TmgLabel = Label(Kutle, text= sonucTmg).grid(row=1, column=1)
   
#   
def KGt():
    sonucKGt = float(entryKutle.get())/10
    KGtLabel = Label(Kutle, text= sonucKGt).grid(row=1, column=1)

def KGhg():
    sonucKGhg = float(entryKutle.get())*10
    KGhgLabel = Label(Kutle, text= sonucKGhg).grid(row=1, column=1)
    
def KGdag():
    sonucKGdag = float(entryKutle.get())*100
    KGdagLabel = Label(Kutle, text= sonucKGdag).grid(row=1, column=1)
    
def KGg():
    sonucKGg = float(entryKutle.get())*1000
    KGgLabel = Label(Kutle, text= sonucKGg).grid(row=1, column=1)
def KGdg():
    sonucKGdm = float(entryKutle.get())*10000
    KGdmLabel = Label(Kutle, text= sonucKGdm).grid(row=1, column=1)
    
def KGcg():
    sonucKGcm = float(entryKutle.get())*100000
    KGcmLabel = Label(Kutle, text= sonucKGcm).grid(row=1, column=1)
    
def KGmg():
    sonucKGmm = float(entryKutle.get())*1000000
    KGmmLabel = Label(Kutle, text= sonucKGmm).grid(row=1, column=1)
    
#
def HGt():
    sonucHGt = float(entryKutle.get())/100
    HGtLabel = Label(Kutle, text= sonucHGt).grid(row=1, column=1)

def HGkg():
    sonucHGkg = float(entryKutle.get())/10
    HGkgLabel = Label(Kutle, text= sonucHGkg).grid(row=1, column=1)
    
def HGdag():
    sonucHMdag = float(entryKutle.get())*10
    HMdagLabel = Label(Kutle, text= sonucHMdag).grid(row=1, column=1)
    
def HGg():
    sonucHGg = float(entryKutle.get())*100
    HGgLabel = Label(Kutle, text= sonucHGg).grid(row=1, column=1)
    
def HGdg():
    sonucHGdg = float(entryKutle.get())*1000
    HGdgLabel = Label(Kutle, text= sonucHGdg).grid(row=1, column=1)
    
def HGcg():
    sonucHGcg = float(entryKutle.get())*10000
    HGcgLabel = Label(Kutle, text= sonucHGcg).grid(row=1, column=1)
    
def HGmg():
    sonucHGmg = float(entryKutle.get())*100000
    HGmgLabel = Label(Kutle, text= sonucHGmg).grid(row=1, column=1)
    
#
def DAGt():
    sonucDAGt = float(entryKutle.get())/1000
    DAGtLabel = Label(Kutle, text= sonucDAGt).grid(row=1, column=1)
    
def DAGkg():
    sonucDAGkg = float(entryKutle.get())/100
    DAGkgLabel = Label(Kutle, text= sonucDAGkg).grid(row=1, column=1)
    
def DAGhg():
    sonucDAGhg = float(entryKutle.get())/10
    DAGhgLabel = Label(Kutle, text= sonucDAGhg).grid(row=1, column=1)
    
def DAGg():
    sonucDAGg = float(entryKutle.get())*10
    DAGgLabel = Label(Kutle, text= sonucDAGg).grid(row=1, column=1)
    
def DAGdg():
    sonucDAGdg = float(entryKutle.get())*100
    DAGdgLabel = Label(Kutle, text= sonucDAGdg).grid(row=1, column=1)
    
def DAGcg():
    sonucDAMcm = float(entryKutle.get())*1000
    DAMcmLabel = Label(Kutle, text= sonucDAMcm).grid(row=1, column=1)
    
def DAGmg():
    sonucDAGmg = float(entryKutle.get())*10000
    DAGmgLabel = Label(Kutle, text= sonucDAGmg).grid(row=1, column=1)
    
#
def Gt():
    sonucGt= float(entryKutle.get())/10000
    GtLabel = Label(Kutle, text= sonucGt).grid(row=1, column=1)
   
def Gkg():
    sonucGkg= float(entryKutle.get())/1000
    GkgLabel = Label(Kutle, text= sonucGkg).grid(row=1, column=1)
    
def Ghg():
    sonucGhg= float(entryKutle.get())/100
    GhgLabel = Label(Kutle, text= sonucGhg).grid(row=1, column=1)
    
def Gdag():
    sonucGdag= float(entryKutle.get())/10
    GdagLabel = Label(Kutle, text= sonucGdag).grid(row=1, column=1)
    
def Gdg():
    sonucGdg= float(entryKutle.get())*10
    GdgLabel = Label(Kutle, text= sonucGdg).grid(row=1, column=1)
  
def Gcg():
    sonucGcg= float(entryKutle.get())*100
    GcgLabel = Label(Kutle, text= sonucGcg).grid(row=1, column=1)
    
def Gmg():
    sonucGmg= float(entryKutle.get())*1000
    GmgLabel = Label(Kutle, text= sonucGmg).grid(row=1, column=1)
    
#
def DGt():
    sonucDGt= float(entryKutle.get())/100000
    DGtLabel = Label(Kutle, text= sonucDGt).grid(row=1, column=1)
  
def DGkg():
    sonucDGkg= float(entryKutle.get())/10000
    DGkgLabel = Label(Kutle, text= sonucDGkg).grid(row=1, column=1)
  
def DGhg():
    sonucDGhg= float(entryKutle.get())/1000
    DGhgLabel = Label(Kutle, text= sonucDGhg).grid(row=1, column=1)
  
def DGdag():
    sonucDGdag= float(entryKutle.get())/100
    DGdagLabel = Label(Kutle, text= sonucDGdag).grid(row=1, column=1)
  
def DGg():
    sonucDGg= float(entryKutle.get())/10
    DGgLabel = Label(Kutle, text= sonucDGg).grid(row=1, column=1)

def DGcg():
    sonucDGcg= float(entryKutle.get())*10
    DGcgLabel = Label(Kutle, text= sonucDGcg).grid(row=1, column=1)
  
def DGmg():
    sonucDGmg= float(entryKutle.get())*100
    DGmgLabel = Label(Kutle, text= sonucDGmg).grid(row=1, column=1)
  
#
def CGt():
    sonucCGt= float(entryKutle.get())/1000000
    CGtLabel = Label(Kutle, text= sonucCGt).grid(row=1, column=1)
  
def CGkg():
    sonucCGkg= float(entryKutle.get())/100000
    CGkgLabel = Label(Kutle, text= sonucCGkg).grid(row=1, column=1)
  
def CGhg():
    sonucCGhg= float(entryKutle.get())/10000
    CGhgLabel = Label(Kutle, text= sonucCGhg).grid(row=1, column=1)
    
def CGdag():
    sonucCGdag= float(entryKutle.get())/1000
    CGdagLabel = Label(Kutle, text= sonucCGdag).grid(row=1, column=1)
    
def CGg():
    sonucCGg= float(entryKutle.get())/100
    CGmLabel = Label(Kutle, text= sonucCGg).grid(row=1, column=1)
  
def CGdg():
    sonucCGdg= float(entryKutle.get())/10
    CGdgLabel = Label(Kutle, text= sonucCGdg).grid(row=1, column=1)
  
def CGmg():
    sonucCGmg= float(entryKutle.get())*10
    CGmgLabel = Label(Kutle, text= sonucCGmg).grid(row=1, column=1)
  
#
def MGt():
    sonucMGt= float(entryKutle.get())/10000000
    MGtLabel = Label(Kutle, text= sonucMGt).grid(row=1, column=1)
  
def MGkg():
    sonucMGkg= float(entryKutle.get())/1000000
    MGkgLabel = Label(Kutle, text= sonucMGkg).grid(row=1, column=1)
  
def MGhg():
    sonucMGhg= float(entryKutle.get())/100000
    MGhgLabel = Label(Kutle, text= sonucMGhg).grid(row=1, column=1)
  
def MGdag():
    sonucMGdag= float(entryKutle.get())/10000
    MGdagLabel = Label(Kutle, text= sonucMGdag).grid(row=1, column=1)
  
def MGg():
    sonucMGg= float(entryKutle.get())/1000
    MGgLabel = Label(Kutle, text= sonucMGg).grid(row=1, column=1)
  
def MGdg():
    sonucMGdg= float(entryKutle.get())/100
    MGdgLabel = Label(Kutle, text= sonucMGdg).grid(row=1, column=1)
  
def MGcg():
    sonucMGcg= float(entryKutle.get())/10
    MGcgLabel = Label(Kutle, text= sonucMGcg).grid(row=1, column=1)
  
#
def Ckutle():
    CkutleLabel = Label(Kutle, text="............................................", fg="white", bg="white")
    CkutleLabel.grid(row=1, column=1)
    entryKutle.delete(0, END)


########################
kutle = Menu(Kutle)
Kutle.config(menu = kutle)

ton = Menu(kutle)
kilogram= Menu(kutle)
hektogram = Menu(kutle)
dekagram = Menu(kutle)
gram = Menu(kutle)
desigram = Menu(kutle)
santigram = Menu(kutle)
miligram = Menu(kutle)

#

Label(Kutle, text="Girilen:").grid(row=0)
Label(Kutle, text="Sonuç:").grid(row=1)

entryKutle= Entry(Kutle)
entryKutle.grid(row=0, column=1)

cKutle= Button(Kutle, text="C", command= Ckutle)
cKutle.grid(row=0, column=2)

#

kutle.add_cascade(label="Ton", menu= ton)
kutle.add_cascade(label="Kilogram", menu= kilogram)
kutle.add_cascade(label="Hektogram", menu= hektogram)
kutle.add_cascade(label="Dekagram", menu= dekagram)
kutle.add_cascade(label="Gram", menu= gram)
kutle.add_cascade(label="Desigram", menu= desigram)
kutle.add_cascade(label="Santigram", menu= santigram)
kutle.add_cascade(label="Miligram", menu= miligram)

#

#Ton Dönüşümleri
ton.add_command(label="Kilogram", command =Tkg)
ton.add_command(label="Hektogram", command =Thg)
ton.add_command(label="Dekagram", command =Tdag)
ton.add_command(label="Gram", command =Tg)
ton.add_command(label="Desigram", command =Tdg)
ton.add_command(label="Santigram", command =Tcg)
ton.add_command(label="Miligram", command =Tmg)

#Kilogram Dönüşümleri
kilogram.add_command(label="Ton", command = KGt)
kilogram.add_command(label="Hektogram", command = KGhg)
kilogram.add_command(label="Dekagram", command = KGdag)
kilogram.add_command(label="Gram", command = KGg)
kilogram.add_command(label="Desigram", command = KGdg)
kilogram.add_command(label="Santigram", command = KGcg)
kilogram.add_command(label="Miligram", command = KGmg)

#Hektogram Dönüşümleri
hektogram.add_command(label="Ton", command = HGt)
hektogram.add_command(label="Kilogram", command = HGkg)
hektogram.add_command(label="Dekagram", command = HGdag)
hektogram.add_command(label="Gram", command = HGg)
hektogram.add_command(label="Desigram", command = HGdg)
hektogram.add_command(label="Santigram", command = HGcg)
hektogram.add_command(label="Miligram", command = HGmg)

#Dekagram Dönüşümleri
dekagram.add_command(label="Ton", command = DAGt)
dekagram.add_command(label="Kilogram", command = DAGkg)
dekagram.add_command(label="Hektogram", command = DAGhg)
dekagram.add_command(label="Gram", command = DAGg)
dekagram.add_command(label="Desigram", command = DAGdg)
dekagram.add_command(label="Santigram", command = DAGcg)
dekagram.add_command(label="Miligram", command = DAGmg)

#Gram Dönüşümleri
gram.add_command(label="Ton", command = Gt)
gram.add_command(label="Kilogram", command = Gkg)
gram.add_command(label="Hektogram", command = Ghg)
gram.add_command(label="Dekagram", command = Gdag)
gram.add_command(label="Desigram", command = Gdg)
gram.add_command(label="Santigram", command = Gcg)
gram.add_command(label="Miligram", command = Gmg)

#Desigram Dönüşümleri
desigram.add_command(label="Ton", command = DGt)
desigram.add_command(label="Kilogram", command = DGkg)
desigram.add_command(label="Hektogram", command = DGhg)
desigram.add_command(label="Dekagram", command = DGdag)
desigram.add_command(label="Gram", command = DGg)
desigram.add_command(label="Santigram", command = DGcg)
desigram.add_command(label="Miligram", command = DGmg)

#Santigram Dönüşümleri
santigram.add_command(label="Ton", command = CGt)
santigram.add_command(label="Kilogram", command = CGkg)
santigram.add_command(label="Hektogram", command = CGhg)
santigram.add_command(label="Dekagram", command = CGdag)
santigram.add_command(label="Gram", command = CGg)
santigram.add_command(label="Desigram", command = CGdg)
santigram.add_command(label="Miligram", command = CGmg)

#Miligram Dönüşümleri
miligram.add_command(label="Ton", command = MGt)
miligram.add_command(label="Kilogram", command = MGkg)
miligram.add_command(label="Hektogram", command = MGhg)
miligram.add_command(label="Dekagram", command = MGdag)
miligram.add_command(label="Gram", command = MGg)
miligram.add_command(label="Desigram", command = MGdg)
miligram.add_command(label="Santigram", command = MGcg)

Kutle.mainloop()
