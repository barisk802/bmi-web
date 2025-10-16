print("Araç yolculuk maliyeti hesaplama")

litre_fiyatı =float(input("Benzin Litre Fiyatını Giriniz(TL) : "))
mesafe=float(input("Kat Edilen Mesafeyi Giriniz(KM) : "))
yakıt=float(input("Araç Tüketimini Giriniz Örn:(litre/100) : "))

toplam_yakıt = yakıt * mesafe
toplam_odeme = toplam_yakıt * litre_fiyatı

print("Hesaplanıyor")

print("Gereken Yakıt Miktarı : {}".format(toplam_yakıt))
print("Ödemeniz Gereken Fiyat : {}".format(toplam_odeme))


