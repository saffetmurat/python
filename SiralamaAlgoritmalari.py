import time

class SiralamaAlgoritmalari():
    __yazilar = {
        "0" : "Sistemde kayıtlı algoritmalar aşağıdadır. Kullanmak istediğinizin sıra numarasını giriniz.\n",
        "1" : "1) Seçerek/Seçmeli Sıralama (Selection Sort)\n",
        "2" : "2) Kabarcık Baloncuk Sıralaması (Bubble Sort)\n"
        }

    def __init__(self):
        self.yontemSec()

    def diziAlma(self):
        liste = []

        print("\nLütfen dizi için eleman giriniz : ")
        print("NOT: Eleman almayı durdurmak için rakam dışı bir karakter giriniz!")

        sayac = 1
        while True:
            try: 
                sayi = int(input("Dizinin {}.elemanını giriniz : ".format(sayac))) 
                liste.append(sayi)
                sayac += 1
            except:
                print("Rakam dışı bir karakter girildiğinden eleman alma işlemi bitirildi.")  
                break 
        return liste    

    def yontemSec(self):
        tercih = input("{}{}{}Tercihiniz : ".format(*self.__yazilar.values()))

        if tercih not in self.__yazilar.keys():
            print("Geçersiz bir tuş girildi. İşlem İPTAL EDİLİYOR.")
        
        else:
            liste = []
            #dizi için eleman alınıyor.
            liste = self.diziAlma()

            #yön seçilecek
            print("\nSıralama hangi yönde olsun?(Sıra numarasını giriniz)")
            yon =  input("1) Büyükten küçüğe doğru\n2) Küçükten büyüğe doğru\nTercihiniz : ")
            
            if yon not in ["1","2"]:
                print("Geçersiz bir tuş girildi. İşlem İPTAL EDİLİYOR.")                
                return False #fonksiyon sonlandırılıyor.

            if tercih == "1":
                self.selectionSort(liste, yon)
            elif tercih == "2":
                self.bubbleSort(liste, yon)
            else:
                pass

    def selectionSort(self, liste, yon):
        if yon == "1":
            for indeks in range(0,len(liste)):
                for indeks1 in range(indeks+1,len(liste)):
                    if liste[indeks] < liste[indeks1]:
                        liste[indeks], liste[indeks1] = liste[indeks1], liste[indeks]

        elif yon == "2":
            for indeks in range(0,len(liste)):
                for indeks1 in range(indeks+1,len(liste)):
                    if liste[indeks] > liste[indeks1]:
                        liste[indeks], liste[indeks1] = liste[indeks1], liste[indeks]
        else: 
            pass

        print("En son elde edilen sıralı liste =>", liste, sep="\n")

    def bubbleSort(self, liste, yon):

        for s in range(0,len(liste)):
            for m in range(0,len(liste)-(s+1)):
                if liste[m] > liste[m+1]:
                    liste[m], liste[m+1] = liste[m+1], liste[m]
        
        if yon == "1":
            liste.reverse()

        print("En son elde edilen sıralı liste =>", liste, sep="\n")  

if __name__ == "__main__":
    SiralamaAlgoritmalari()
    time.sleep(1)


