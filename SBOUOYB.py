import time
from os import system

class SBOUOYB():
    __aciklama = """Bu uygulama ile Sınıfların Birbirlerine Olan Uzaklıklarının Öklid Yöntemi ile Bulunması(SBOUOYB) amaçlanmaktadır."""
    def __init__ (self):
        system('cls') # konsol ekranı temizleniyor.
        self.menu()
    
    def menu(self):
        while True:
            menuIcerigi={
                "1": "Uygulamanın açıklamasını görmek için 1'e basınız",
                "2": "İşleme başlamak için 2'ye basınız",
                "3": "Çıkış için 3'e basınız"
            }
            for anahtar, deger in menuIcerigi.items():
                print(f"{anahtar}) {deger}")
            sonuc = input("Tercihiniz : ")

            system('cls') # konsol ekranı temizleniyor.

            if sonuc == "1":
                print(self.__aciklama,end="\n\n")

            elif sonuc == "2":
                siniflar = self.veriGirisi()
                self.hesaplama(siniflar)

            elif sonuc == "3":
                break

            else:
                print("Geçersinz bir ifade girdiniz.\nTekrar deneyiniz..",end="\n\n")
            
    def veriGirisi(self):
        while True:
            try:
                hataMesaji = "Bir tamsayı giriniz..."
                boyut = int(input("Bir sınıftaki eleman kaç boyutlu uzayda bir noktayı temsil edecek : "))

                sinifSayisi = int(input(f"{boyut} boyutlu uzayda kaç tane sınıfla işlem yapılacak : "))

                system("cls") # konsol ekranı temizleniyor.

                siniflar = []
                for sinifNumarasi in range(sinifSayisi):
                    sinif = []
                    elemanSayisi = int(input("{}. sinif kaç elemandan oluşmaktadır : ".format(sinifNumarasi+1)))
                    for elemanNumarasi in range(elemanSayisi):    
                        eleman = []
                        for boyutNumarasi in range(boyut):
                            deger = int(input(f"{elemanNumarasi+1}. elemanın {boyutNumarasi+1}. değerini giriniz : "))
                            eleman.append(deger)
                        sinif.append(tuple(eleman))
                    siniflar.append(sinif)
            except:
                print(hataMesaji,"\nTekrar veri girişi yapnız...")
            else:
                #Kullanıcının girdiği değerler gösteriliyor.
                for sinifIndeks in range(len(siniflar)):
                    print(f"{sinifIndeks + 1}. sınıfın elemanları=>")
                    for elemanIndeks in range(len(siniflar[sinifIndeks])):
                        print(f"{siniflar[sinifIndeks][elemanIndeks]}")
                    print("\n\n")
                return siniflar
    def hesaplama(self,siniflar=[]):
        """ 
        Öklit Yönteminde sınıfların homojen ve dairesel bir dağılıma sahip olduğu kabul edilir.
        Bu yüzden sınıfların orta noktaları bulunur ve Öklit yöntemi bu orta noktalar üzerinden yapılır.
        """
        
        #Her bir sınıfın orta noktası bulunur.
        ortaNoktalar = []
        boyut = len(siniflar[0][0]) # 1. sinifin 1. elemanının kaç boyutlu olduğu bulunuyor.

        for sinif in siniflar:
            toplam = [0 for i in range(boyut)]
            for eleman in sinif:
                for indeks in range(boyut):
                    toplam[indeks] += eleman[indeks]
            for indeks in range(boyut):
                toplam[indeks] /= len(sinif)  
            ortaNoktalar.append(tuple(toplam))   
        #######################################
        for indeks in range(len(ortaNoktalar)):
            for i in range(indeks+1,len(ortaNoktalar)):
                sinif1 = ortaNoktalar[indeks]
                sinif2 = ortaNoktalar[i]
                sonuc = self.oklitHesaplama(sinif1, sinif2, boyut)
                print(f"{indeks+1}. sınıf ile {i+1}. sinif arasındaki öklit uzaklığı = {sonuc}")
        print("\n")          

    def oklitHesaplama(self,sinif1, sinif2, boyut):
        toplam = 0
        for indeks in range(boyut):
            toplam += (sinif1[indeks]-sinif2[indeks])**2
        sonuc = toplam**(0.5)

        return sonuc

if __name__ == "__main__":
    sonuc = SBOUOYB()
    print("Uygulama Kapatılıyor.. Bekleyiniz...")
    time.sleep(3)
