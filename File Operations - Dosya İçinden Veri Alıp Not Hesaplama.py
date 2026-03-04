with open ("notlar.txt", "r", encoding="utf=--8") as file:
    genel_liste = []
    
    for satir in file:
        satir = satir[:-1]  #Sondaki karakteri siler
        liste = satir.split(",") #Virgüller siler
        
        isim = liste[0]
        not1 = int(liste[1])
        not2 = int(liste[2])
        not3 = int(liste[3])
        ortalama = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

        if (ortalama>=90):
            harf="AA"

        elif (ortalama >= 85 and ortalama < 90):
            harf = "BA"

        elif (ortalama >= 80 and ortalama < 85):
            harf = "BB"

        elif (ortalama >= 75 and ortalama < 80):
            harf = "CB"

        elif (ortalama >= 70 and ortalama < 75):
            harf = "CC"

        elif (ortalama >= 65 and ortalama < 70):
            harf = "DC"

        elif (ortalama >= 60 and ortalama < 65):
            harf = "DD"

        elif (ortalama >= 55 and ortalama < 60):
            harf = "FD"

        elif (ortalama < 55):
            harf = "FF"

        sonuc = isim + "-->" + harf + "\n"
        genel_liste.append(sonuc)

    with open ("notlar sonuç.txt", "w", encoding="utf-8") as file2:
        for i in genel_liste:
            file2.write(i)
        
