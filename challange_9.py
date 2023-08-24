# Bir diziye bağlı kalmadan, kullanıcın girdiği değerlerin içinden; çift-tek sayıların toplamını bulabileceğimiz bir kod parçası olusturdum.
sayilar = []
n = int(input("Kaç tane sayi kullanacaksiniz?: "))
for i in range(n):
      sayi = int(input(f"{i+1}. sayiyi giriniz: "))
      sayilar.append(sayi)

# Değişken kullanıyorum
toplam_cift = 0
toplam_tek = 0
# 'for' döngüsü ile sayıları kontrol ediyoruz...
for sayi in sayilar:
    if sayi % 2 == 0:  
        toplam_cift += sayi  
if sayi % 1 == 0:
     toplam_tek += sayi
# Sonuç;
print("Çift sayilarin toplami:", toplam_cift)
print("Tek sayilarin toplami:", toplam_tek)
