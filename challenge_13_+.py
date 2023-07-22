from sympy import symbols, diff, integrate

def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

def sonucu_kontrol_et(sonuc):
    if asal_mi(int(sonuc)):
        print("Sonuç bir asal sayıdır.")
    else:
        print("Sonuç bir asal sayı değildir.")

def hesap_makinesi():
    try:
        sayi1 = float(input("Birinci sayiyi girin: "))
        sayi2 = float(input("İkinci sayiyi girin: "))
        operator = input("İşlem operatörünü girin (+, -, *, /): ")

        if operator == "+":
            sonuc = sayi1 + sayi2
        elif operator == "-":
            sonuc = sayi1 - sayi2
        elif operator == "*":
            sonuc = sayi1 * sayi2
        elif operator == "/":
            sonuc = sayi1 / sayi2
        else:
            print("Geçersiz işlem operatörü.")
            return

        print(f"Sonuç: {sonuc}")
        sonucu_kontrol_et(sonuc)

    except ValueError:
        print("Lütfen geçerli bir sayi girin.")
    except ZeroDivisionError:
        print("Bir sayiyi sifira bölmeye çaliştiniz.")

def turev_al():
    try:
        x = symbols('x')
        ifade = input("Türevini almak istediğiniz ifadeyi girin: ")
        turev_ifadesi = diff(ifade, x)
        print(f"Türev: {turev_ifadesi}")
        sonucu_kontrol_et(turev_ifadesi)

    except Exception as e:
        print(f"Hata: {e}")

def integral_al():
    try:
        x = symbols('x')
        ifade = input("İntegralini almak istediğiniz ifadeyi girin: ")
        integral_ifadesi = integrate(ifade, x)
        print(f"Integral: {integral_ifadesi}")
        sonucu_kontrol_et(integral_ifadesi)

    except Exception as e:
        print(f"Hata: {e}")

def sadece_sayi_girisi():
    try:
        sayi = float(input("Bir sayi girin: "))
        print(f"Girdiğiniz sayi: {sayi}")
        sonucu_kontrol_et(sayi)

    except ValueError:
        print("Lütfen geçerli bir sayi girin.")

def main():
    secim = input("Lütfen yapmak istediğiniz işlemi seçin:\n1- Hesap Makinesi\n2- Sadece Sayi Girişi\n3- Türev Alma\n4- Integral Alma\nSeçiminiz (1/2/3/4): ")

    if secim == "1":
        hesap_makinesi()
    elif secim == "2":
        sadece_sayi_girisi()
    elif secim == "3":
        turev_al()
    elif secim == "4":
        integral_al()
    else:
        print("Geçersiz seçim. Lütfen 1, 2, 3 veya 4 seçeneğini girin.")

main()
