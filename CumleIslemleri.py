import time

class CumleIslemleri():
    def __init__(self):
        self.giris()

    def giris(self):
        baslik="Basit Cümle İşleme Uygulaması"
        print("*"*len(baslik),baslik,"*"*len(baslik),sep="\n",end="\n")

        while True:
            print("")
            tercih = input("İşleme başlamak için 1'e\nAçıklamaları görmek için 2'ye\nHakkımda kısmını görmek için 3'e basınız..")
            if tercih == "1":
                while True:
                    self.cumleIslemi()
                    
                    if input("Uygulamadan çıkmak için E/e tuşuna basınız..").upper() == "E":
                        print("Program Kapatılıyor...")
                        time.sleep(2)
                        break 
                break
            elif tercih == "2":
                self.aciklamalar()
            elif tercih == "3":
                self.hakkimda()
            else:
                print("Benim için anlamsız bir tuşa bastınız... Tekrar deneyiniz...")

    def aciklamalar(self):
        aciklama ="""AÇIKLAMALAR=>
        Bu uygulamanın amacı string türünün fonksiyonlarından olan split, strip, lstrip, rstrip, upper, lower, capitalize, replace, startswith, edswith, find, rfind fonksiyonlarını kullanarak bir uygulama yapmaktır.
        Uygulama basit bir cümle işleme uygulaması olarak tasarlanmıştır. 
        """
        print(aciklama)

    def hakkimda(self):
        hakkimda = "\nHAKKIMDA=>\nSaffet Murat tarafından yapıldı\n(Created by: Saffet Murat)\n\nhttps://trmsma.wordpress.com\n\nhttps://github.com/saffetmurat"
        print(hakkimda,end="\n\n")


    def cumleIslemi(self):
        try:
            #1)CÜMLEDEKİ KELİME SAYISINI BULAN PROGRAM
            baslik="1)CÜMLEDEKİ KELİME SAYISINI BULAN PROGRAM"

            print("*"*len(baslik), baslik, sep="\n", end="\n")

            cumle=input("Cümlenizi giriniz: ")
            print("GİRDİĞİNİZ CÜMLEDE TOPLAM", len(cumle.split()),"tane kelime var", sep=" ", end="\n\n")

            print("-"*60, end="\n\n")

            #################################################################################################################################
            #2)CUMLE PARÇALAMA PROGRAMI
            baslik="2)CUMLE PARÇALAMA PROGRAMI"

            print("*"*len(baslik), baslik, sep="\n",end="\n")
            cumle=input("Cümlenizi giriniz: ")
            parcala=input("Neye göre parçalayalım: ")
            print("TOPLAM",len(cumle.split(parcala)), "parçaya ayrılmıştır.","Bulunan Kelimeler =>",cumle.split(parcala),sep="\n",end="\n\n")

            print("-"*60, end="\n\n")

            #################################################################################################################################
            #3)FAZLALIKLARI ATAN PROGRAM
            baslik="3)FAZLALIKLARI ATAN PROGRAM"
            print("*"*len(baslik),baslik,"Sol ve Sağ taraftan belirlediğiniz fazlalıkları atar.",sep="\n")
            cumle=input("Cümleyi giriniz: ")
            atılacak=input("Neyi atalım = ")

            print("Sonuc=>",cumle.strip(atılacak),end="\n\n")

            print("-"*60, end="\n\n")

            #############################################################

            print("Sol taraftan belirlediğiniz fazlalıkları atar.")
            cumle=input("Cümleyi giriniz: ")
            atılacak=input("Neyi atalım = ")

            print("Sonuc=>",cumle.lstrip(atılacak),end="\n\n")

            print("-"*60, end="\n\n")

            #############################################################

            print("Sağ taraftan belirlediğiniz fazlalıkları atar.")
            cumle=input("Cümleyi giriniz: ")
            atılacak=input("Neyi atalım = ")

            print("Sonuc=>",cumle.rstrip(atılacak),end="\n\n")

            print("-"*60, end="\n\n")

            #################################################################################################################################
            #4)CUMLEYİ BÜYÜK YAPAN PROGRAM
            baslik="4)CUMLEYİ BÜYÜK YAPAN PROGRAM"
            print("*"*len(baslik),baslik,sep="\n")
            cumle=input("Cümleyi giriniz: ")
            print("Sonuc=>",cumle.upper(),end="\n\n")

            print("-"*60, end="\n\n")

            #################################################################################################################################
            #5)CUMLEYİ KÜÇÜK YAPAN PROGRAM
            baslik="5)cümleyi küçük yapan program"
            print("*"*len(baslik),baslik,sep="\n")
            cumle=input("Cümleyi giriniz: ")
            print("Sonuc=>",cumle.lower(),end="\n\n")

            print("-"*60, end="\n\n")

            #################################################################################################################################
            #6)CUMLENİN İLK HARFİNİ BÜYÜK YAPAN PROGRAM
            baslik="6)CUMLENİN İLK HARFİNİ BÜYÜK YAPAN PROGRAM"
            print("*"*len(baslik),baslik,sep="\n")
            cumle=input("Cümleyi giriniz: ")
            print("Sonuc=>",cumle.capitalize(),end="\n\n")

            print("-"*60, end="\n\n")

            #################################################################################################################################
            #7)CUMLEDE YER DEĞİŞTİREN PROGRAM
            baslik="7)CUMLEDE YER DEĞİŞTİREN PROGRAM"
            print("*"*len(baslik),baslik,sep="\n")
            cumle=input("Cümleyi giriniz: ")
            eski=input("Neyi kaldıralım? =>")
            yeni=input("Kaldırdığımızın yerine neyi koyalım? =>")
            print("Sonuc=>",cumle.replace(eski,yeni),end="\n\n")

            print("-"*60, end="\n\n")

            #################################################################################################################################
            #8)CÜMLEDE ARANAN VAR MI ÖĞRENEN PROGRAM
            baslik="8)CÜMLEDE ARANAN VAR MI ÖĞRENEN PROGRAM"
            print("*"*len(baslik),baslik,"Cümlenin başında arar.",sep="\n")
            cumle=input("Cümleyi giriniz: ")
            bul=input("Cümlenin başında neyi arayalım =>")
            print("Sonuc ( TRUE ise VAR, FALSE ise YOK )=>",cumle.startswith(bul),end="\n\n")

            print("-"*60, end="\n\n")

            #####################################################
            print("Cümlenin sonunda arar.")
            cumle=input("Cümleyi giriniz: ")
            bul=input("Cümlenin sonunda neyi arayalım =>")
            print("Sonuc ( TRUE ise VAR, FALSE ise YOK )=>",cumle.endswith(bul),end="\n\n")

            print("-"*60, end="\n\n")

            #################################################################################################################################
            #9)CÜMLEDE ARANANIN İNDEKS NUMARASINI BULAN PROGRAM
            baslik="9)CÜMLEDE ARANANIN İNDEKS NUMARASINI BULAN PROGRAM"
            print("*"*len(baslik),baslik,"Cümlenin solundan başlar aramaya.",sep="\n")
            cumle=input("Cümleyi giriniz: ")
            eski=input("Cümlede neyi arayalım =>")
            print("Arananın bulunduğu indeks numarası ( BULAMAZSA -1 değeri gözükür.)=>",cumle.find(eski),end="\n\n")

            print("-"*60, end="\n\n")

            ###################################################################################################

            print("Cümlenin sağından başlar aramaya.",sep="\n")
            cumle=input("Cümleyi giriniz: ")
            eski=input("Cümlede neyi arayalım =>")
            print("Arananın bulunduğu indeks numarası ( BULAMAZSA -1 değeri gözükür.)=>",cumle.rfind(eski),end="\n\n")

            print("-"*60, end="\n\n")

        except Exception as hata:
            print("\nBir hatayla kaşılaşıldı. Tekrar Deneyin...","Hatanın Teknik İfadesi=>",hata,sep="\n",end="\n\n")


if __name__ == "__main__":
    ci = CumleIslemleri()
