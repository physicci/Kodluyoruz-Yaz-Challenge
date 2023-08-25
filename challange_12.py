def hesapla_tavuk_koyun(toplam_hayvan, toplam_bacak):
    for tavuk_sayisi in range(toplam_hayvan + 1):
        koyun_sayisi = toplam_hayvan - tavuk_sayisi
        if (2 * tavuk_sayisi + 4 * koyun_sayisi) == toplam_bacak:
            return tavuk_sayisi, koyun_sayisi
    return None, None

toplam_hayvan = 36
toplam_bacak = 100

tavuk, koyun = hesapla_tavuk_koyun(toplam_hayvan, toplam_bacak)

if tavuk is not None and koyun is not None:
    print(f"Çiftlikte {tavuk} tavuk ve {koyun} koyun vardır.")
else:
    print("Uygun bir kombinasyon yok.")
