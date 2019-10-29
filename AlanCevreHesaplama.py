import math

class AlanCevreHesaplama():

    __turler = ('Üçgen', 'Dikdörtgen' , 'Çember')

    def __init__(self):
        self.tercih()

    def tercih(self):
        self.durum = input("Alan mı Çevre mi hesaplansın\n(Alan için 1'e Çevre için 2'ye basınız..): ")
        if self.durum not in ["1","2"]:
            print("Geçersiz bir tuşa bastınız. İşleminiz İPTAL ediliyor....")
            return False

        print("Aşağıdakilerden hangisi için hesaplama yapalım ?")

        for indeks in range(len(self.__turler)):
            print("{}) {}".format(indeks+1, self.__turler[indeks]))

        tercih = input("Tercihinizin sıra numarasını giriniz : ")
        
        if tercih == "1":
            self.ucgenHesaplama()
        elif tercih == "2":
            self.dikdortgenHesaplama()
        elif tercih == "3":
            self.cemberHesaplama()
        else:
            print("Girdiğiniz karakter geçerli bir tuşa karşılık gelmiyor...")

    def ucgenHesaplama(self):
        try:
            bir = float(input("\nÜçgenin birinci kenarını giriniz :"))
            iki = float(input("Üçgenin ikinci kenarını giriniz :"))
            uc = float(input("Üçgenin üçüncü kenarını giriniz :"))
        except:
            print("Düzgün bir sayı girilmediği için işlem İPTAL ediliyor....")
        else:
            if self.durum == "1":
                U = (bir + iki + uc) / 2
                alan = (U * (U - bir) * (U - iki) * (U - uc)) ** (1 / 2)
                print("Birinci kenarı {}, İkinci kenarı {},Üçüncü kenarı {} olan üçgenin alanı {}".format(bir, iki, uc, U))
            else:
                print("Birinci kenarı {}, İkinci kenarı {},Üçüncü kenarı {} olan üçgenin çevresi {}".format(bir, iki, uc, bir + iki + uc))

    def dikdortgenHesaplama(self):
        try:
            bir = float(input("\nDikdörtgenin uzun kenarını giriniz :"))
            iki = float(input("Dikdörtgenin kısa kenarını giriniz :"))
        except:
            print("Düzgün bir sayı girilmediği için işlem İPTAL ediliyor....")
        else:
            if self.durum == "1":
                print("Uzun kenarı {}, Kısa kenarı {} olan dikdörtgenin alanı {}".format(bir,iki,bir*iki))
            else:
                print("Uzun kenarı {}, Kısa kenarı {} olan dikdörtgenin çevresi {}".format(bir,iki,(bir+iki)*2))

    def cemberHesaplama(self):
        try:
            yaricap = float(input("\nÇemberin yarıçapını giriniz :"))
        except:
            print("Düzgün bir sayı girilmediği için işlem İPTAL ediliyor....")
        else:
            if self.durum == "1":
                print("Yarı çapı {} olan çemberin alanı {}".format(yaricap, math.pi*yaricap*yaricap))
                #Ya da 
                #print("Yarı çapı {} olan çemberin alanı {}".format(yaricap, math.pi*(yaricap**2)))
            else:
                print("Yarı çapı {} olan çemberin çevresi {}".format(yaricap, 2*math.pi*yaricap))


if __name__ == "__main__":
    AlanCevreHesaplama(),
    input("Çıkış için bir tuşa basınız....")