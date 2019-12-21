class RakamaCevirme():
    __birBasamakli = { 0 : ['SIFIR', 'Sıfır', 'sıfır'],
        1 : ['BİR', 'Bir', 'bir'],
        2 : ['İKİ', 'İki', 'iki'],
        3 : ['ÜÇ', 'Üç', 'üç'],
        4 : ['DÖRT', 'Dört', 'dört'],
        5 : ['BEŞ', 'Beş', 'beş'],
        6 : ['ALTI', 'Altı', 'altı'],
        7 : ['YEDİ', 'Yedi', 'yedi'],
        8 : ['SEKİZ', 'Sekiz', 'sekiz'],
        9 : ['DOKUZ', 'Dokuz', 'dokuz'],
    }

    __ikiBasamakli={10 : ['ON', 'On', 'on'],
        20 : ['YİRMİ', 'Yirmi', 'yirmi'],
        30 : ['OTUZ', 'Otuz', 'otuz'],
        40 : ['KIRK', 'Kırk', 'kırk'],
        50 : ['ELLİ', 'Elli', 'elli'],
        60 : ['ALTMIŞ', 'Altmış', 'altmış'],
        70 : ['YETMİŞ', 'Yetmiş', 'yetmiş'],
        80 : ['SEKSEN', 'Seksen', 'seksen'],
        90 : ['DOKSAM', 'Doksan', 'doksan'],
    }

    __cokBasamakli = {1000 : ['BİN', 'Bin', 'bin'],
        1000000 : ['MİLYON', 'Milyon', 'milyon'],
        1000000000 : ['MİLYAR', 'Milyar', 'milyar'],
        1000000000000 : ['TRİLYON', 'Trilyon', 'trilyon'],
        1000000000000000 : ['KATTRİLYON', 'Kattrilyon', 'kattrilyon'], 
    }

    def __init__(self):
        self.giris()

    def giris(self):
        metin = input("Bu uygulama harf ile yazdığınız sayısal ifadeleri rakamsal gösterime çevirmektedir.\nÖrnek=> İki kilo elma aldım.\nÇıktısı=>2 kilo elma aldım.\nLütfen metninizi giriniz: ")
        geciciMetin = self.cevir(metin)
        print("Sonuç metin=>")
        print(geciciMetin)
    
    def degerlendirme(self, kelime, sozluk):#bir ve iki basamaklı sayılar için
        gecici = 0

        for anahtar, degerler in sozluk.items():
            for deger in degerler:
                if deger == kelime:
                    gecici += anahtar
                    return gecici, True
        
        return 0, False
    
    def degerlendirme1(self, gecici, toplam, kelime, sozluk):#Çok basamaklı sayılar için
        for anahtar, degerler in sozluk.items(): 
            for deger in degerler:
                if deger == kelime:
                    #gelen kelime dört yüz bin vb. ise
                    if gecici == 0:
                    #"bin lira" cümlesi incelenirken gecici buraya 0 değeriyle gelir.
                    #Bu yüzden gecici'nin değeri 1 yapılır ki çarpma işlemi olsun
                        gecici=1
                    #Burada gecici'nin değeri basamak değeri ile çarpılır.
                    #Örneğin, kırk altı bin, gecici bu satırda 46 değerine sahip olur.
                    gecici *= anahtar #Bu satırda 46 ile 1000 çarpılır.
                    #toplam değişkeni 100'den büyük tüm değeri ve tüm sonuç değerini tutacaktır.
                    toplam += gecici
                    gecici = 0     

                    return (True, gecici, toplam)

        return (False, 0, 0)

    def cevir(self, metin):
        kelimeler = []
        kelimeler = metin.split(" ")#Metin, boşluk karakterine göre parçalanır.
        geciciMetin = ""

        sayac = 0 
        gecici = 0 #yüzden küçük değeri tutacak
        toplam = 0 #yüzden büyük değeri tutacak

        sonuclar = []

        while sayac < len(kelimeler):
            #gelen kelime bir, iki vb. ise onu topluyorum
            sonuclar.append(self.degerlendirme(kelimeler[sayac], self.__birBasamakli))
            sonuclar.append(self.degerlendirme(kelimeler[sayac], self.__ikiBasamakli))
            sonuclar.append(self.degerlendirme1(gecici, toplam, kelimeler[sayac], self.__cokBasamakli))

            if sonuclar[0][1]:
                gecici += sonuclar[0][0]

            #gelen kelime on, yirmi vb. ise onu topluyorum            
            elif sonuclar[1][1]:
                gecici += sonuclar[1][0]           

            elif kelimeler[sayac] == "YÜZ" or kelimeler[sayac] == "Yüz" or kelimeler[sayac] == "yüz":
                gecici*=100
                #Dikkat eilirse "beş yüz doksan milyon üç yüz seksen dokuz" gibi bir ifadede her üç grupta "yüz" kelimesi bulunmaktadır.
                #Yani sayı söylenirken üçerli gruplara bölünür ve her üçerli grubun içinde "yüz" kelmesi bulunmaktadır.
                #Bu üçerli grupları oluşturmak için ilk üç if yapısı kullanıldı.
                #Son elif yapısı ise Örneğin iki yüze seksen beş bin/milyon/trilyon vb. 'deki bin/milyon/trilyon için çalışmaktadır.

            elif sonuclar[2][0]:
                gecici = sonuclar[2][1]
                toplam = sonuclar[2][2]

            else:
                if toplam != 0 or gecici != 0:
                    toplam += gecici#Bu aşamada toplam değişkeni tüm sayısal değeri tutmuş olur.
                    geciciMetin+= (str(toplam)+ " ")
                    toplam = 0
                    gecici = 0
                    geciciMetin += (kelimeler[sayac] + " ")
                else:
                    #Bu aşamada, "yüz yirmi beş bin lira ..." gibi bir cümlede 
                    #if bloğunda incelenen kelime lira demektir.
                    geciciMetin += (kelimeler[sayac] + " ")

            sonuclar = []
            sayac += 1

        if gecici != 0:# bu aşamaya girmesi demek ".... yüz yirmi beş bin" gibi bir cümle var demektir.
            toplam += gecici
            geciciMetin+= (str(toplam)+ " ")
            toplam=0
            gecici=0
        
        return geciciMetin

if __name__ == "__main__":
    rc = RakamaCevirme()