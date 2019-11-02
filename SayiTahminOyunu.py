import random, time

class SayiTahminOyunu():

    def __init__(self):
        self.aciklamalar()

    def aciklamalar(self):
        print("Aklımda, 0 ile 100 arasında bir sayı tuttum. Hadi bu sayıyı tahmin et... :)")
        print("Not: Oyundan çıkmak için rakam dışında bir karaktere bas.")
        
    def sayiUret(self):
        return random.randint(0,101)

    def tahminEtme(self):
        sayi = self.sayiUret()
        tahminSayisi = 0

        while True:
            try:

                girilen = int(input("Tahmininizi giriniz: "))
                tahminSayisi += 1

                if sayi == girilen:
                    print("Tebrikler {} sayısını {}. tahmininizde buldunuz.".format(sayi, tahminSayisi))
                    print("\nYeni bir sayı tuttum. Hadi Tahmin Et!")
                    sayi = self.sayiUret()
                    tahminSayisi = 0
                elif sayi < 0 and sayi > 100:
                    print("Girdiğiniz {} sayısı, 0 ile 100 arasında bir sayı değil!".format(girilen))
                elif sayi < girilen:
                    print("Girdiğin {} sayısı aklımda tuttuğum sayıdan büyük!".format(girilen))               
                elif sayi > girilen:
                    print("Girdiğin {} sayısı aklımda tuttuğum sayıdan küçük!".format(girilen)) 

            except:
                print("Oyundan çıkış isteğiniz alındı.") 
                break               

if __name__ == "__main__":
    s = SayiTahminOyunu()
    s.tahminEtme()
    print("Program Kapatılıyor. Bekleyiniz...")
    time.sleep(2)
