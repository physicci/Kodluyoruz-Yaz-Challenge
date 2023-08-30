urunler = {"kitap": 80, "defter": 20, "kalem": 5}
alinan_urunler = {"kitap": 2, "defter": 3, "kalem": 4}
toplam_odeme = sum(urunler[urun] * alinan_urunler[urun]
                    for urun in urunler)
print("Müşteri toplam", toplam_odeme, "TL ödeme yapmalı.")
