#Programın amacı 
#1) random.choice() ifadesi ile listeden rastgele bir değer seçmek. Burada peşepeşe iki defa bu ifade kullanılmıştır. İstenirse random.sample(liste,2)
# ifadesi ile listeden iki tane değeri aynı anda çekebiliriz. Ancak bu değerler birbirlerinin aynısı olmazdı. Bu uygulamda iki değerin birbirine benzer
# olmasına da izin verilmek istendi
#2) Basit bir şekilde, SELECT ve INSERT INTO kalıplarıyla veritabanı üzerinde çalışmak

import os
import sqlite3 as s3
import time
import random

class TakmaAd():
    __veritabani = ""
    __imlec = ""
    __hataMesaji = ""
    __veriler = []

    def __init__(self, adres = os.getcwd() + os.sep + "adlar.db"):
        self.adres = adres
        self.giris()
    
    def baglan(self):
        if os.path.exists(self.adres):
            self.__veritabani = s3.connect(self.adres)
            self.__imlec = self.__veritabani.cursor()
        else:
            self.__hataMesaji = "Sistem belirtilen veritabanını bulamıyor."
            raise Exception
    
    def adCek(self):
        self.baglan()

        sorgu = "SELECT ADLAR_AD FROM ADLAR;"
        sonuc = self.__imlec.execute(sorgu)
        gecici = sonuc.fetchall()
        self.__veriler = [gecici[i][0] for i in range(0,len(gecici))]
        #Veritabanından gelen veri tuple olduğu için bu
        #yapıyla veriler listeye aktarıldı.

    def takmaAdlar(self):
        ilkAd = random.choice(self.__veriler)
        ikinciAd = random.choice(self.__veriler)
        
        print("Takma Ad (Nickname)ınız : {} {}".format(ilkAd, ikinciAd))

    def adEkle(self):

        adListesi = []
        while True:
            eklenecekAd = input("Eklemek istediğiniz adı giriniz : ")
            if not eklenecekAd:
                print("Düzgün bir ad giriniz!")
            else:
                if eklenecekAd in self.__veriler:
                    print("Bu ad veritabanında zaten var! Başka bir ad giriniz...")
                else:
                    adListesi.append(eklenecekAd)
                    tercih = input("Başka bir ad eklemek ister misiniz?(E/e):")
                    if tercih.lower() != "e":
                        print("İsteğiniz üzere bu işlem bitiriliyor")
                        break
        
        for ad in adListesi:
            sorgu = "INSERT INTO ADLAR ( ADLAR_AD ) VALUES ( '{}' );".format(ad)
            self.__imlec.execute(sorgu)
        self.__veritabani.commit()

        print("Yazdığınız Ad(lar) Listeye Eklendi !")

    def adListele(self):
        print(*self.__veriler,sep="\n",end="\n\n")

        print("Toplamda {} tane ad veritabanında bulunmaktadır.".format(len(self.__veriler)))

    def giris(self):
        try:
            while True:
                self.adCek()#Veritabanındaki adlar alınır.

                if self.__veriler==[]:
                    print("Veritabanında herhangi bir ad yok!\nLütfen ad ekleyin...")
                    self.adEkle()

                elif input("\nSizin için bir Takma Ad (Nickname) oluşturalım mı?(E/e) : ").lower() == "e":
                    self.takmaAdlar()

                elif input("\nPeki, ad listemize bir ad eklemek ister misiniz?(E/e) : ").lower() == "e":
                    self.adEkle()

                elif input("\nPeki, ad listemizdeki adları görmek ister misiniz?(E/e) : ").lower() == "e":
                    self.adListele()

                elif input("\nUygulamadan çıkmak ister misiniz?(E/e) : ").lower() == "e":
                    print("\nİsteğiniz üzere uygulama kapatılıyor. :(")
                    break

                self.__veritabani.close()
                
        except Exception:
            print("HATA! ", self.__hataMesaji, "\nBu yüzden Uygulama kapatılıyor...")

        finally:
            time.sleep(2)
            #Kullanıcının son yazılanları fark edeceği kadar Uygulamanın açık kalmasını sağlamak için.

if __name__ == "__main__":
    ta = TakmaAd()
