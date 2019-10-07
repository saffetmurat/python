
class SinifDersDurumu():

    __hataMesaji = ""

    def __init__(self):
        self.baslangic()

    def baslangic(self):
        baslik = "Sınıftaki öğrencilerin notunu alıp her öğrencinin durumunu belirleme"
        print("*" * len(baslik), baslik, "*" * len(baslik), sep="\n", end="\n\n")

        try:
            self.__hataMesaji = "Bir tam sayı girilmedi !"
            sayiOgren=int(input("Toplam Öğrenci sayısını giriniz :"))
            sayiDers=int(input("Toplam Ders sayısını giriniz :"))
            
            if sayiOgren < 0 or sayiDers < 0:
                self.__hataMesaji = "Negatif bir sayı girdiniz ! Pozitif bir tam sayı girilmeliydi !"
                raise Exception

            ders=[]
            dersler=[]
            dersler_ortlama=[]
            ort=0
            for d in range(1,sayiDers+1):
                for g in range(1,sayiOgren+1):
                    ders_notu = int(input("{}. ders için {}. öğrencini notunu giriniz :".format(d,g)))

                    while ders_notu < 0 or ders_notu > 100:
                        print("HATA ! Girilen ders notu 0'dan küçük 100'den büyük olamaz.")
                        ders_notu = int(input("{}. ders için {}. öğrencini notunu giriniz :".format(d,g)))

                    ort += ders_notu
                    ders.append(ders_notu)
                print("")
                dersler.append(ders)
                dersler_ortlama.append((ort/sayiOgren))
                ders=[]
                ort=0

            print("Öğrencilerin Durumları =>")
            for d in range(0,sayiDers):
                print("{}. dersin not ortalaması : {}".format(d+1,dersler_ortlama[d]))
                for g in range(0,sayiOgren):
                    if dersler[d][g] >= dersler_ortlama[d]:
                        print("{}. öğrenci {}. dersten GEÇTİ.".format(g+1,d+1))
                    else:
                        print("{}. öğrenci {}. dersten KALDI.".format(g+1,d+1))
                print("")
        except:
            print("HATA ! {}".format(self.__hataMesaji))

if __name__ == "__main__":
    sdd = SinifDersDurumu()
    input("Programı Kapatmak için bir tuşa basın") #kullanıcı klavyeden bir tuşa basana kadar ekranı açık tutmak için