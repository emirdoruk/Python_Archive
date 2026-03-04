def notHesapla(satir):
    
    satir=satir[:-1] #satırların sonundaki \n i siler
    liste=satir.split(",")
    print(liste)
    isim = liste[0]
    not1= int(liste[1])
    not2= int(liste[2])
    not3 = int(liste[3])
    sonNot = ((not1*30/100) +(not2*30/10)+(not3*40/100))

    if(sonNot >=90):
        harf="AA"
    elif(sonNot >=85):
        harf="BA"
    elif(sonNot >=80):
        harf="BB"
    elif(sonNot >=75):
        harf="CB"
    elif(sonNot >=70):
        harf="CC"
    else:
        harf="FF"

    return isim + "------------->" + harf + "\n" 

with open ("notlar.txt","r",encoding="utf-8") as file:
    ekleneceklerListesi = []

    for i in file:
        ekleneceklerListesi.append(notHesapla(i))

    print(ekleneceklerListesi)
    
    with open("notlarSon.txt","w",encoding="utf-8") as lastfile:

        for t in ekleneceklerListesi:
            lastfile.write(t)
            
print(lastfile.read())

        
