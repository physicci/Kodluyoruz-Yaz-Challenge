def kelime_sayisi_hesapla(metin):
    kelimeler = metin.split()
    return len(kelimeler)
metin = input("Metni giriniz: ")
kelime_sayisi = kelime_sayisi_hesapla(metin)
print(("Metindeki kelime sayisi:"), kelime_sayisi)