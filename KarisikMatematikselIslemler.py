import random as rastgele
import os

class Matematik():

    __baslik={
            "1": "\n1) Klavyeden girilen N adet sayıdan en büyük ve en küçük olanını bulma",
            "2": "\n2) Bir dizideki negatif ve pozitif tam sayıları bulma",
            "3": "\n3) Bir dizideki elemanların aritmetik ve geometrik ortalmasını bulma",
            "4": "\n4) Girilen Veriye göre Faktöriyel sonucunu bulma",
            "5": "\n5) Girilen Verilere Göre Permütasyon sonucunu bulma",
            "6": "\n6) Girilen Verilere Göre Kombinasyon sonucunu bulma",
            "7": "\n7) Girilen Verilere Göre Binom açılımını bulma"
        }

    __hataMesaji = ""

    def __init__(self):
        self.giris()

    def giris(self):
        while True:

            print("\nUYGULAMALAR{}{}{}{}{}{}{}\nÇıkış için buradaki sıra numaralarının dışında bir karakter girin.".format(*self.__baslik.values()))
            sira = input("Kullanmak istediğiniz uygulamanın Sıra Numarasını yazınız :")

            if sira == "1":
            	self.EnBuyukEnKucukBul()
            elif sira == "2":
            	self.NegatifPozitifBulma()
            elif sira == "3":
            	self.AritmetikGeometrikOrt()
            elif sira == "4":
            	print("/" * len(self.__baslik["4"]), self.__baslik["4"], "/" * len(self.__baslik["4"]), sep="\n", end="\n\n")
            	try:
            		self.__hataMesaji="Bir tam sayı girilmedi !"
			
            		sayi = int(input("Hangi sayının faktöriyelini alalım :"))
            		if sayi < 0:
            			self.__hataMesaji="Girilen sayı negatif olamaz !"
            			raise Exception
				
            		sonuc=self.FaktoriyelBulma(sayi)
            		print("{} sayısının faktöriyeli {}".format(sayi,sonuc))
            	except Exception:
            		print("Hata ! {}".format(self.__hataMesaji))	
            elif sira == "5":
            	self.PermutasyonBulma()
            elif sira == "6":
            	self.KombinasyonBulma()
            elif sira == "7":
            	self.BinomAcilimi()
            else:
            	print("Uygulama Kapatılıyor.")
            	break
    
    def EnBuyukEnKucukBul(self):
        print("-"*len(self.__baslik["1"]), self.__baslik["1"], "-"*len(self.__baslik["1"]),sep="\n",end="\n\n")

        try:
            self.__hataMesaji="Bir tam sayı girilmedi !"
            boy = int(input("Dizinin eleman sayısını giriniz :"))

            if boy < 0 :
                self.__hataMesaji="Dizinin eleman sayısı negatif olamaz !"
                raise Exception                

            say = 3
            eleman = []
            max=int(input("{}. sayıyı giriniz :".format(1)))
            eleman.append(max)
            min=int(input("{}. sayıyı giriniz :".format(2)))
            eleman.append(min)

            while boy >= say:
                sayi = int(input("{}. sayıyı giriniz :".format(say)))
                if max < sayi:
                    max = sayi
                if min > sayi:
                    min = sayi
                eleman.append(sayi)
                say += 1

            print("Tüm elemanlar=> {}\nEn büyük eleman {}\nEn küçük eleman {}".format(eleman, max, min))
        except:
            print("Hata ! {}".format(self.__hataMesaji))

    def NegatifPozitifBulma(self):
        print("+"*len(self.__baslik["2"]), self.__baslik["2"], "+"*len(self.__baslik["2"]),sep="\n",end="\n\n")
        try:
            self.__hataMesaji="Bir tam sayı girilmedi !"
            boy = int(input("Dizinin eleman sayısını giriniz :"))

            if boy < 0 :
                self.__hataMesaji="Dizinin eleman sayısı negatif olamaz !"
                raise Exception  

            say = 1
            dizi=[]
            eleNeg = elePoz = 0
            while boy >= say:
                eleman = int(input("Dizinin {}. elemanını giriniz :".format(say)))
                say+=1
                if eleman<0:
                    dizi.insert(0,eleman)
                    eleNeg += 1
                else:
                    dizi.append(eleman)
                    elePoz += 1

            print("Toplam {} tane negatif, {} pozitif sayı girildi.".format(eleNeg, elePoz))
            print("Dizinin son hali :", dizi)
        except:
            print("Hata ! {}".format(self.__hataMesaji))

    def AritmetikGeometrikOrt(self):
        print("/" * len(self.__baslik["3"]), self.__baslik["3"], "/" * len(self.__baslik["3"]), sep="\n", end="\n\n")
        try:
            self.__hataMesaji="Bir tam sayı girilmedi !"
            elemSayisi = int(input("Dizinin eleman sayısını giriniz :"))

            if elemSayisi < 0 :
                self.__hataMesaji="Dizinin eleman sayısı negatif olamaz !"
                raise Exception  

            dizi=[]

            for s in range(1,elemSayisi+1):
                dizi.append(int(input("{}. elemanı giriniz :".format(s))))

            artimetik = 0
            geometrik = 1
            for s in range(0,len(dizi)):
                artimetik += dizi[s]
                geometrik *= dizi[s]
            print("Aritmetik ortalama => {}".format((artimetik / elemSayisi)))
            print("Geometrik ortalama => {}".format((geometrik ** (1 / elemSayisi))))
        except:
            print("Hata ! {}".format(self.__hataMesaji))

    def FaktoriyelBulma(self, sayı):
        if sayı == 0:
            return 1
        else:
            return sayı * self.FaktoriyelBulma(sayı-1)

    def PermutasyonBulma(self):
        print("x" * len(self.__baslik["5"]), self.__baslik["5"], "x" * len(self.__baslik["5"]), sep="\n", end="\n\n")
        try:
            self.__hataMesaji="Bir tam sayı girilmedi !"
			
            ne = int(input("P(n,r)'deki n değerini girin :"))
            re = int(input("P(n,r)'deki r değerini girin :"))
			
            if ne < 0 or re < 0:
                self.__hataMesaji="Girilen sayı negatif olamaz !"
                raise Exception		
            if re > ne:
                self.__hataMesaji="Sayılar arasında uyumsuzluk var !"
                raise Exception	                
				
            print("P({},{}) = {}".format(ne,re,self.FaktoriyelBulma(ne)/self.FaktoriyelBulma((ne-re))))
        except:
            print("Hata ! {}".format(self.__hataMesaji))
			
    def KombinasyonBulma(self, ne=0, re=0, Kendisi=True):
        if Kendisi:
            try:
                self.__hataMesaji="Bir tam sayı girilmedi !"
				
                print(":" * len(self.__baslik["6"]), self.__baslik["6"], ":" * len(self.__baslik["6"]), sep="\n", end="\n\n")
                ne = int(input("C(n,r)'deki n değerini girin :"))
                re = int(input("C(n,r)'deki r değerini girin :"))

                if ne < 0 or re < 0:
                    self.__hataMesaji="Girilen sayı negatif olamaz !"
                    raise Exception

                if re > ne:
                    self.__hataMesaji="Sayılar arasında uyumsuzluk var !"
                    raise Exception	 

                print("C({},{}) = {}".format(ne,re,self.FaktoriyelBulma(ne)/(self.FaktoriyelBulma((ne-re))*self.FaktoriyelBulma(re))))
				
            except Exception:
                    print("Hata ! {}".format(self.__hataMesaji))
        else:
            return self.FaktoriyelBulma(ne)/(self.FaktoriyelBulma((ne-re))*self.FaktoriyelBulma(re))

    def BinomAcilimi(self):
        print("$" * len(self.__baslik["7"]), self.__baslik["7"], "$" * len(self.__baslik["7"]), sep="\n", end="\n\n")
		
        try:
            self.__hataMesaji="Bir tam sayı girilmedi !"
			
            ne = int(input("(x+y)^n'deki n değerini girin:"))
            xe = int(input("(x+y)^n'deki x değerini girin:"))
            ye = int(input("(x+y)^n'deki y değerini girin:"))

            if ne < 0 or xe < 0 or ye < 0:
                self.__hataMesaji="Girilen sayı negatif olamaz !"
                raise Exception
            
            self.__hataMesaji="Uygun sayılar girilmedi !"
            gosterim = "({}+{})^{} =".format(xe,ye,ne)
            sonuc = 0
            for s in range(0,ne+1):
                gosterim += " {}*({}^{})*({}^{}) +".format(self.KombinasyonBulma(ne, s, False), xe, (ne-s),ye,s)
                sonuc += (self.KombinasyonBulma(ne,s,False)*(xe**(ne-s))*(ye**s))

            print(gosterim.rstrip("+"),"=",sonuc)
        except:
            print("Hata ! {}".format(self.__hataMesaji))

########################################################################################################################

if __name__ == "__main__":
	mtmtk = Matematik()




