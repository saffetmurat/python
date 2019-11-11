import time

class HesapMakinesiIkiSayi():

    __baslik="Kullanıcıdan alınan iki sayı üzerinden kullanıcının istediği işlemlerin yapılması"
    __islemlerIcerigi="""
    1)Toplama                               2)Çıkarma
    3)Çarpma                                4)Bölme(Sonuc Tam sayı olacak)
    5)Bölme(Sonuc Ondalıklı sayı olacak)    6)Mod Alma
    7)Yüzde Alma                            8)Üs Alma
    9)Kök Alma                              10)Geçmişi Görüntüle
    11)Geçmişi Temizle                      12)Hesap Makinesini KAPAT

    Kullanmak istediğiniz işlemin numarasını giriniz :"""

    def __init__(self):
        print("*"*len(self.__baslik),self.__baslik,"*"*len(self.__baslik),sep="\n")
        self.islemler()

    def sayiAl(self):
        while True:
            try:
                sayi1=int(input("İlk Sayıyı giriniz :"))
                sayi2=int(input("İkinci Sayıyı giriniz :"))
                return sayi1, sayi2
            except:
                print("Girdiğiniz değerlerde sıkıntı var. Tekrar deneyiniz.")

    def islemler(self):
      
        gecmis = []
        sayilar = ()

        while True:
            time.sleep(1)

            islem = input(self.__islemlerIcerigi)

            if not islem in [str(i) for i in range(1,13)]:
                print("Girdiğiniz Tuşun Benim İçin Bir Anlamı Yok :(")
                continue
            
            elif islem in [str(i) for i in range(1,10)]:
                sayilar=self.sayiAl()

            elif islem == "10":
                if gecmis:
                    print(*gecmis,sep="\n")
                else:
                    print("Geçmiş BOŞ")
                continue

            elif islem == "11":
                gecmis=[]
                print("Geçmiş Temizlendi.")
                continue

            elif islem == "12":
                print("Program Kapatma İsteğiniz Alındı...\nProgram Kapatılıyor...")
                time.sleep(2)
                break 

            ##############################################################################################

            if islem == "1":           
                gecmis.append("{} + {} = {}".format(sayilar[0], sayilar[1], sayilar[0] + sayilar[1]))

            elif islem == "2":
                gecmis.append("{} - {} = {}".format(sayilar[0], sayilar[1], sayilar[0] - sayilar[1]))

            elif islem == "3":
                gecmis.append("{} * {} = {}".format(sayilar[0], sayilar[1], sayilar[0] * sayilar[1]))

            elif islem == "4":
                gecmis.append("{} // {} = {}".format(sayilar[0], sayilar[1], sayilar[0] // sayilar[1]))

            elif islem == "5":
                gecmis.append("{} / {} = {}".format(sayilar[0], sayilar[1], sayilar[0] / sayilar[1]))

            elif islem == "6":
                gecmis.append("{} denktir {} (mod {})".format(sayilar[0],sayilar[0]%sayilar[1],sayilar[1]))

            elif islem == "7":
                gecmis.append("{} * ( {} / 100 ) = {}".format(sayilar[0], sayilar[1], (sayilar[0] * sayilar[1]) / 100))

            elif  islem == "8":
                gecmis.append("{} ^ {} = {}".format(sayilar[0], sayilar[1],(sayilar[0] ** sayilar[1])))

            elif islem == "9":
                gecmis.append("{} ^ (1/{}) = {}".format(sayilar[0], sayilar[1],(sayilar[0] ** (1 / sayilar[1]))))

            print("Yapılan işlem => {}".format(gecmis[len(gecmis)-1]))
        
if __name__ == "__main__":
    hm = HesapMakinesiIkiSayi()
