file = open("Dosyadan Veri Okuma.txt", "r", encoding="utf=8")# encoding komuduyla yerel karakterleri kullnama başlanır
for satir in file:
    print (satir)
file.close()
