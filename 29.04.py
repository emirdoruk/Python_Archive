GS=[]
FB=[]
BJK=[]

with open("Futbolcular.txt","r",encoding="utf-8") as file1:

      for satir in file1:
            satir=satir[:-1]
            liste=satir.split(",")

            isim=liste[0]
            takim=liste[1]

            if(takim=="Galatasaray"):

                  GS.append(satir+"\n")

            elif(takim=="Fenerbahçe"):

                  FB.append(satir+"\n")

            elif(takim=="Beşiktaş"):

                  BJK.append(satir+"\n")

with open("Fenerbahçe.txt","w",encoding="utf-8") as file2:

      for satir in FB:

            file2.write(satir)


with open("Galatasaray.txt","w",encoding="utf-8") as file3:

      for satir in GS:

            file3.write(satir)


with open("Beşiktaş.txt","w",encoding="utf-8") as file4:

      for satir in BJK:

            file4.write(satir)








      
