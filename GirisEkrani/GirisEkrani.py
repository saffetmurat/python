from SifreKontrolu import Kontroller as sk
import os
import time

class Giris():

    def __init__(self, adres = os.getcwd()+os.sep+"girisVeritabani.csv"):
        self.adres = adres

    def dosyaAc(self, kip = "r"):
        if os.path.exists(self.adres):
            dosya = open(self.adres, kip)
            return dosya
        else:
            raise Exception("Sisteme erişirken bir hata oldu :(\nVeritabanı bulunamıyor.\nSonra tekrar deneyiniz.")        

    def kullaniciVarmi(self):
        print("\nSisteme girmek için Kullanıcı Adınızı girmeniz gerekmektedir.")
        dsy = self.dosyaAc()
        icerik = dsy.readlines()
        dsy.close()

        while True:
            kulAd = input("\nKullanıcı Adınızı Giriniz : ")

            for ad in icerik:
                if kulAd == ad.split(";")[0].strip("\n"):
                    return True, kulAd, ad.split(";")[1].strip("\n") #Kullanıcı adıyla şifre geriye döndürülür.
            
            print("Böyle bir kullanıcı kayıtlı değil :(\nTekrar deneyiniz :)")

            if "e" == input("Sistemden çıkmak için e/E tuşuna basınız...").lower():
                return (False,)
    
    def girisKismi(self, sonuc=(False,)):
        if not sonuc[0]:#Buraya girMEZSE demek ki yeni bir kayıt yapılmıştır.
                        #Bu durumda zaten kullanıcı adı ve şifresi sonuc değişkeninde vardır.
            sonuc = self.kullaniciVarmi()

        if sonuc[0]:#True ise kullanıcı adı ve şifresi sonuc değişkeninde vardır.
            print("Sisteme girmek için Şifrenizi girmeniz gerekmektedir.")

            for hak in range(2,-1,-1):
                sifre = input("Merhaba {} !\n Lütfen şifrenizi giriniz : ".format(sonuc[1]))
                if sifre == sonuc[2]:
                    print("\nGirdiğiniz \" {} \" sifresi DOĞRU.\nHOŞ GELDİNİZ!\nSistem açılıyor....".format(sonuc[2]))
                    break
                else:
                    print("\nGirdiğiniz \" {} \" sifresi YANLIŞ. {} hakkınız kaldı.".format(sifre, hak))
            else:
                print("\nSürekli yanlış şifre girildiğinden sistem kapatıldı. Sonra Tekrar deneyiniz...")
        else:
            print("İsteğiniz üzere sistem kapatılıyor...")
        
    def yeniKayit(self):
        dsy = self.dosyaAc("a+")
        dsy.seek(0) #imlec dosyanın başına çekilir.
        icerik = dsy.readlines()

        kulad = ""
        while True:
            kulad = input("Kullanacağınız Kullanıcı Adınızı giriniz :")   
            for ad in icerik:
                if kulad == ad.split(";")[0].strip("\n"):
                    print("\nGirdiğiniz {} kullanıcı adı kullanılmaktadır.\nBaşka bir tane seçiniz.\n".format(kulad))  
                    break
            else:
                break

        print("Merhaba {} !\nSisteme girerken kullanmak istediğiniz şifreyi giriniz... ".format(kulad))
        print("Şifrenin uygunluğu tespit edilecektir =>\n")
        kulSifre = sk()#__init__() fonksiyonunun içindeki self.kontrol()'den dolayı bir daha kontrol() fonksiyonunu çağırmaya gerek yok.
        
        dsy.write( kulad + ";" + kulSifre.sifreAl() + "\n")  #sifreAl() ile self.kontrol()'de belirlenen şifre alınmaktadır.
        print("İşlem başarılı bir şekilde tamamlanmıştır.")
        dsy.close()

        if input("Merhaba {}!\n Siteme giriş yapmak ister misin?(E/e)".format(kulad)).lower() == "e":
            self.girisKismi((True, kulad, kulSifre.sifreAl()))
        else:
            print("İsteğiniz üzere giriş sayfasına yönlendirilmiyorsunuz.\nBu durumda program kapatılıyor...")


    def anaKisim(self):
        try:
            secenek=input("Sisteme girmek için 1'e\nYeni kayıt oluşturmak için 2'ye \nbasınız:") 

            if secenek == "1":
                self.girisKismi()
            elif secenek == "2":
                self.yeniKayit()
            else: 
                print("Geçersiz bir tuş girdiniz.\nİşleminiz iptal ediliyor.")
        except Exception as hata:
            print("HATA! ", hata)
            
        time.sleep(2)

if __name__ == "__main__":
    grs = Giris()
    grs.anaKisim()