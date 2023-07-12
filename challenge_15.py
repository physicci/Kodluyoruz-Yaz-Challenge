
import datetime

ad = input("Adinizi Giriniz: ")
dogum_yili = int(input("Dogum Yilinizi Girin(YYYY): "))

guncel_tarih = datetime.datetime.now() # bugunun tarihi
guncel_yil = guncel_tarih.year # bugunun yili
yas = guncel_yil - dogum_yili

print("Merhaba {}, yaşiniz {}'dir".format(ad, yas))