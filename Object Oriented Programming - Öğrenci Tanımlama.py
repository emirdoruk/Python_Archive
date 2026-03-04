class Öğrenci():
    def __init__ (self, isim, soyisim, yaş, sinif, okul):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.sinif = sinif
        self.okul = okul

öğrenci1 = Öğrenci("Efe Emre", "Özdil", 17, 11, "Bahçeşehir Koleji")
öğrenci2 = Öğrenci("Emir Doruk", "Pırasalar", 17, 11, "Bornova Koleji")

print(öğrenci1.isim, öğrenci1.soyisim, " <3 ", öğrenci2.isim, öğrenci2.soyisim)
