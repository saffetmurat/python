import time

class TabanDonusturme():
    __baslik = "TAM SAYILAR İÇİN TABAN DÖNÜŞÜMLERİ (2,3,4,5,6,7,8,9,10)"
    __hataMesaji = ""
    

    def __init__(self):
        #print ile başlık oluşturuluyor.
        print("*"*len(self.__baslik),self.__baslik,"*"*len(self.__baslik),sep="\n",end="\n\n")
        self.islemler()

    def islemler(self):
        try:
            self.__hataMesaji = "Girilen sayı bir tamsayı değil!"
            taban=int(input("Sayının Tabanını girin :"))

            sayı=int(input("Sayıyı girin :"))
            if (sayı < 0):
                self.__hataMesaji = "Girilen sayı negatif olamaz!"
                raise Exception                
            
            sayı=str(sayı)
            tabanKabul=[2,3,4,5,6,7,8,9,10]

            if tabanKabul.count(taban)==0:
                self.__hataMesaji = "Kabul edilen tabanlardan biri girilmedi"
                raise Exception

            for i in sayı:
                if taban <= int(i):
                    self.__hataMesaji = "Bir basamaktaki rakam tabana eşit veya tabandan büyük olamaz!"
                    raise Exception

            self.__hataMesaji = "Sayı bir tamsayı değil!"
            taban1=int(input("Girilen Sayının Hangi Tabandaki karşılığı bulunsun :"))
            if tabanKabul.count(taban1)<=0:
                self.__hataMesaji = "Kabul edilen tabanlardan biri girilmedi"
                raise Exception

            self.__hataMesaji = "Hatanın nedeni anlaşılamadı!"
            toplam = 0
            kuvvet = len(sayı) - 1
            #girilen sayının önce onluk tabandaki karşılığı bulunur
            for i in sayı:
                toplam+=int(i)*(taban**kuvvet)
                kuvvet-=1
            #onluk tabandan girilen sayıya çevrildi
            print(toplam)
            bolum=toplam
            eleman = []
            while bolum>0:
                eleman.append(bolum%taban1)
                bolum=bolum//taban1

            son=""
            for i in eleman:
                son=str(i)+son
            print("Elde edilen sonuc :", son)

        except Exception:
            print("Hata nedeni : ", self.__hataMesaji)

if __name__ == "__main__":
    tb = TabanDonusturme()

    sayac = 20
    while sayac:
        print("\rProgram Kapatılıyor. Son {} saniye ...".format(sayac),end="")
        time.sleep(1)
        sayac -= 1
