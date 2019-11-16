import time

class Karisik():

    __basliklar = {
        "1" : "Girdiğiniz Sayının Asal Olup Olmadığını Bulan Program",
        "2" : "Fibonacci Sayısını Bulan Program",
        "3" : "Faktöriyel Bulan Program",
        "4" : "Girdiğiniz Sayının Çift/Tek Olup Olmadığını Bulan Program",
        "5" : "Girdiğiniz Sayıya Kadarki Asal Sayıları Bulan Program",
        "6" : "Girilen Sayının Armstrong Sayısı Olup Olmadığını Bulan Program",
        "7" : "Girilen Sayıya Kadarki Armstrong Sayıları Bulan Program",
    }

    __hataMesaji = "Anlaşılamayan bir hata oldu. Program Kapatılıyor..."

    def __init__(self):
        self.tercih()

    def tercih(self):
        while True:

            self.__hataMesaji = "Geçerli bir numara girmediniz.. Program kapatılıyor..."

            print("Uygulamadaki mevcut Programlar aşağıdadır:")

            for anahtar, deger in self.__basliklar.items():
                print("{}) {}".format(anahtar,deger))

            try:
                sira = input("İstediğiniz programın numarasını giriniz : ")

                if sira not in [str(i) for i in range(1,len(self.__basliklar)+1)]:
                    raise Exception
                
                self.baslik(sira)
                if sira == "1":
                    self.asalSayiMi()
                elif sira == "2":
                    self.fibonacciHesaplama()
                elif sira == "3":
                    self.faktöriyelBulma()
                elif sira == "4":
                    self.ciftTekBelirleme()
                elif sira == "5":
                    self.asallariBulma()
                elif sira == "6":
                    self.armstrongMu()
                elif sira == "7":
                    self.armstrongBulma()
                else:
                    pass

            except:
                print(self.__hataMesaji)
                break

            print()
            time.sleep(2)
    
    def baslik(self, sira):
        print("=" * len(self.__basliklar[sira]), self.__basliklar[sira], "=" * len(self.__basliklar[sira]), sep="\n")

    def asalSayiMi(self):
        self.__hataMesaji = "Bir tamsayı girilmedi.. İşlem İptal ediliyor..."
        try:
            sayi=int(input("Sayıyı giriniz :"))

            self.sayiNegatifKontrol(sayi)

            durum = "asaldır."
            for i in range(2,sayi):
                if sayi%i==0:
                    durum = "asal değildir."
                    break

            print("{} sayısı {}".format(sayi, durum))

        except:
            print(self.__hataMesaji)

    def fibonacciHesaplama(self):
        self.__hataMesaji = "Bir tamsayı girilmedi.. İşlem İptal ediliyor..."

        birinciTerim = 0
        ikinciTerim = 1

        try:
            terim = int(input("Kaçınçı terime kadar fibonacci sayılarını bulalım : "))

            self.sayiNegatifKontrol(terim)

            print("1. terim = {}\n2. terim = {}".format(birinciTerim, ikinciTerim))

            for t in range(3, terim+1):
                print("{}. terim = {}".format(t, birinciTerim + ikinciTerim))
                birinciTerim, ikinciTerim = ikinciTerim, (birinciTerim + ikinciTerim)

        except:
            print(self.__hataMesaji)
        
    def faktöriyelBulma(self):
        self.__hataMesaji = "Bir tamsayı girilmedi.. İşlem İptal ediliyor..."

        try:
            sayi = int(input("Hangi sayının faktöriyelini bulalım? : "))

            self.sayiNegatifKontrol(sayi)

            sonuc = 1
            for s in range(2, sayi+1):
                sonuc *= s
            
            print("{} sayısının faktöriyeli => {}".format(sayi,sonuc))

        except:
            print(self.__hataMesaji)

    def ciftTekBelirleme(self):
        self.__hataMesaji = "Bir tamsayı girilmedi.. İşlem İptal ediliyor..."
        try:
            sayi=int(input("Sayıyı giriniz :"))

            self.sayiNegatifKontrol(sayi)
            
            durum = "çifttir."
            if sayi%2 != 0:
                durum = "tektir."
            
            print("{} sayısı {}".format(sayi,durum))

        except:
            print(self.__hataMesaji)

    def asallariBulma(self):
        self.__hataMesaji = "Bir tamsayı girilmedi.. İşlem İptal ediliyor..."
        try:
            sayi=int(input("Sayıyı giriniz :"))

            self.sayiNegatifKontrol(sayi)

            asallar = []
            for s in range(2,(sayi+1)):
                durum=True
                for m in range(2,s):
                    if s%m == 0:
                        durum=False
                        break
                if durum:
                    asallar.append(s)
            
            print("Asal olarak bulunan sayılar =>",asallar)

        except:
            print(self.__hataMesaji)
    
    def armstrongMu(self):
        self.__hataMesaji = "Bir tamsayı girilmedi.. İşlem İptal ediliyor..."
        try:
            sayi=int(input("Sayıyı giriniz :"))

            self.sayiNegatifKontrol(sayi)
            
            sonuc = 0
            basamakSayisi = len(str(sayi))
            for i in str(sayi):
                sonuc += int(i)**basamakSayisi

            if sonuc == sayi:
                print("Girilen {} sayısı bir armstrong sayısıdır.".format(sayi))
            else:
                print("Girilen {} sayısı bir armstrong sayısı değildir.".format(sayi))

        except:
            print(self.__hataMesaji)

    def armstrongBulma(self):
        self.__hataMesaji = "Bir tamsayı girilmedi.. İşlem İptal ediliyor..."
        try:
            sayi=int(input("Sayıyı giriniz :"))

            self.sayiNegatifKontrol(sayi)

            armstronglar = []
            for s in range(2,(sayi+1)):
                sonuc = 0
                basamakSayisi = len(str(s))
                for i in str(s):
                    sonuc += int(i)**basamakSayisi

                if sonuc == s:
                    armstronglar.append(sonuc)
                
            print("Armstrong sayısı olarak bulunan sayılar =>",armstronglar)

        except:
            print(self.__hataMesaji)

    def sayiNegatifKontrol(self, sayi):

        if sayi < 0:
            self.__hataMesaji = "Girilen sayı Negatif olamaz. İşlem İptal ediliyor..."
            raise Exception

if __name__ == "__main__":
    Karisik()
    time.sleep(1)
