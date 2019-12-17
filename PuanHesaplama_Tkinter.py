from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

class PuanHesaplama():
    __comboboxListesi = []
    __ekran = []

    def __init__(self):
        pass

    def aciklama(self):
        aciklamaYazisi="""        Matematik, Fen, Türkçe ve Sosyal alanlarından yapılan doğru, yanlış ve boş sayıları esas alınarak bir puan hesaplama yapılmaktadır.
        Her ders için toplam 50 soru var kabul edilmektedir.
        Her soru 1 puan değerindedir. Her dersten aldığın puan, senin o dersteki net sayına eşittir. 
        Her bir ders için net sayısı, hesaplanırken aşağıdaki formül kullanılır:
                net_sayisi = dogru_sayisi - ( yanlis_sayisi / 4 )
        Yani her 4 yanlış, 1 doğruyu götürmektedir.
        Toplam puan 200'dur. Toplam puan, her derste yaptığın netlerin toplamıdır.
        Baraj puanı 100 kabul edilmektedir."""

        showinfo("Bilgilendirme", aciklamaYazisi)

    def hakkimda(self):
        showinfo("Hakkımda","Saffet Murat tarafından yapıldı\n(Created by: Saffet Murat)\n\n{}\n\n{}".format("https://trmsma.wordpress.com","https://github.com/saffetmurat"))

    def ekranKaldirma(self, ekran=""):
        if ekran != "":
            self.__ekran.append(ekran)
        else:
            try:
                self.__ekran[0].destroy()#Her ekrana girişte bir önceki var olan ekran yıkılır.
                self.__ekran = []
                self.__comboboxListesi = []
            except:
                pass
    
    def ortakEkranKisimlari(self, ekran, ekranBaslik=""):
        ekran.title(ekranBaslik)
        ekran.geometry("580x180+100+100")
        ekran.resizable(width = False, height = False)

        menu1 = Menu(ekran)
        ekran.config(menu = menu1)

        menuAciklamalar = Menu(menu1, tearoff = 0)
        menu1.add_cascade(label = "Açıklamalar", menu = menuAciklamalar)
        menuAciklamalar.add_command(label = "Program Hakkında Açıklamalar", command = self.aciklama)
        menuAciklamalar.add_command(label = "Hakkımda", command = self.hakkimda)

    def anaEkranYapma(self):  
        self.ekranKaldirma()#Aktif ekran silinir.
        anaEkran = Tk()
        self.ekranKaldirma(anaEkran)#Aktif ekran algılandı

        self.ortakEkranKisimlari(anaEkran, "Puan Hesaplam Uygulaması - Ana Ekran Penceresi")

        etiketMatematik = Label(anaEkran, text = "Matematik dersindeki doğru sayısını\t\t, yanlış sayısını\t          , boş sayısını\t belirleyiniz.")
        etiketTurkce = Label(anaEkran, text = "Türkçe dersindeki doğru sayısını\t         , yanlış sayısını\t  , boş sayısını\t         belirleyiniz.")
        etiketFen = Label(anaEkran, text = "Fen dersindeki doğru sayısını\t   , yanlış sayısını\t            , boş sayısını\t   belirleyiniz.") 
        etiketSosyal = Label(anaEkran, text = "Sosyal dersindeki doğru sayısını\t        , yanlış sayısını\t , boş sayısını\t       belirleyiniz.")

        for indeks in range(12):
            self.__comboboxListesi.insert(indeks, ttk.Combobox(anaEkran, state = 'readonly', values = [i for i in range(51)], width = 3))
            self.__comboboxListesi[indeks].current(0) 
        
        butonHesapla = Button(anaEkran, text = "Hesaplama Yap", command = self.sonucEkraniYapma)

        etiketMatematik.place(relx = 0.01, rely= 0.05)
        self.__comboboxListesi[0].place(relx = 0.35, rely= 0.05)#Matematik doğru sayısını temsil ediyor.
        self.__comboboxListesi[1].place(relx = 0.57, rely= 0.05)#Matematik yanlış sayısını temsil ediyor.
        self.__comboboxListesi[2].place(relx = 0.768, rely= 0.05)#Matematik boş sayısını temsil ediyor.

        etiketTurkce.place(relx = 0.01, rely= 0.25)
        self.__comboboxListesi[3].place(relx = 0.315, rely= 0.25)#Türkçe doğru sayısını temsil ediyor.
        self.__comboboxListesi[4].place(relx = 0.53, rely= 0.25)#Türkçe yanlış sayısını temsil ediyor
        self.__comboboxListesi[5].place(relx = 0.725, rely= 0.25)#Türkçe boş sayısını temsil ediyor.
        
        etiketFen.place(relx = 0.01, rely= 0.45)
        self.__comboboxListesi[6].place(relx = 0.285, rely= 0.45)#Fen doğru sayısını temsil ediyor.
        self.__comboboxListesi[7].place(relx = 0.5, rely= 0.45)#Fen yanlış sayısını temsil ediyor
        self.__comboboxListesi[8].place(relx = 0.695, rely= 0.45)#Fen boş sayısını temsil ediyor.

        etiketSosyal.place(relx = 0.01, rely= 0.65)
        self.__comboboxListesi[9].place(relx = 0.31, rely= 0.65)#Sosyal doğru sayısını temsil ediyor.
        self.__comboboxListesi[10].place(relx = 0.525, rely= 0.65)#Sosyal yanlış sayısını temsil ediyor
        self.__comboboxListesi[11].place(relx = 0.719, rely= 0.65)#Sosyal boş sayısını temsil ediyor.

        butonHesapla.place(relx = 0.01, rely= 0.82)

        anaEkran.mainloop()

    def hesaplamaYap(self):
        ################ HESAPLAMA KISMI ############################################
        dogru = yanlis = bos = 0
        dersAdi = ""
        islemDurum = True

        netler = []

        for indeks in range(0,12,3):
            dogru = int(self.__comboboxListesi[indeks].get())
            yanlis = int(self.__comboboxListesi[indeks + 1].get())
            bos = int(self.__comboboxListesi[indeks + 2].get())

            netler.append((dogru - (yanlis / 4)))#4 yanlis bir doğruyu götürecek

            if (dogru + yanlis + bos) > 50 or (dogru + yanlis + bos) < 50:
                islemDurum = False
                if indeks == 0:
                    dersAdi = "Matematik"
                elif indeks == 3:
                    dersAdi = "Türkçe"
                elif indeks == 6:
                    dersAdi = "Fen" 
                elif indeks == 9:
                    dersAdi = "Sosyal" 

                showwarning("Uyarı", "{} dersindeki doğru, yanlış ve boş soruların toplamı, toplam soru sayısı olan 50'ye eşit değildir.\nBunu düzeltiniz.".format(dersAdi))
        
        if islemDurum:
            return netler
        else:
            return False
        #############################################################################

    def sonucEkraniYapma(self):
        #Sonuc Ekranı Kısmı##########################################################
        netler = self.hesaplamaYap()
        if netler == False:
            return False

        self.ekranKaldirma()#Aktif ekran silinir.

        sonucEkrani = Tk()
        sonucEkrani.protocol('WM_DELETE_WINDOW', self.anaEkranYapma)

        self.ekranKaldirma(sonucEkrani)

        self.ortakEkranKisimlari(sonucEkrani, "Puan Hesaplam Uygulaması - Sonuç Penceresi")
        
        toplamPuan = netler[0] + netler[1] + netler[2] + netler[3]

        etiketMatematik = Label(sonucEkrani, text = "Matematik dersindeki Net Sayısı => {}".format(netler[0]), font = "Times 12")
        etiketTurkce = Label(sonucEkrani, text = "Türkçe dersindeki Net Sayısı => {}".format(netler[1]), font = "Times 12")
        etiketFen = Label(sonucEkrani, text = "Fen dersindeki Net Sayısı => {}".format(netler[2]), font = "Times 12")
        etiketSosyal = Label(sonucEkrani, text = "Sosyal dersindeki Net Sayısı => {}".format(netler[3]), font = "Times 12")
        etiketToplamPuan = Label(sonucEkrani, text = "Elde ettiği Toplam Puan => {}".format(toplamPuan), font = "Times 12")
        
        ###############################################################################
        yazilar = self.degerlendirme(netler, toplamPuan)

        yorumlarText = Text(sonucEkrani, width = 35, height = 10)
        yorumlarText.insert("0.0","Yorumlar =>\n")

        for indeks in range(len(yazilar)):
            yorumlarText.insert(END, yazilar[indeks])

        yorumlarText.config(state = DISABLED)

        yorumlarText.tag_add("yorumlar", "1.0", "1.11")
        yorumlarText.tag_config("yorumlar", background="white", foreground="red")

        yorumlarText.tag_add("genelYorumlar", "10.0", "10.34")
        yorumlarText.tag_config("genelYorumlar", background="white", foreground="red")

        etiketMatematik.place(relx=0.01,rely=0.03)
        etiketTurkce.place(relx=0.01,rely=0.23)
        etiketFen.place(relx=0.01,rely=0.43)
        etiketSosyal.place(relx=0.01,rely=0.63)
        etiketToplamPuan.place(relx=0.01,rely=0.83)

        yorumlarText.place(relx=0.5,rely=0.03)

        sonucEkrani.mainloop()

        ###############################################################################

    def degerlendirme(self, netler, toplamPuan):
        yazilar = []
        dersAdlari = ["Matematik", "Türkçe", "Fen", "Sosyal"]

        for indeks in range(len(netler)):
            if netler[indeks]==50:
                yazilar.append("{} dersinde tam bir başarı yakaladın. TEBRİKLER! :)\n\n".format(dersAdlari[indeks]))
            elif netler[indeks] >= 40:
                yazilar.append("{} dersinde başarılı sayılırsın\n\n".format(dersAdlari[indeks]))
            elif netler[indeks] > 25:
                yazilar.append("{} dersinde başarılı sayılırsın ancak biraz daha çalışmalısın.\n\n".format(dersAdlari[indeks]))
            elif netler[indeks] > 15:
                yazilar.append("{} dersinde başarılı DEĞİLSİN. Biraz daha çalışmalısın.\n\n".format(dersAdlari[indeks]))
            else:
                yazilar.append("{} dersinde çok kötüsün. ÇOK ÇALIŞMAN GEREKİYOR\n\n".format(dersAdlari[indeks]))

        yazilar.append("SINAVIN TAMAMINI DEĞERLENDİRİRSEK;\n")
        if toplamPuan == 200:
            yazilar.append("TEBRİKLER! Tam Puan Aldın :)\n\n")
        elif toplamPuan > 150:
            yazilar.append("Sınavdan başarılı sayılırsın.\n\n")
        elif toplamPuan > 100:
            yazilar.append("100 olan baraj puanını geçmeyi başarabildin. Ama daha çok çalışmalısın.\n\n")
        else:
            yazilar.append("100 olan baraj puanını geçemedin. ÇOK ÇALIŞMAN GEREK!\n\n")

        return yazilar

if __name__ == "__main__":
    ph = PuanHesaplama()
    ph.anaEkranYapma()