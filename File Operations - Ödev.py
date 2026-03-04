with open ("sınıf.txt", "r", encoding="utf-8") as file:
    genel = []

    for satir in file:
        satir = satir[:-1]
        liste = satir.split(",")

        sinif = liste[0]
        ortalama = (int(liste[1]) + int(liste[2]) + int(liste[3]) +int(liste[4])) / 4

        sonuc = sinif + " Yaş Ortalaması: " + str(ortalama) + "\n"
        genel.append(sonuc)

    with open ("ortalama.txt", "w", encoding="utf-8") as file2:
        for i in genel:
            file2.write(i)
