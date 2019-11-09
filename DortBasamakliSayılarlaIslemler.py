class DortBasamakliSayilar():

    __baslik = {
        "1" : "a+b+c+d=20 ve a.d=24 şartını sağlayan  4 basamaklı sayıları ve miktarını bulma",
        "2" : "a+b+c+d = ab+cd şartını sağlayan 4 basamaklı sayıları ve miktarını bulma",
        "3" : "a*b+c+d = ab+cd şartını sağlayan 4 basamaklı sayıları ve miktarını bulma",
    }

    def __init__(self):
        self.secim()

    def aciklamalar(self, tercih):
        if tercih == "1":
            print("Açıklama =>\na+b+c+d = 20 ve a.d=24 şartını sağlayan 4 basamaklı sayıları bulup ekranda göstermektedir.")
        elif tercih == "2":
            print("Açıklama =>\na+b+c+d = ab+cd şartını sağlayan 4 basamaklı sayıları bulup ekranda göstermektedir.")
        elif tercih == "3":
            print("Açıklama =>\na*b+c+d = ab+cd şartını sağlayan 4 basamaklı sayıları bulup ekranda göstermektedir.")
        else:
            print("Geçersiz bir tercih girdiniz. İşleminiz İptal ediliyor...")
            return False 

    def secim(self):
        for anahtar, deger in self.__baslik.items():
            print("{}) {}".format(anahtar, deger))

        tercih = input("\nTercihinizi giriniz : ")
        if self.aciklamalar(tercih) == False:
            return False

        if tercih == "1":
            self.abcd4BasamakliBul()

        elif tercih == "2":
            self.abArticd()

        elif tercih == "3":
            self.abArticArtid()

        else:
            pass

    def abcd4BasamakliBul(self):

        sayılar=[]
        for s in range(1000,10000):
            m=str(s)
            if (int(m[0]) + int(m[1]) + int(m[2]) + int(m[3])) == 20 and (int(m[0]) * int(m[3])) == 24:
                sayılar.append(s)
        print("Toplamda {} tane bulundu.\nBulunan Sonuc=>".format(len(sayılar)))
        for m in sayılar:
            print(m)

    def abArticd(self):

        sayılar=[]
        for s in range(1000,10000):
            m=str(s)
            if (int(m[0]) + int(m[1]) + int(m[2]) + int(m[3])) == (int(m[0]) * int(m[1]) + int(m[2]) * int(m[3])):
                sayılar.append(s)
        print("Toplamda {} tane bulundu.\nBulunan Sonuc=>".format(len(sayılar)))
        for m in sayılar:
            print(m)

    def abArticArtid(self):

        sayılar=[]
        for s in range(1000,10000):
            m=str(s)
            if (int(m[0]) * int(m[1]) + int(m[2]) + int(m[3])) == (int(m[0]) * int(m[1]) + int(m[2]) * int(m[3])):
                sayılar.append(s)
        print("Toplamda {} tane bulundu.\nBulunan Sonuc=>".format(len(sayılar)))
        for m in sayılar:
            print(m)
            
if __name__ == "__main__":
    DortBasamakliSayilar()
    input("Çıkış için bir tuşa basınız...")