print("lütfen kilonuzu kilogram cinsinden giriniz")
kilo = float(input( "kilo: "))
print("lütfen boyunuzu santimetre cinsinden giriniz")
boy = float(input( "boy: "))

bki = kilo/ boy*boy

if (bki < 18.5):
    print("zayıf")

elif (bki >= 18.5 and bki < 25):
    print("normal")

elif (bki >= 25 and bki < 30):
    print("fazla kilolu")

else :
    print("obez")
