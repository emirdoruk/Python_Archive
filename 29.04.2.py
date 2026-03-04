FBage=[]
toplam=0
with open("Fenerbahçe.txt","r",encoding="utf-8") as file1:

      for satir in file1:
            satir=satir[:-1]
            liste=satir.split(",")

            yas=int(liste[2])

            FBage.append(yas)

with open("FenerbahçeYas.txt","w",encoding="utf-8") as file2:

      for yas in FBage:

            toplam=toplam+yas

      ortalama=toplam/len(FBage)

      file2.write(str(ortalama))

      
            
                                         
            
            
