import random
import time

class SayisalLoto():
    __baslik="Sayısal Loto Kolonu Dolduran Program"

    def __init__(self):
        self.giris()

    def kolonSayisiBelirleme(self):
        while True:
            try:
                kolonSayisi = int(input("Kaç tane kolon üretelim? : "))
                return kolonSayisi
            except:
                print("Bir tam sayı girilmedi. Tekrar deneyin...")

    def giris(self):
        print("*"*len(self.__baslik),self.__baslik,"*"*len(self.__baslik),sep="\n",end="\n")

        while True:
            istek = input("Programdan çıkmak için 1'e devam etmek için herhangi bir tuşa basınız...")

            if istek == "1":
                print("Program Kapatılıyor...")
                time.sleep(1)
                break

            sayi = self.kolonSayisiBelirleme()#sayi tuple cinsinden olur.

            kolon = []
            kolonlar = []
            sayac = 0

            while sayac < sayi:# var olan bir kolon üretince onu kaydetmeyip tekrardan üretiyor.    
                for s in range(0,6):#Bir kolonda 6 tane sayı olduğu için range(0,6)
                    numara = random.randint(1,50)#Bir kolonda [1,50] aralığında sayı vardır.
                    while numara in kolon:#üretilen sayi kolonda varsa tekrardan üretilir.
                        numara = random.randint(1,50)
                    kolon.append(numara)
                    kolon.sort()

                if kolon not in kolonlar:#farklı kolonların üretilmesi için
                    kolonlar.append(kolon)
                    sayac += 1
                    print("{}. kolon = {}".format(sayac,kolon))
                else:
                    kolon=[]
                
if __name__ == "__main__":
    sl = SayisalLoto()
