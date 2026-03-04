#Fonksiyon

print ("""
Hesap Makinesi

1- Toplama
2- Çıkarma
3- Çarpma
4- Bölme
5- Yüzdelik
6- Üslü İfade
7- Köklü İfade
8- Faktöriyel
""")

def topla(a, b):
    sonuct = a +b
    return sonuct

def cikar(c, d):
    sonucci = c - d
    return sonucci
    
def carp(e, f):
    sonucca = e * f
    return sonucca
    
def bol(g, h):
    sonucb = g / h
    return sonucb

def yuzde(i):
    sonucy = i / 100
    return sonucy

def us(j, k):
    sonucu = j ** k
    return sonucu

def kok(l, m):
    sonuck = l ** (1 / m)
    return sonuck

def  faktoriyel(n):
    sonucf = 1
    for i in range(1, n+1):
        sonucf = sonucf * i 
    return sonucf

while True:
    girilen = input("yapmak istediğiniz işlemin sayısını giriniz    ")
    if (girilen == "1"):
        while True:
            a = float(input("birinci toplananı giriniz "))
            b = float(input("ikinci toplananı giriniz "))
            sonuct1 = topla(a, b)
            print("sonuç: " , sonuct1)
            print("-------------------")
            break
        
    if (girilen == "2"):
        while True:
            c = float(input("eksileni giriniz "))
            d= float(input("çıkanı giriniz "))
            sonucci1 = cikar(c, d)
            print("sonuç: " , sonucci1)
            print("-------------------")
            break
        
    if (girilen == "3"):
        while True:
            e = float(input("birinci çarpanı giriniz "))
            f = float(input("ikinci çarpanı giriniz "))
            sonucca1 = carp(e, f)
            print("sonuç: " , sonucca1)
            print("-------------------")
            break
        
    if (girilen == "4"):
        while True:
            g = float(input("bölüneni giriniz "))
            h= float(input("böleni giriniz "))
            sonucb1 = bol(g, h)
            print("sonuç: " , sonucb1)
            print("-------------------")
            break

    if (girilen == "5"):
        while True:
            i = float(input("yüzdeliği alınacak sayıyı giriniz "))
            sonucy1 = yuzde(i)
            print("sonuç: " , sonucy1)
            print("-------------------")
            break
            
    if (girilen == "6"):
        while True:
            j = float(input("taban olacak sayıyı giriniz "))
            k= float(input("üs olacak sayıyı giriniz "))
            sonucu1 = us(j, k)
            print("sonuç: " , sonucu1)
            print("-------------------")
            break

    if (girilen == "7"):
        while True:
            l = float(input("kökün içinde olacak sayıyı giriniz "))
            m = float(input("kökün derecesi olacak sayıyı giriniz "))
            sonuck1 = kok(l, m)
            print("sonuç: " , sonuck1)
            print("-------------------")
            break
            
    if (girilen == "8"):
        while True:
            n = int(input("faktöriyeli alınacak sayıyı giriniz "))
            sonucf1 = faktoriyel(n)
            print("sonuç: " , sonucf1)
            print("-------------------")
            break
