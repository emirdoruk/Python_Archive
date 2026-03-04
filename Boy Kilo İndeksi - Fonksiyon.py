def  bkiHesapla (kilo, boy):
    bki= kilo/(boy*boy)
    return bki

while True:
    kilo= float(input("Lütfen Kilonuzu Giriniz: "))
    boy= float(input("Lütfen Boyunuzu Giriniz:"))
    mybki=   bkiHesapla(kilo, boy)
    
    print("BKİ Sonucunuz: " , mybki)

    if(mybki <= 18.5):
        print("Çok Zayıfsınız\n")

    elif(mybki > 18.5 and mybki <= 25):
        print("İdeal Kilodasınız\n")

    elif(mybki > 25 and mybki <= 30):
        print("Kilolusunuz\n")

    else:
        print("Çok Kilolusunuz\n")
