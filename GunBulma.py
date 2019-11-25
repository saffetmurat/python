import time

class GunBulma():
    __gunSayisi={#ay:gun
        0 : 0,
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }

    __ayKodlari = {
        1 : 1, #Ocak
        2 : 4,
        3 : 4,
        4 : 7,
        5 : 2,
        6 : 5,
        7 : 7,
        8 : 3,
        9 : 6,
        10 : 1,
        11 : 4,
        12 : 6 #Aralık
    }

    __gunKodlari = {
        1 : "Pazar", 
        2 : "Pazartesi",
        3 : "Salı",
        4 : "Çarşamba",
        5 : "Perşembe",
        6 : "Cuma",
        7 : "Cumartesi"
    }

    def __init__(self):
        self.giris()

    def giris(self):

        while True:
            self.anaMenu()
            onay = input("\nProgramı tekrarlamak ister misiniz? (e/h):").lower() 
            print("\n")
            if onay == "e":
                self.__gunSayisi[2] = 28 #Programda fazlalık yıl olmuşsa 29 oluyor. Bu yüzden işlem tekrarlanacağı vakit 28 yapıldı.
            elif onay == "h":
                print("Program kapatılıyor. Güle Güle...")
                time.sleep(1)
                break
            else:
                print("Geçersiz tuş. Program kapatılıyor. ")
                time.sleep(1)
                break

    def anaMenu(self):

        aciklama="Verilen bir tarihin yılın kaçıncı günü olduğunu\nve haftanın hangi gününe denk geldiğini bulan program"
        print(aciklama,"Lütfen tarihin,",sep="\n\n")

        tarih = self.tarihAlma() #kullanıcıdan tarih bilgisini alıyor.
        self.gunuBulma(tarih) #kullanıcıdan gelen tarih bilgisini kullanarak yılın kaçıncı günü olduğunu buluyor.
        self.gunAdiniBulma(tarih)

    def tarihAlma(self):

        while True:
            mesajlar = []#Karşılaşılan hataları yazdırmak için
            gun, ay, yil = input("Gün Bilgisini giriniz (Rakamla) : "), input("Ay Bilgisini giriniz (Rakamla) : "), input("Yıl Bilgisini giriniz (Rakamla) : ")

            #Girilen gun, ay ve yıl bilgisinin doğru değerlere sahip olup olmadığı belirlenir.
            if not gun.isdigit():
                mesajlar.append("Girilen gün bilgisi rakam değil")
            elif int(gun) <= 0 or int(gun) >= 32:
                mesajlar.append("Girilen gün bilgisinin alabileceği değerler [1-31] aralığındadır.")
            else:
                pass

            if not ay.isdigit():
                mesajlar.append("Girilen ay bilgisi rakam değil")
            elif int(ay) <= 0 or int(ay) >= 13:
                mesajlar.append("Girilen ay bilgisinin alabileceği değerler [1-12] aralığındadır.")       
            else:
                pass

            if not yil.isdigit():
                mesajlar.append("Girilen yıl bilgisi rakam değil")
            else:
                pass    

            #Hatalar Yazdırılıyor.
            if len(mesajlar)>0:
                print("\nKarşılaşılan Hatalar=>",*mesajlar,sep="\n\n",end="\n\n")
                continue

            ###################################################################################

            print("Girilen tarih = {}.{}.{}".format(gun,ay,yil))
            onay = input("Tarihi onaylıyor musunuz? (e/h) :").lower()
            if onay == "e":
                break
            elif onay == "h":
                print("Bilgiler tekrar alınacaktır.")
            else:
                print("Geçersiz tuş. Düzgün bir değer giriniz!")
        
        return gun, ay, yil

    def gunuBulma(self, tarih):

        #Fazlalık yıla göre şubat ayı düzenleniyor.
        fazlalik_gun = self.artikYil(int(tarih[2]))
        if fazlalik_gun:
            self.__gunSayisi[2] = self.__gunSayisi[2] + 1 
        
        son_gun = int(tarih[0])
        for aylar, günler in self.__gunSayisi.items():
            if int(tarih[1]) > aylar:
                son_gun += self.__gunSayisi[aylar]

        print("Girilen {}.{}.{} tarihi yılın {}. günüdür. ".format(tarih[0], tarih[1], tarih[2], son_gun))

    def artikYil(self, yil):#Sonuc 0 ise artık yıl değil, 1 ise artık yıldır.
        
        return 1 if (yil % 4 == 0) and (yil % 100 != 0 or yil % 400 == 0) and yil % 4000 != 0 else 0

    def gunAdiniBulma(self, tarih):

        gecici = tarih[2][len(tarih[2])-2:] #sayının onlar ve birler basamağını almak için
        sonKod = int(tarih[0]) % 7 + self.__ayKodlari[int(tarih[1])] + int(gecici) % 7 + (int(gecici) // 4) % 7
        sonKod = sonKod % 7

        if int(tarih[2]) >= 2000:
            sonKod -= 1

        print("Girilen {}.{}.{} tarihi haftanın {} günüdür. ".format(tarih[0], tarih[1], tarih[2], self.__gunKodlari[sonKod]))


if __name__ == "__main__":
    gb = GunBulma()

