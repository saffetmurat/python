import time
from os import system
import math

class BasitVektorIslemleri():
    __hataMesaji = ""
    __islemYazilari = {
        1: "Bir Vektorün normunu hesaplama",
        2: "Bir Vektorün normalizasyonunu bulma",
        3: "İki vektörün noktasal çarpımını bulma",
        4: "Bir vektörün sıfır vektör olup olmadığını bulma",
        5: "İki vektörün ortogonal olup olmadığını bulma",
        6: "İki Vektör arasındaki açıyı bulma"
    }
    __vektorBilgileri = {}

    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            print("İşlem Menusu".center(40, "-"), end="\n\n")
            for anahtar, deger in self.__islemYazilari.items():
                print(f"{anahtar}) {deger}")

            try:
                self.__hataMesaji = "Geçerli bir işlem numarası girilmedi"
                secenek = int(input("\n\nYapmak İstediğiniz İşlemin Numarasını Giriniz :"))

                if not secenek in range(1, len(self.__islemYazilari)+1):
                    raise Exception

                if secenek == 1:#Bir Vektorün normunu hesaplama
                    self.vektorAlma()
                    sonuc = self.vektorNormuHesaplama()

                    print(f"{sonuc[0]} adlı {sonuc[1]} değerli vektörün normu {sonuc[2]} dir.")

                elif secenek == 2:# Bir Vektorün normalizasyonunu bulma
                    self.vektorAlma()
                    sonuc = self.vektorNormalizasyonunuBulma()

                    print(f"{sonuc[0][0]} adlı {sonuc[0][1]} değerli vektörün normu {sonuc[0][2]}\nnormalizasyon sonucu {sonuc[1]}'dir.")
                
                elif secenek == 3:#İki vektörün noktasal çarpımını bulma
                    self.vektorAlma()
                    print("İkinci vektörü giriniz")
                    self.vektorAlma()
                    self.noktasalCarpim()

                elif secenek == 4:#Bir vektörün sıfır vektör olup olmadığını bulma
                    self.vektorAlma()
                    
                    self.sifirVektorMu()

                elif secenek == 5:#İki vektörün ortogonal olup olmadığını bulma
                    self.vektorAlma()
                    
                    print("İkinci vektörü giriniz")
                    self.vektorAlma()
                    self.ortogonalMi()

                elif secenek == 6:#İki Vektör arasındaki açıyı bulma
                    self.vektorAlma()
                    
                    print("İkinci vektörü giriniz")
                    self.vektorAlma()
                    self.aciBulma()
                    
            except:
                print(f"Hata Mesajı =>\n{self.__hataMesaji}")

            finally:
                durum = input("Yeni bir işlem yapmak için e/E tuşuna basınız : ")
                if durum == "e" or durum == "E":
                    system("cls")
                    self.__vektorBilgileri = {}#yeni bir işlem için eski vektör bilgileri siliniyor.
                else:
                    break


    def vektorAlma(self):
        vektorAd = input(
            "Kullanacağınız vektörün adını giriniz(Örneğin; u, v ...) :")
        if vektorAd == "":
            self.__hataMesaji = "Geçerli Bir Ad girilmedi"
            raise Exception

        print("Sayı dışında bir veri girişi olana kadar vektör için değer girebilirsiniz")

        bilesenler = []
        sayac = 1
        while sayac:
            try:
                bilesenler.append(int(input(f"{sayac}. deger : ")))
                sayac += 1
            except:
                break

        if len(bilesenler) == 0:
            self.__hataMesaji = "Vektor için bir değer girilmedi.."
            raise Exception

        self.__vektorBilgileri[vektorAd] = bilesenler
        bilesenler = []

        system('cls')  # windowsda konsolu temizlemek için kullanılır
        
        print(f"Girdiğiniz {vektorAd} adlı vektorün değeri {self.__vektorBilgileri[vektorAd]}'dir ")
        print("Bu vektor -> {} <- boyutlu bir uzayda bir noktaya karşılık gelmektedir.".format(len(self.__vektorBilgileri[vektorAd])))

    def vektorNormuHesaplama(self,vektörIndeks=0):
        gecici = self.__vektorBilgileri.items()
        # Sözlük listeye çevrildi ve ilk elemanı alında.
        anahtar, deger = list(gecici)[vektörIndeks]
        sonuc = 0
        for eleman in deger:
            sonuc += (eleman)**2

        sonuc = sonuc**0.5
        return anahtar, deger, sonuc

    def vektorNormalizasyonunuBulma(self):
        sonuc = self.vektorNormuHesaplama()

        gecici = self.__vektorBilgileri.items()
        anahtar, deger = list(gecici)[0]

        normalizasyonluVektor = []

        for eleman in deger:
            normalizasyonluVektor.append(eleman / sonuc[2])

        return sonuc, normalizasyonluVektor

    def noktasalCarpim(self):
        gecici = list(self.__vektorBilgileri.items())
        # Sözlük listeye çevrildi ve ilk elemanı alındı.
        vektor1Ad, vektor1Deger = gecici[0]
        vektor2Ad, vektor2Deger = gecici[1]

        sonuc = 0
        if len(vektor2Deger) == len(vektor1Deger):
            for i in range(len(vektor1Deger)):
                sonuc += vektor1Deger[i]*vektor2Deger[i]
            
            print(f"{vektor1Ad} adlı {vektor1Deger} içerikli vektör ile {vektor2Ad} adlı {vektor2Deger} içerikli iki vektörün noktasal çarpımının sonucu => {sonuc}")
        else:
            print("Lütfen iki vektörün uzunluğu aynı olsun.")

    def sifirVektorMu(self):
        gecici = list(self.__vektorBilgileri.items())
        # Sözlük listeye çevrildi ve ilk elemanı alındı.
        vektor1Ad, vektor1Deger = gecici[0]
        vektor2Ad, vektor2Deger = gecici[0]

        sonuc = 0
        
        for i in range(len(vektor1Deger)):
            sonuc += vektor1Deger[i]*vektor2Deger[i]
        
        if sonuc==0:
            print(f"{vektor1Ad} adlı {vektor1Deger} içerikli vektörün kendisi ile olan noktasal çarpımı sonucu=>{sonuc}\nolduğundan bir sıfır vektördür.")
        else:
            print(f"{vektor1Ad} adlı {vektor1Deger} içerikli vektörün kendisi ile olan noktasal çarpımı sonucu=>{sonuc}\nolduğundan  bir sıfır vektör DEĞİLDİR.")           

    def ortogonalMi(self):
        gecici = list(self.__vektorBilgileri.items())
        # Sözlük listeye çevrildi ve ilk elemanı alındı.
        vektor1Ad, vektor1Deger = gecici[0]
        vektor2Ad, vektor2Deger = gecici[1]

        sonuc = 0
        if len(vektor2Deger) == len(vektor1Deger):
            for i in range(len(vektor1Deger)):
                sonuc += vektor1Deger[i]*vektor2Deger[i]

            print(f"{vektor1Ad} adlı {vektor1Deger} içerikli vektör ile {vektor2Ad} adlı {vektor2Deger} içerikli iki vektörün noktasal çarpımının sonucu => {sonuc}")

            if sonuc == 0:
                print("olduğundan bu iki vektör ortogonaldir.")
            else:
                print("olduğundan bu iki vektör ortogonal DEĞİLDİR.")
        else:
            print("Lütfen iki vektörün uzunluğu aynı olsun.")

    def aciBulma(self):

        norm1 = self.vektorNormuHesaplama(0)
        norm2 = self.vektorNormuHesaplama(1)

        #noktasal(skaler) çarpım yapılıyor
        gecici = list(self.__vektorBilgileri.items())
        vektor1Ad, vektor1Deger = gecici[0]
        vektor2Ad, vektor2Deger = gecici[1]

        skalerSonuc = 0
        if len(vektor2Deger) == len(vektor1Deger):
            for i in range(len(vektor1Deger)):
                skalerSonuc += vektor1Deger[i]*vektor2Deger[i]
        else:
            self.__hataMesaji = "Lütfen iki vektörün uzunluğu aynı olsun."
            raise Exception
        #####################################
        cosAci = skalerSonuc/(norm1[2]*norm2[2])

        
        aci = round(math.degrees(math.acos(cosAci)))
        print(f"{vektor1Ad} adlı {vektor1Deger} içerikli vektör ile {vektor2Ad} adlı {vektor2Deger} içerikli iki vektör arasındaki açı => {aci} derecedir.")

########################################################################################################################


if __name__ == "__main__":
    bvi = BasitVektorIslemleri()
    print("Uygulama Kapatılıyor...Bekleyiniz...")
    time.sleep(3)

