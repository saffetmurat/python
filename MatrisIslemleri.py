#matrislerle ilgili temel işlemler
import time

class Matris():
    __hataMesaji = ""
    __islemAdlari = ["2 Matrisi Çarpma",
    "Bir matrisin kuvvetini alma",
    "Birim matris oluşturma"
    ]

    def __init__(self):
        self.basla()
    
    def basla(self):
        while True:
            m1 = []
            m2 = []

            yazilar = "\nÇıkış için herhangi bir karaktere basınız.\nYukarıdaki işlemlerden birini seçmek için numarasını giriniz : "
            tercih = input("\n1) {}\n2) {}\n3) {}{}".format(*self.__islemAdlari,yazilar))
           
            if tercih == "1":

                print("\nİlk Matris için :")
                m1 = self.matrisAl()

                if m1 != [] :
                    print("\nİkinci Matris için :")
                    m2 = self.matrisAl()
                if m2 != [] :
                    mSon = self.ikiMatrisCarpmasi(m1, m2)
                    self.matrisBastir(mSon)

            elif tercih == "2":
                
                print("\nMatris için :")
                m1 = self.matrisAl()

                if m1 != [] :
                    try:
                        self.__hataMesaji = "Hata! Girilen Kuvvet Bir Tam Sayı Değil!"
                        us = int(input("\nGirilen Matrisin kaçıncı kuvvetini alalım? :"))
                    except :
                        print(self.__hataMesaji)
                    else:
                        mSon = self.matrisUssuAlma(m1,us)
                        self.matrisBastir(mSon)
            elif tercih == "3":
                self.BirimMatrisOlusturma()

            else:
                print("Çıkış yapılıyor !")
                break

    #Kullanıcıdan matris almayı sağlayan fonksiyon
    def matrisAl(self):
        try:
            matrisAra = []
            matris = []
            self.__hataMesaji = "Hata! Satır-Sutün için bir tam sayı girilmedi!"
            satir = int(input("Matrisin satir sayısını giriniz : "))
            sutun = int(input("Matrisin sutün sayısını giriniz : "))

            self.__hataMesaji = "Hata! Matrise verilen değerler bir tamsayı olmalı!"
            for s in range(satir):
                for m in range(sutun):
                    matrisAra.append(int(input("Matrisin {}. satır - {}. sutün elemanını giriniz :".format(s+1,m+1))))
                matris.append(matrisAra)
                matrisAra = []
            
        except:
            print(self.__hataMesaji)

        finally:
            return matris

    #Parametre olarak gelen matrisi ekrana bastıran fonksiyon
    def matrisBastir(self,matris):
        if matris : #Matris doluysa ekrana yazdırıyor.
            print("Bulunan Sonuc ==>>",end="\n\n")

            for satir in matris:
                print(satir)
            
            print("")

    #İki matrisin çarpımını buluyor.
    def ikiMatrisCarpmasi(self, matris1, matris2):
        try:
            ara = []
            son=[]
            
            carp=0
            toplam=0

            self.__hataMesaji = "Hata! Matrislerin boyutları çarpma işlemi için uyumlu değil!"
            for k in range(len(matris1)):
                for r in range(len(matris1)):
                    for s in range(len(matris1[k])):
                        carp = matris1[k][s] * matris2[s][r]
                        toplam = toplam + carp
                    ara.append(toplam)
                    toplam=0
                son.append(ara)
                ara = [] 
        except:
             print(self.__hataMesaji)
        finally:
            return son

    #Matrisin kuvvetini buluyor.
    def matrisUssuAlma(self, matris,us):
        try:
            ara = []
            son = []
            matrisSon=[]
            matris1 = matris.copy()
            carp = 0
            toplam = 0
            
            self.__hataMesaji = "Hata! Matris çarpımı yapılırken hata oluştu!"
            while us >= 2:
                for k in range(len(matris)):
                    for r in range(len(matris[k])):
                        for s in range(len(matris[k])):
                            carp = matris1[k][s] * matris[s][r]
                            toplam = toplam + carp
                        ara.append(toplam)
                        toplam=0
                    son.append(ara)
                    ara = []
                matris1 = son
                son = []
                us -= 1

            matrisSon = matris1.copy()

        except:
            print(self.__hataMesaji)

        finally:
            return matrisSon

    #Birim matris oluşturma
    def BirimMatrisOlusturma(self):
        try:
            self.__hataMesaji = "Hata! Girilen değer bir tamsayı olmalı!"
            boyut = int(input("Kaç boyutlu birim matris oluşturulsun. Giriniz :"))

            birimMatris = []
            ara=[]

            for s in range(0, boyut):
                for m in range(0, boyut):
                    if s == m:
                        ara.append(1)
                    else:
                        ara.append(0)
                birimMatris.append(ara)
                ara=[]

            self.matrisBastir(birimMatris)
        except:
            print(self.__hataMesaji)

###########################################

if __name__ == "__main__":
    m = Matris()
    time.sleep(1)
    
# A = [ [-1, 4, 9], [4, -95, 1], [2, 1, 9] ]
# B = [ [101, 1, 4], [2, 5, 65], [3, 1, 1] ]

 
# A = [ [-1, 4, 9], [4, -95, 1], [2, 1, 9] ]
# s = 3
