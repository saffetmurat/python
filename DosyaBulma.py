import os
import subprocess
import string
from ctypes import windll
import datetime
import time

class DosyaBul():

    __sonuclar=[{},{},{},{}]
    #1. sözlük, ad ve uzantı birebir aynı olarak bulunan dosyaları tutar.
    #2. sözlük, ad birebir aynı, uzantı farklı olarak bulunan dosyaları tutar.
    #3. sözlük, ad yaklaşık ve uzantı birebir aynı olarak bulunan dosyaları tutar.
    #4. sözlük, ad yaklaşık aynı, uzantı farklı olarak bulunan dosyaları tutar.

    def __init__(self):
        self.giris()

    def giris(self):
        try:
            baslik = "Girilen dosya adının konumunu arayan program"
            print("*"*len(baslik),baslik,"*"*len(baslik),sep="\n",end="\n\n")

            dosyaAd = input("Aramak istediğiniz dosyanın adını giriniz : ")
            if dosyaAd == "":
                print("HATA ! Bir dosya adı girmediniz!")
                return False
                
            dosyaUzanti = "."+ input("Aramak istediğiniz dosyanın uzantısını giriniz : .")
            dosyaAdUzantili = dosyaAd + dosyaUzanti

            enTepe = ""

            suruculer = self.surucuIsimleri()

            print("Sistemde bulunan sürücüler aşağıdadır : ") 

            for indeks in range(len(suruculer)):
                print("{}) {}".format(indeks+1,suruculer[indeks]))
            print("{}) Tüm sürücülerde".format(len(suruculer)+1))

            
            while True:
                tercih = input("İlgili Dosya yukarıdaki sürücülerden hangisinde aransın?\nSıra numarasını giriniz:")

                try:
                    enTepe = suruculer[int(tercih)-1]  + ":"
                    print("{} sürücüsü inceleniyor. Lütfen bekleyiniz...".format(enTepe))
                    self.bulYazdir(dosyaAd, dosyaUzanti, dosyaAdUzantili, enTepe)
                    break

                except:
                    if tercih == "{}".format(len(suruculer)+1):
                        for indeks in range(len(suruculer)):
                            enTepe = suruculer[indeks] + ":"
                            print("{} sürücüsü inceleniyor. Lütfen bekleyiniz...".format(enTepe))
                            self.bulYazdir(dosyaAd, dosyaUzanti, dosyaAdUzantili, enTepe)                                                           
                    else:
                        print("Geçersiz bir tuşa bastınız!")
                    break

        except Exception as hata:
            print("Anlaşılamayan bir hata oluştu! :(")
            print("Hatanın teknik ifadesi = ",hata)

    def bulYazdir(self, dosyaAd, dosyaUzanti, dosyaAdUzantili, enTepe):        
        try:  
            self.__sonuclar = [{},{},{},{}]
            self.bul(dosyaAd, dosyaUzanti, dosyaAdUzantili, enTepe)

            while True:
                tercih = input("""{} sürücüsünde bulunan sonuçların
1) Sadece dosyaya yazdırılması için 1'e
2) Sadece ekrana yazdırılması için 2'ye
3) Hem dosya hem de ekrana yazdırılması için 3'e basın
Tercihiniz :""".format(enTepe))

                if tercih == "1":
                    self.yazdir("1",enTepe)
                    break

                elif tercih == "2":
                    self.yazdir("2",enTepe)
                    break

                elif tercih == "3":   
                    self.yazdir("1",enTepe)
                    self.yazdir("2",enTepe)
                    break

                else:
                    print("Geçersiz bir tuş girdiniz! Tekrar deneyin!", end="\n\n")
                
        except Exception as hata:
            print("Anlaşılamayan bir hata oluştu! :(")
            print("Hatanın teknik ifadesi = ",hata)


    #Bilgisayarda bulunan sürücülerin isimlerini buluyor.
    def surucuIsimleri(self):

        suruculer = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                suruculer.append(letter)
            bitmask >>= 1

        return suruculer

    def bul(self, dosyaAd, dosyaUzanti, dosyaAdUzantili, enTepe):

        for kokdizin, altDizin, dosya in os.walk( enTepe + os.sep ):

            if len(dosya) > 0:#yani bu dizinde dosya var demektir.
                for dos in dosya:
                    ad, uzanti = os.path.splitext(dos)

                    if dosyaAdUzantili == dos:
                        ek=os.sep.join([kokdizin,dos])
                        self.__sonuclar[0][ek] = dos

                    elif dosyaAd == ad and uzanti != dosyaUzanti:
                        ek=os.sep.join([kokdizin,dos])
                        self.__sonuclar[1][ek] = dos

                    elif dosyaAd in ad and uzanti == dosyaUzanti:
                        ek=os.sep.join([kokdizin,dos])
                        self.__sonuclar[2][ek] = dos   

                    elif dosyaAd in ad and uzanti != dosyaUzanti:
                        ek=os.sep.join([kokdizin,dos])
                        self.__sonuclar[3][ek] = dos

                    else:
                        pass

    def yazdir(self, tercih, enTepe):
        sonucKonum = None

        bulunanlarinSayisi = [
            len(self.__sonuclar[0]),
            len(self.__sonuclar[1]),
            len(self.__sonuclar[2]),
            len(self.__sonuclar[3]), 
            (len(self.__sonuclar[0]) + len(self.__sonuclar[1]) + len(self.__sonuclar[2]) + len(self.__sonuclar[3]))
        ]

        yazilar=[
            "Bunlardan {} tanesinin ad ve uzantıları birebir aynıdır. Bunlar=>",
            "Bunlardan {} tanesinin adları birebir aynı ancak uzantıları farklıdır. Bunlar=>",
            "Bunlardan {} tanesinin adları yaklaşık aynı ancak uzantıları birebirdir. Bunlar=>",
            "Bunlardan {} tanesinin adları yaklaşık aynı ancak uzantıları farklıdır. Bunlar=>",
            "{} dizininde bulunan \"{}\" dosyası"
        ]

        kayitAdi = ""# if sonucKonum != None: bloğunda ilgili yere yazdırmak için burada tanımlandı.
        if tercih == "1":
            tarih = datetime.datetime.now()
            kayitAdi = "Bulunan_Sonuçlar_{}-{}-{}_{}-{}-{}.txt".format(tarih.year, tarih.month, tarih.day, tarih.hour, tarih.minute, tarih.second)
            while os.path.exists(os.getcwd() + os.sep + kayitAdi):
                time.sleep(1)
                kayitAdi = "Bulunan_Sonuçlar_{}-{}-{}_{}-{}-{}.txt".format(tarih.year, tarih.month, tarih.day, tarih.hour, tarih.minute, tarih.second)
    
            sonucKonum = open(kayitAdi,"w+")
            print("Dosya :  ",os.getcwd(), " yolunda {} adıyla kaydedildi.".format(kayitAdi))

        elif tercih == "2":
            sonucKonum = None

        print("{} sürücüsünde, toplamda bu ad veya uzantıya sahip {} tane dosya bulundu.\n".format(enTepe, bulunanlarinSayisi[4]), file = sonucKonum)

        for i in range(0,len(self.__sonuclar)):
            
            if self.__sonuclar[i]:
                print(yazilar[i].format(bulunanlarinSayisi[i]),end="\n" ,file=sonucKonum)
                for anahtar, deger in self.__sonuclar[i].items():
                    print(yazilar[4].format(anahtar,deger), file=sonucKonum)
                print("", file=sonucKonum)

        if sonucKonum != None:
            istek = input("Dosyayı Açmak ister misiniz?[E/e]")
            if istek == "E" or istek == "e":
                subprocess.Popen(['notepad.exe', '{}'.format( os.getcwd() + os.sep + kayitAdi )])
        



if __name__ == "__main__":
    bul = DosyaBul()
    input("Programın Kapatılması için bir tuşa basın!")