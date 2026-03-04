#Faktöriyel Hesaplama

while True:
    sayi = int(input ("sayı giriniz "))

    if (sayi == 0):
        break
    
    faktoriyel = 1

    for i in range(1, sayi+1):
        faktoriyel = faktoriyel * i

    print("sonuç: " , faktoriyel)
