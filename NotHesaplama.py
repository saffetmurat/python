import time

class NotHesaplama():

    __yazilar=["1. vize notunuzu giriniz :",
            "2. vize notunuzu giriniz :",
            "Final notunuzu giriniz :",
            "Notlar [0-100] aralığında olabilir. Buna uygun bir değer giriniz.",
            "Not Hesaplama Programı",
            "\nAçıklamaları görmek için 1'e, İşlemlere başlamak için 2'ye, Çıkış için herhangi bir tuşa basınız...",
            "Program kullanıcıdan 1. vize, 2. vize ve final notları için notlar almakta ve ortalamasını hesaplamaktadır.\nOrtalamayı belirlenen aralıklarla kıyaslayarak Harfli Notu üretmektedir.",
            ]

    __araliklar = [0, 40, 50, 65, 80, 90, 100];

    def __init__(self):
        self.giris()
        
    def giris(self):
        print("-"*len(self.__yazilar[4]), self.__yazilar[4], "-"*len(self.__yazilar[4]), sep="\n")

        while True:
            tercih = input(self.__yazilar[5])


            if tercih == "1":
                print(self.__yazilar[6])
            elif tercih == "2":
                self.islemler()
            else:
                print("Program Kapatılıyor...")
                time.sleep(1)
                break

            time.sleep(1)
  
    def islemler(self):
        #Notlar alınıyor.
        notlar=[]

        while len(notlar)<3:
            try:
                gecici=int(input("{}".format(self.__yazilar[len(notlar)])))
                if gecici<0 or gecici>100:
                    print(self.__yazilar[3])
                else:
                    notlar.append(int(gecici))
            except Exception as hata:
                print("Girilen Notlar tam sayı türünde olmalıdır.", hata)

        #########################################################

        #notların ortalaması bulunuyor.
        ortalama = 0
        for m in notlar:
            ortalama += m

        ortalama = ortalama/ len(notlar)

        ##########################################################

        #Harf notu hesaplanıyor.
        harfNotu=""
        if ortalama >= self.__araliklar[0] and ortalama < self.__araliklar[1]:
            harfNotu="FF"
        elif ortalama >= self.__araliklar[1] and ortalama < self.__araliklar[2]:
            harfNotu="DD"
        elif ortalama >= self.__araliklar[2] and ortalama < self.__araliklar[3]:
            harfNotu="CC"
        elif ortalama >= self.__araliklar[3] and ortalama < self.__araliklar[4]:
            harfNotu="BB"
        elif ortalama >= self.__araliklar[4] and ortalama < self.__araliklar[5]:
            harfNotu="AB"
        elif ortalama >= self.__araliklar[6] and ortalama <= self.__araliklar[6]:
            harfNotu="AA"
        else:
            harfNotu="Bir tufalık oldu :("

        ######################################################################

        #Sonuçlar ekrana bastırılıyor.
        print("\nGirilen Notlar =>\n1. vize => {}\n2. vize => {}\nFinal => {}".format(notlar[0],notlar[1],notlar[2]))
        print("Elde edilen ortalama =>",ortalama)
        print("Elde edilen harf notu", harfNotu)

if __name__ == "__main__":
    nh = NotHesaplama()