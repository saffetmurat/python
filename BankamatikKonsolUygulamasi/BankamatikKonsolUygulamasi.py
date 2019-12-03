from time import sleep
import os

class BankamatikKonsolUygulamasi():

    __ekran="""____________________________________
    BANKAMATİK KONSOL UYGULAMASI

1- Bakiye Sorgulama
2- Para Yatırma
3- Para Çekme
4- Hesaplarım arası para aktarımı
5- Yeni bir hesap aç
6- Bir hesap sil
7- ÇIKIŞ
____________________________________
"""
    def __init__(self):
        print("\nBANKAMATİK KONSOL UYGULAMASIna Hoş Geldiniz!\nAşağıdaki ekranda gözüken işlemleri yapabilirsiniz")

    def dosyaAc(self, kip="r"):
        if os.path.exists(os.getcwd()+os.sep+"bankamatikKonsolUygulamasi.csv"):
            dosya = open("bankamatikKonsolUygulamasi.csv",kip)
            return dosya
        else:
            print("Sisteme erişmede sıkıntı oldu. Daha sonra tekrar deneyin :(")
            raise Exception

    def sorgula(self):
        dsy = self.dosyaAc()
        
        print("BAKİYENİZ")
        for hesbak in dsy:
            hesap = "Hesap {}, Bakiyeniz = {} TL".format(hesbak.split(";")[0].strip("\n"), hesbak.split(";")[1].strip("\n"))
            print(hesap)

        dsy.close()

    def paraIslemi(self, param=0):
        #param 0 ise para yatırma, 1 ise para çekme olacak
        mesajlar = [
            "Hangi Hesabınıza para yatıracaksınız.\nHesap numarası giriniz : ",
            "Yatırmak istediğiniz miktar : ",
            "Hangi Hesabınızdan para cekeceksiniz.\nHesap numarası giriniz : ",
            "Çekmek istediğiniz miktar : "
            ]

        ###################################################
        self.sorgula()

        dsy = self.dosyaAc("a+")
        dsy.seek(0)#a+'da açıldığı için imlec dosyanın sonunda. Okuma yapabilmek için dosyanın
                #başına getiriliyor.
        
        hesapDurum = "\nGirdiğiniz Hesap Numarası bulunamadı."
        icerik = dsy.readlines()#Dosyanın içeriği okunuyor.
        ###################################################
        
        #Farklılık var
        if param == 0:
            hesap = input("{}".format(mesajlar[0]))
        else:
            hesap = input("{}".format(mesajlar[2]))     
        ###################################################

        for hesbak in icerik:
            hes = hesbak.split(";")[0].strip("\n")
            if hesap == hes:
                bak = int(hesbak.split(";")[1].strip("\n"))

                try:
                    if param == 0:#para yatırma
                        miktar = int(input("{}".format(mesajlar[1])))
                        bak = miktar + bak
                    else:#para çekme
                        miktar = int(input("{}".format(mesajlar[3]))) 
                        if miktar > bak :#çekilecek miktar bakiyeden fazla ise uyarı
                                        #verip işlemi iptal edecek.
                            hesapDurum = "!!!YETERSİZ BAKİYE!\n"+("."*17)
                            break
                        else:
                            bak = bak - miktar
                except:
                    hesapDurum = "Miktar bilgisi rakam olarak girilmediğinden işlem İPTAL edildi."
                    break
                else:
                    bak = str(bak) + "\n"
                    yeni_eklenecek = ";".join([hes,bak])
                    indeks = icerik.index(hesbak)
                    icerik.pop(indeks)
                    icerik.insert(indeks,yeni_eklenecek)
                    hesapDurum = "."*17
                    break
        
        #dosyaya yazılıyor.
        dsy.seek(0)
        dsy.truncate()
        dsy.seek(0)
        dsy.writelines(icerik)
        dsy.close()
        ######################

        #son durum kullanıcıya gösteriliyor.
        print("{}".format(hesapDurum))

        self.sorgula()

    def hesaplarArasi(self):
        self.sorgula()

        dsy = self.dosyaAc("a+")
        dsy.seek(0)#a+'da açıldığı için imlec dosyanın sonunda. Okuma yapabilmek için dosyanın
                #başına getiriliyor.
        
        hesapDurum = "\nGirdiğiniz İLK Hesap Numarası bulunamadı.\n" + "."*17

        hesaplarVarmi = [0, 0]   #Kullanıcının girdiği hesapların olup olmadığını tutuyor. 0 hesap yok demektir.
        icerik = dsy.readlines() #Dosyanın içeriği okunuyor.

        hes1 = input("Hangi hesabınızdan para alınsın? : ")

        bakSon = []
        hesSon = []

        for hesbak in icerik:
            hes = hesbak.split(";")[0].strip("\n")
            if hes1 == hes:
                hesaplarVarmi[0]=1#ilk girilen hesap var demek
                bakSon.append(int(hesbak.split(";")[1].strip("\n")))
                hesSon.append(hesbak)
                hesapDurum = "."*17
                break

        if hesaplarVarmi[0] == 1:
            hes2 = input("Hangi hesabınıza para eklensin? : ")

            if hes2 == hesSon[0].split(";")[0].strip("\n"):
                hesapDurum = "\nPara gönderen ve alan hesap numarası aynı olamaz.\n" + "."*17
            else:
                for hesbak in icerik:
                    hes = hesbak.split(";")[0].strip("\n")
                    if hes2 == hes:
                        hesaplarVarmi[1]=1#ikinci girilen hesap var demek
                        bakSon.append(int(hesbak.split(";")[1].strip("\n")))
                        hesSon.append(hesbak)
                        break
                if len(hesSon)<2:
                    hesapDurum = "\nGirdiğiniz İKİNCİ Hesap Numarası bulunamadı.\n" + "."*17


        if hesaplarVarmi[1] == 1:#Doğru hesap girildi demektir.
            miktar = int(input("Ne kadar para transfer edilsin? :"))
            if miktar > bakSon[0]:
                hesapDurum = "Bu işlem için hesabınızda YETERLİ PARA YOK !"
            else:
                bakSon[0] = bakSon[0] - miktar
                bakSon[1] = bakSon[1] + miktar

                ##Hesaplar güncelleniyor.
                for i in range(2):
                    indeks = icerik.index(hesSon[i])
                    icerik.pop(indeks)
                    bak = str(bakSon[i]) + "\n"
                    yeni_eklenecek = ";".join([hesSon[i].split(";")[0].strip("\n"),bak])
                    icerik.insert(indeks,yeni_eklenecek)
                ###########################################


        #dosyaya yazılıyor.
        dsy.seek(0)
        dsy.truncate()
        dsy.seek(0)
        dsy.writelines(icerik)
        dsy.close()
        ######################

        #son durum kullanıcıya gösteriliyor.
        print("{}".format(hesapDurum))

        self.sorgula()

    def hesapAc(self):
        import random as rm
        tercih = input("Yeni bir hesap açmak istediğinizden emin misiniz? E/H : ").lower()  
        if tercih == "e":
            dsy = self.dosyaAc("a+")
            dsy.seek(0)#a+'da açıldığı için imlec dosyanın sonunda. Okuma yapabilmek için dosyanın
                    #başına getiriliyor.
            
            icerik = dsy.readlines() #Dosyanın içeriği okunuyor.
            
            hesapNo = ""
            if icerik:#içerik doluysa 
                devam = True
                indeks = 0
                while devam:
                    hesapNo = str(rm.randrange(1,101))
                    devam = False
                    for hesbak in icerik:
                        hes = hesbak.split(";")[0].strip("\n")
                        if hesapNo == hes:
                            devam = True
                            break
                #Hesapları sıralıyor.
                for hesbak in icerik:
                    hes = hesbak.split(";")[0].strip("\n")
                    if int(hesapNo) < int(hes):
                        indeks = icerik.index(hesbak)
                        yeni_eklenecek = ";".join([hesapNo,"0\n"])
                        icerik.insert(indeks,yeni_eklenecek)
                        break                      
            ##############################################
            else:#Hiç hesabı yoksa
                hesapNo = str(rm.randrange(1,101))
                yeni_eklenecek = ";".join([hesapNo,"0\n"])
                icerik.append(yeni_eklenecek)          

            #dosyaya yazılıyor.
            dsy.seek(0)
            dsy.truncate()
            dsy.seek(0)
            dsy.writelines(icerik)
            dsy.close()
            ######################

            #son durum kullanıcıya gösteriliyor.
            print("{}".format("."*17))

            self.sorgula()

        elif tercih == "h":
            print("Yeni bir hesap açma İŞLEMİ İPTAL EDİLDİ...\n")
        else:
            print("{}\n{}".format("UYARI!","Geçerli bir işlem seciniz"))   

    def hesapSil(self):
        tercih = input("Hesap silmek istediğinizden emin misiniz? E/H : ").lower()  
        if tercih == "e":
            self.sorgula()   
            hesapNo = input("Hangi hesabı silmek istiyorsunuz: ")

            dsy = self.dosyaAc("a+")
            dsy.seek(0)#a+'da açıldığı için imlec dosyanın sonunda. Okuma yapabilmek için dosyanın
                    #başına getiriliyor.
            
            icerik = dsy.readlines() #Dosyanın içeriği okunuyor.

            hesapDurum = "\nGirdiğiniz Hesap Numarası bulunamadı.\n" + "." * 17
            for hesbak in icerik:
                hes = hesbak.split(";")[0].strip("\n")
                if hesapNo == hes:
                    
                    bakiye = int(hesbak.split(";")[1].strip("\n"))
                    if bakiye < 0:
                        hesapDurum = "\nHesabınızda borç olduğundan hesap SİLİNEMEZ\n" + "." * 17
                    elif bakiye == 0:
                        icerik.remove(hesbak)
                        hesapDurum = "\nHesap silindi\n" + "." * 17
                    else:
                        hesapDurum = "Hesabınızda para bulunuyor. Hesabı silmeden önce parayı alınız.\n" + "." * 17
                    break
                            
            #dosyaya yazılıyor.
            dsy.seek(0)
            dsy.truncate()
            dsy.seek(0)
            dsy.writelines(icerik)
            dsy.close()
            ######################

            #son durum kullanıcıya gösteriliyor.
            print("{}".format(hesapDurum))

            self.sorgula()

        elif tercih == "h":
            print("Hesap silme İŞLEMİ İPTAL EDİLDİ...\n")
        else:
            print("{}\n{}".format("UYARI!","Geçerli bir işlem seciniz"))   

    def anaEkran(self):
        try:
            while True:
                print(self.__ekran)
                secenek = input("Hangi işlemi yapmak istiyorsunuz :  ")

                if secenek == "1":
                    self.sorgula()
                elif secenek == "2":
                    self.paraIslemi()
                elif secenek == "3":
                    self.paraIslemi(1)
                elif secenek == "4":
                    self.hesaplarArasi()
                elif secenek == "5":
                    self.hesapAc()
                elif secenek == "6":
                    self.hesapSil()
                elif secenek == "7":
                    tercih = input("Çıkmak istediğinizden emin misiniz? E/H : ").lower()
                    if tercih == "e":
                        print("ÇIKIŞ İŞLEMİ YAPILIYOR...\nLÜTFEN BİRAZ BEKLEYİNİZ...")
                        sleep(2)#2 saniye bekletiyor.
                        break
                    elif tercih == "h":
                        print("ÇIKIŞ İŞLEMİ İPTAL EDİLDİ...\n")
                    else:
                        print("{}\n{}".format("UYARI!","Geçerli bir işlem seciniz"))   
                else:
                    print("{}\n{}".format("UYARI!","Geçerli bir işlem seciniz"))
        except:
            print("Beklenmedik bir hatayla karşılaşıldığından dolayı ÇIKIŞ İŞLEMİ YAPILIYOR...")
            sleep(2)#2 saniye bekletiyor.

if __name__ == "__main__":
    bku = BankamatikKonsolUygulamasi()
    bku.anaEkran()