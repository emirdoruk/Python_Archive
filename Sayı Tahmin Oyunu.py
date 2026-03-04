import random
import time

print("""
Sayı tahmin oyununa hoş geldiniz.
1 ile 50 arasında bir sayı tahmin edin.
""")

rastgelesayi = random.randint(1,50)
hak = 6

while True:
    girilensayi = int(input("Tahminizi Giriniz: "))


    if(girilensayi <=50 and girilensayi >=1):
        if(girilensayi > rastgelesayi):
            hak = hak-1
            print("Daha küçük bir sayı giriniz." , " Kalan hakkınız: " , hak)
            time.sleep(2)

        elif(girilensayi < rastgelesayi):
            hak = hak-1
            print("Daha büyük bir sayı giriniz." , " kalan hakkınız: " , hak)
            time.sleep(2)

        elif(girilensayi == rastgelesayi):
            hak = hak-1
            print("Bildiniz. Oyun sona erdi.")
            break

        if(hak==0):
            print("Hakkınız bitti. Oyun sona erdi.")
            break

    else:
        hak = hak-1
        print("Geçerli bir sayı giriniz." , " Kalan hakkınız: " , hak)
        time.sleep(2)

