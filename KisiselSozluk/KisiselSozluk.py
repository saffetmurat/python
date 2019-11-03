import os
import time

class Sozluk():
    
    __islemler = [
        "1) Kelime Listele",
        "2) Kelime Ara", 
        "3) Kelime Ekle", 
        "4) Kelime Güncelle", 
        "5) Kelime Sil", 
        "6) Toplam Kelime Sayısını Öğren", 
        "7) Programı Kapat", 
    ]

    def __init__(self, adres):
        self.adres = adres
        self.giris()

    def kaydedipKapatma(self, dsy, icerik):
        dsy.seek(0)    #Okuma yapıldığı için imlec sona gelmişti. Başa çekiliyor.
        dsy.truncate() #Dosya yapısı bozulmadan içeriği temizleniyor.
        dsy.writelines(icerik)
        dsy.close() 

    def dosyaAc(self, kip = "r"):
        try:
            #dosya açılırsa ilgili nesne geriye döndürülür.
            dsy = open(self.adres, kip)
            return dsy
        except:
            #dosya açılamadıysa False değeri geriye döndürülür.
            print("Hata ! İlgili dosya bulunamıyor veya açılamıyor ! ")
            return False
    
    def giris(self):

        while True:
            tercih = input("\nMevcut İşlemler =>\n{}\n{}\n{}\n{}\n{}\n{}\n{}\nİstediğiniz işlemin numarasını giriniz : ".format(*self.__islemler))

            if tercih == "1":
                self.kelimeListele()

            elif tercih == "2":
                self.kelimeAra()

            elif tercih == "3":
                self.kelimeEkle()

            elif tercih == "4":
                self.kelimeGuncelle()

            elif tercih == "5":
                self.kelimeSil()
            
            elif tercih == "6":
                self.toplamKelimeSayisi() 

            elif tercih == "7":
                print("\nProgramı Kapatma isteğiniz alınmıştır.\nProgram kapatılıyor... :(")
                time.sleep(3)
                break

            else:
                print("\nGeçersiz bir tuşa basıldı. Bu yüzden herhangi bir işlem yapılmıyor.\n")

    def kelimeListele(self):
        dsy = self.dosyaAc()

        if not dsy:
            #dosya açılmamışsa fonksiyon return komutuyla geriye 
            #False değeri döndürerek sonlanıyor.
            return False

        icerik = dsy.readlines()

        print("Sözlükteki Kelimeler=>",end="\n\n")

        for kelimeler in icerik:
            print("{} = {}".format(kelimeler.split(";")[0].strip("\n"),kelimeler.split(";")[1].strip("\n")))
        print("")

        dsy.close()
    
    def kelimeAra(self):
        secenekler = ["1) Tam kelime araması","2) Benzer kelime araması","1) İlk kısımda", "2) İkinci kısımda", "3) Tüm kısımlarda"]

        tercihTur = input("\nArama Yapmak için aşağıdaki seçenekler bulunmaktadır :\n{}\n{}\nLütfen sıra numarasını giriniz :".format(secenekler[0],secenekler[1]))
        print("")#yeni bir alt satıra geçirmek için

        if tercihTur not in ["1","2"]:
            print("Geçersiz bir tuşa bastınız. İşleminiz İPTAL ediliyor!",end="\n\n")
            return False

        tercihYer = input("Nerede Arama yapalım ?\n{}\n{}\n{}\nLütfen sıra numarasını giriniz :".format(secenekler[2], secenekler[3], secenekler[4]))
        print("")#yeni bir alt satıra geçirmek için

        if tercihYer not in ["1","2","3"]:
            print("Geçersiz bir tuşa bastınız. İşleminiz İPTAL ediliyor!",end="\n\n")
            return False

        aranacak = input("Aranacak kelimeyi girin : ")

        if aranacak == '':
            print("Aranacak kelime girilmedi! İşlem İPTAL ediliyor.")
            return False

        dsy = self.dosyaAc()

        if not dsy:
            #dosya açılmamışsa fonksiyon return komutuyla geriye 
            #False değeri döndürerek sonlanıyor.
            return False
        
        icerik = dsy.readlines()

        print("Bulunan Sonuçlar =>\n")
        if tercihYer == "1": #ilk kısımda(sütunda) arama yapmak için
            for kelimeler in icerik:
                if self.ara(aranacak, kelimeler.split(";")[0].strip("\n"), tercihTur):
                    print("{} = {}".format(kelimeler.split(";")[0].strip("\n"),kelimeler.split(";")[1].strip("\n")))

        elif tercihYer == "2": #ikinci kısımda arama yapmak için
            for kelimeler in icerik:
                if self.ara(aranacak, kelimeler.split(";")[1].strip("\n"), tercihTur):
                    print("{} = {}".format(kelimeler.split(";")[0].strip("\n"),kelimeler.split(";")[1].strip("\n")))

        else : #tercihYer == "3": #tüm kısımlarda arama yapmak için
            for kelimeler in icerik:#ilk kısımda arama yapıyor.
                if self.ara(aranacak, kelimeler.split(";")[0].strip("\n"), tercihTur):
                    print("{} = {}".format(kelimeler.split(";")[0].strip("\n"),kelimeler.split(";")[1].strip("\n")))

            for kelimeler in icerik:#ikinci kısımda arama yapıyor.
                if self.ara(aranacak, kelimeler.split(";")[1].strip("\n"), tercihTur):
                    print("{} = {}".format(kelimeler.split(";")[0].strip("\n"),kelimeler.split(";")[1].strip("\n")))

        print("")#yeni bir alt satıra geçirmek için
        dsy.close()

    def ara(self, aranacak, dizidekiKelime, tur):
        if tur == "1":
            if aranacak == dizidekiKelime:
                return True
        else:
            if aranacak in dizidekiKelime:
                return True

        return False

    def kelimeEkle(self):
        
        ekleKelime1 =  input("Eklenecek kelimeyi giriniz :")

        if ekleKelime1 == '':
            print("Eklenecek kelime girilmedi! İşlem İPTAL ediliyor.")
            return False

        dsy = self.dosyaAc("a+")#sonuna ekleme yapılacak şekilde açıldı.

        if not dsy:
            #dosya açılmamışsa fonksiyon return komutuyla geriye 
            #False değeri döndürerek sonlanıyor.
            return False

        dsy.seek(0)#imleç başa çekildi. Dosyanın okunabilmesi için
        icerik = dsy.readlines()

        for kelimeler in icerik:
            if ekleKelime1 == kelimeler.split(";")[0].strip("\n"):
                print("Sözlükte \"{}\" kelimesi kayıtlı! İsterseniz aşağıdakilerden birini yapabilirsiniz :".format(ekleKelime1))
                print("1) Var olan bu kelimeyi silip yeniden ekleyebilirsiniz\n2) Var olan bu kelimeyi güncelleyebilirsiniz\n")
                dsy.close()
                return False
        
        ekleKelime2 = input("Bu kelimenin karşılığını giriniz :")
        if ekleKelime2 == '':
            print("Eklenecek kelimenin karşılığı girilmedi! İşlem İPTAL ediliyor.")
            dsy.close()
            return False

        #kelime ekleniyor.
        icerik.append(ekleKelime1+";"+ekleKelime2+"\n")
        self.kaydedipKapatma(dsy, icerik)                  

        print("İşlem başarılı bir şekilde yapıldı.")

    def kelimeSil(self):

        silKelime =  input("Silinecek kelimeyi giriniz :")

        if silKelime == '':
            print("Silinecek kelime girilmedi! İşlem İPTAL ediliyor.")
            return False
        
        dsy = self.dosyaAc("a+")#sonuna ekleme yapılacak şekilde açıldı.

        if not dsy:
            #dosya açılmamışsa fonksiyon return komutuyla geriye 
            #False değeri döndürerek sonlanıyor.
            return False
        
        dsy.seek(0)#imleç başa çekildi. dosyanın okunabilmesi için
        icerik = dsy.readlines()


        #Kelime  birinci ve ikinci kısımlarda aranır.
        for kelimeler in icerik: 
            if silKelime == kelimeler.split(";")[0].strip("\n") or silKelime == kelimeler.split(";")[1].strip("\n"):
                icerik.remove(kelimeler)
                self.kaydedipKapatma(dsy, icerik)
                print("İşlem başarılı bir şekilde yapıldı.")
                return True# kelime bulundu ve silindi demektir. Fonksiyonun çalışması durdurulur.

        gecici=[]
        print("Silmek için girdiğiniz \"{}\" kelimesi sözlükte bulunmadı.".format(silKelime))
        for kelimeler in icerik: 
            if silKelime in kelimeler.split(";")[0].strip("\n") or silKelime in kelimeler.split(";")[1].strip("\n"):
                gecici.append(kelimeler)

        if gecici:
            print("Ancak girdiğiniz kelimeye benzer aşağıdaki kelime(ler) sözlükte var.")
            print("Bunlardan birisini mi silmek istediniz?\n")

            sayac = 1
            for kelime in gecici:
                print("{}) {} = {}".format(sayac, kelime.split(";")[0].strip("\n"), kelime.split(";")[1].strip("\n")))
                sayac += 1

            islem = input("\nSilmek istediğinizin sıra numarasını girin. İPTAL etmek için sıra numaraları dışında bir tuşa basın : ")
            try:
                silKelime = gecici[int(islem)-1]
                icerik.remove(silKelime)
                self.kaydedipKapatma(dsy, icerik)
                print("İşlem başarılı bir şekilde yapıldı.")
            except:
                print("İşleminiz İPTAL ediliyor.")

    def kelimeGuncelle(self):

        gunKelime = input("Güncellenecek kelimeyi giriniz : ")

        if gunKelime == '':
            print("Güncellenecek kelime girilmedi! İşlem İPTAL ediliyor.")
            dsy.close()
            return False

        dsy = self.dosyaAc("a+")#sonuna ekleme yapılacak şekilde açıldı.

        if not dsy:
            return False

        dsy.seek(0)#imleç başa çekildi. dosyanın okunabilmesi için
        icerik = dsy.readlines()

        for kelimeler in icerik:
            if gunKelime == kelimeler.split(";")[0].strip("\n"):
                gunKelime1 = input("Kelimenin yeni karşılığını giriniz :")

                if gunKelime1 == '':
                    print("Güncellenecek kelimenin yeni karşılığı girilmedi! İşlem İPTAL ediliyor.")
                    dsy.close()
                    return False

                onay = "{} = {}\nifadesi\n{} = {}\nolarak güncellenecektir. Onaylıyor musunuz?[E/e] :".format(kelimeler.split(";")[0].strip("\n"), kelimeler.split(";")[1].strip("\n"), gunKelime, gunKelime1)
                tercih = input(onay) 
                if tercih == "E" or tercih == "e":
                    icerik.remove(kelimeler)
                    icerik.append(gunKelime+";"+gunKelime1+"\n")
                    self.kaydedipKapatma(dsy, icerik) 
                    print("İşlem başarılı bir şekilde yapıldı.")
                else:
                    print("İşleminiz İPTAL ediliyor.") 

                #evet de dese hayır da dese fonksiyon bu aşamada görevini tamamladığı için bitiriliyor.
                return True#fonksiyonu bitirmek için bir geri dönüş değeri verildi.
        
        gecici = []
        print("Güncellemek için girdiğiniz \"{}\" kelimesi sözlükte bulunmadı.".format(gunKelime))
        for kelimeler in icerik: 
            if gunKelime in kelimeler.split(";")[0].strip("\n"):
                gecici.append(kelimeler)

        if gecici:
            print("Ancak girdiğiniz kelimeye benzer aşağıdaki kelime(ler) sözlükte var.")
            print("Bunlardan birisini mi güncellemek istediniz?\n")

            sayac = 1
            for kelime in gecici:
                print("{}) {} = {}".format(sayac, kelime.split(";")[0].strip("\n"), kelime.split(";")[1].strip("\n")))
                sayac += 1

            islem = input("\nGüncellemek istediğinizin sıra numarasını girin. İPTAL etmek için sıra numaraları dışında bir tuşa basın : ")
            try:
                gunYeniKelime1 = gecici[int(islem)-1].split(";")[0].strip("\n")
                gunYeniKelime2 = gecici[int(islem)-1].split(";")[1].strip("\n")

                gunYeniKelimeY = input("Kelimenin yeni karşılığını giriniz :")

                if gunYeniKelimeY == '':
                    print("Güncellenecek kelimenin yeni karşılığı girilmedi! İşlem İPTAL ediliyor.")
                    dsy.close()
                    return False


                onay = "{} = {}\nifadesi\n{} = {}\nolarak güncellenecektir. Onaylıyor musunuz?[E/e] :".format(gunYeniKelime1, gunYeniKelime2, gunYeniKelime1, gunYeniKelimeY)
                tercih = input(onay) 
                if tercih == "E" or tercih == "e":
                    icerik.remove(gecici[int(islem)-1])
                    icerik.append(gunYeniKelime1 + ";" + gunYeniKelimeY + "\n")
                    print("İşlem başarılı bir şekilde yapıldı.")
                else:
                    print("İşleminiz İPTAL ediliyor.")                    

                self.kaydedipKapatma(dsy, icerik)

            except:
                print("İşleminiz İPTAL ediliyor.")

    def toplamKelimeSayisi(self):
        dsy = self.dosyaAc()

        if not dsy:
            return False

        icerik= dsy.readlines()

        print("\nToplam Kelime Sayısı => {}\n".format(len(icerik)))

if __name__ == "__main__":
    dosya = "{}".format(os.getcwd() + os.sep + "KisiselSozluk.csv")
    soz=Sozluk(dosya)
