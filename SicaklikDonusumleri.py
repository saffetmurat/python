import time

class Sicaklik():

    __yazilar = ["Girilen sıcaklık değerini istenen sıcaklık değerine dönüştürme",
    "\nAÇIKLAMA ==>",
    """Bu program girilen bir türdeki sıcaklık değerini
istenen başka bir sıcaklık türündeki 
değere dönüştürmeyi amaçlamaktadır.""",
    "\nSistemde Kayıtlı Sıcaklık Türleri =>",
    "\nHangi sıcaklık türünden değer girecekseniz numarasını giriniz :",
    "Sıcaklık Değerini Giriniz :",
    "\nSonucu hangi sıcaklık türünden görmek istiyorsanız onun numarasını giriniz :"
    ]

    def __init__(self):
        self.aciklama()
        self.sicaklikTurleri = ["Celcius", "Reomür", "Fahrenhayt", "Kelvin"]
        self.baslama()

    def aciklama(self):
        print("*" * len(self.__yazilar[0]), self.__yazilar[0], "*" * len(self.__yazilar[0]), sep="\n")
        print(self.__yazilar[1],self.__yazilar[2],self.__yazilar[3], sep="\n")

    def baslama(self):
        try:
            self.tur1 = input("1) {}\n2) {}\n3) {}\n4) {}{}".format(*self.sicaklikTurleri,self.__yazilar[4]))
            self.turSicaklik = float(input(self.__yazilar[5]))

            self.tur2 = input("\n1) {}\n2) {}\n3) {}\n4) {}{}".format(*self.sicaklikTurleri,self.__yazilar[6]))

            self.sicaklikDonusumler()
        except:
            print("Bir hatayla karşılaşıldı!")

    def sicaklikDonusumler(self):

        sonuc = 0.0
        durum =True

        if  self.tur1 == "1" and  self.tur2 == "2":
            sonuc = ( self.turSicaklik * 80)/100
        elif  self.tur1 == "1" and  self.tur2 == "3":
            sonuc = ( self.turSicaklik * 180) / 100 + 32
        elif  self.tur1 == "1" and  self.tur2 == "4":
            sonuc =  self.turSicaklik + 273
        elif  self.tur1 == "2" and  self.tur2 == "1":
            sonuc = ( self.turSicaklik * 100) / 80
        elif  self.tur1 == "2" and  self.tur2 == "3":
            sonuc = (( self.turSicaklik*180)/80) + 32
        elif  self.tur1 == "2" and  self.tur2 == "4":
            sonuc = (( self.turSicaklik*100)/80) + 273
        elif  self.tur1 == "3" and  self.tur2 == "1":
            sonuc = (( self.turSicaklik-32)/180)*100
        elif  self.tur1 == "3" and  self.tur2 == "2":
            sonuc = (( self.turSicaklik-32)/180)*80
        elif  self.tur1 == "3" and  self.tur2 == "4":
            sonuc = ((( self.turSicaklik-32)/180)*100) + 273
        elif  self.tur1 == "4" and  self.tur2 == "1":
            sonuc = ( self.turSicaklik - 273)
        elif  self.tur1 == "4" and  self.tur2 == "2":
            sonuc = (( self.turSicaklik - 273)/100) * 80
        elif  self.tur1 == "4" and  self.tur2 == "3":
            sonuc = ((( self.turSicaklik - 273) / 100) * 180) + 32
        else:
            durum=False
            print("Uygun bir tercih yapmadınız :(")

        if durum:
            print("{} {} = {} {}".format( self.turSicaklik, self.sicaklikTurleri[int( self.tur1)-1], sonuc, self.sicaklikTurleri[int( self.tur2)-1]))

if __name__ == "__main__":
    s = Sicaklik()
    
    say = 20
    while say:
        print("\rProgram Kapatılıyor. Son {} saniye....".format(say),end="")
        time.sleep(1)
        say -= 1
