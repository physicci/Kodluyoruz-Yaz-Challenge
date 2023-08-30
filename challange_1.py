def yakalama_zamani(hiz_yarisci1, hiz_yarisci2):
    if hiz_yarisci2 <= hiz_yarisci1:
        return None
    yakalama_suresi = hiz_yarisci1 / (hiz_yarisci2 - hiz_yarisci1)
    return yakalama_suresi

hiz_yarisci1 = 15
hiz_yarisci2 = 20

yakalama_suresi = yakalama_zamani(hiz_yarisci1, hiz_yarisci2)

if yakalama_suresi is not None:
   print(f"İkinci yarismaci ilk yarismaciyi {yakalama_suresi:.2f} saat sonra yakalar.")
else:
    print("İkinci yarismaci ilk yarismaciyi yakalayamaz.")
