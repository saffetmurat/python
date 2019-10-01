import time

def aciklamalar():
    baslık="""Klavyeden girilen N adet tam sayının 
negatif ve pozit olanları ile tüm sayıların
ayrı ayrı ortalamasını bulan program"""

    print("*"*(len(baslık)//3),baslık,"*"*(len(baslık)//3),sep="\n",end="\n\n")

    print("İşlemin sonlanması için rakam dışında bir karaktere basın !")

def ortalamaHesaplama():

    ortHep = ortPoz = ortNeg = poz = neg = sayP = sayN = 0
    sayac = 1

    while True:

        try:
            sayi = int(input("{}. tam sayıyı giriniz :".format(sayac)))
        except:
            #Hata verirse demekki kullanıcı rakam dışı bir karakter girmiştir.
            print("1) Pozitif{0}{1}\n2) Negatif{0}{2}\n3) Tüm{0}{3}".format(" tam sayıların ortalaması => ",ortPoz, ortNeg, ortHep))
            break
        else:
            #Bu kısım çalışıyorsa demekki giriş verisi uygundur.
            sayac += 1
            if sayi >= 0:
                poz += sayi
                sayP += 1
                ortPoz = poz / sayP
            else:
                neg += sayi
                sayN += 1
                ortNeg = neg / sayN
            
            ortHep = (neg+poz) / (sayN+sayP)

if __name__ == "__main__":
    aciklamalar()
    ortalamaHesaplama()
    print("Program Kapatılıyor....")
    time.sleep(5)
