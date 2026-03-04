file = open("Dosyadan Veri Okuma.txt", "r", encoding="utf=8")
for satir in file:
    print (satir, end="")
file.close()
