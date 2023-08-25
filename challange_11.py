def ortalama_hesapla(dizi):
    toplam = sum(dizi)
    ortalama = toplam / len(dizi)
    return ortalama

dizi = []
eleman_sayisi = int(input("Dizi kaç elemanli olacak? "))

for i in range(eleman_sayisi):
    eleman = float(input(f"{i+1}. elemani girin: "))
    dizi.append(eleman)


ortalama = ortalama_hesapla(dizi)
print(f"Dizinin ortalamasi: {ortalama}")
