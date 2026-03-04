from tkinter import *

Birim = Tk()
Birim.title("Birim Dönüşümleri")
Birim.geometry("500x100")

########################
def  kutle1 ():
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
    
    Label(Kutle, text="Girilen:").grid(row=0)
    Label(Kutle, text="Sonuç:").grid(row=1)
    
    entryKutle= Entry(Kutle)
    entryKutle.grid(row=0, column=1)    
    
    cKutle= Button(Kutle, text="C", command= Ckutle)
    cKutle.grid(row=0, column=2)
    
    kutle.add_cascade(label="Ton", menu= ton)
    kutle.add_cascade(label="Kilogram", menu= kilogram)
    kutle.add_cascade(label="Hektogram", menu= hektogram)
    kutle.add_cascade(label="Dekagram", menu= dekagram)
    kutle.add_cascade(label="Gram", menu= gram)
    kutle.add_cascade(label="Desigram", menu= desigram)
    kutle.add_cascade(label="Santigram", menu= santigram)
    kutle.add_cascade(label="Miligram", menu= miligram)
    
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

########################
def uzunluk1():
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

########################
def zaman1():
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

########################
def sicaklik1():
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
    
########################
birim = Menu(Birim)
Birim.config(menu = birim)

kutlE = Menu(birim)
uzunluK = Menu(birim)
zamaN = Menu(birim)
sicakliK = Menu(birim)

birim.add_command(label="Kütle Dönüşümleri", command = kutle1)
birim.add_command(label="Uzunluk Dönüşümleri", command = uzunluk1)
birim.add_command(label="Zaman Dönüşümleri", command = zaman1)
birim.add_command(label="Sıcaklık Dönüşümleri", command = sicaklik1)

Birim.mainloop()
