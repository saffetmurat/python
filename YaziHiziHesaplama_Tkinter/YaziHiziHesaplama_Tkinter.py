from tkinter import *
from tkinter.messagebox import *
import os
import random
from datetime import datetime

class YaziHiziHesaplama():
    __icerik = []#asıl metni tutuyor.
    __zamanBilgileri = [0, 0, 0]#3 elemanlı olacak;
                        #ilk eleman zamanın başlangıç tarihini
                        #ikinci eleman zamanın bitiş tarihini
                        #üçüncü eleman toplam süreyi tutacak

    def __init__(self, adres = os.getcwd() + os.sep + "yaziHiziHesaplamaMetni.txt"):
        self.adres = adres
    
    def dosyaAc(self, kip = "r"):
        if os.path.exists(self.adres):
            dosya = open(self.adres, kip)
            return dosya
        else:
            showerror("Hata", "Metinlerin bulunduğu dosya bulunamıyor.\nBu yüzden uygulama kapatılıyor.")
            raise Exception

    def metinAl(self):
        dsy = self.dosyaAc()
        metin = dsy.read().replace("\n","")

        cumle =""
        self.__icerik = []
        for harf in metin:
            if not harf in ['.', '!', '?']:#Bu karakterlere göre parçalanıyor.
                cumle += harf
            else:
                cumle += harf
                self.__icerik.append(cumle)
                cumle = ""
        dsy.close()

    def metinDogruluguHesaplama(self):
        metinYazilan = self.girilenMetin.get("1.0", END)
        metinAsil = self.gosterilenMetin.get("1.0", END)
        
        yazilanKelimeler = metinYazilan.strip(" ").strip("\n").split(" ");
        asilKelimeler = metinAsil.strip(" ").strip("\n").split(" ");

        yanlisKelimeIndeksi = []

        buyukListe = yazilanKelimeler.copy()
        if len(buyukListe) < len(asilKelimeler):
            buyukListe = []
            buyukListe = asilKelimeler.copy()
        
        for i in range(len(buyukListe)):#yanlis olan kelimelerin indeksleri bulunur.
            try:
                if yazilanKelimeler[i] != asilKelimeler[i]:
                    yanlisKelimeIndeksi.append(i)
            except:
                yanlisKelimeIndeksi.append(i)               

        try:
            showinfo("Bilgilendirme", "Yazma için ayırdığınız süre toplamda " + str(round(self.__zamanBilgileri[2], 2)) + " saniyedir.")
            showinfo("Bilgilendirme", "1 saniyede ortalama {} kelime yazabildiniz.".format(round(len(yazilanKelimeler)/(self.__zamanBilgileri[2]),2)))
            showinfo("Bilgilendirme", "Yazının doğruluk oranı yüzde {}".format(100 - round(len(yanlisKelimeIndeksi)/len(asilKelimeler)*100),2))
        except:
            showerror("Hata", "Bir hata oluştu. Bu yüzden bilgilendirme yapılamıyor.")
        finally:
            showinfo("Bilgilendirme","Açılacak olan pencerede yazdıklarınız arasından yanlış sırada ve yazımda olanlar ile eksik/fazla olan kısımlar kırmızı renk ile gösterilmektedir.")

        self.sonucPenceresi = Tk()
        self.sonucPenceresi.title("Yazım Sonuç Ekranı")
        self.sonucPenceresi.geometry("600x300+100+100")
        self.sonucPenceresi.resizable(width=FALSE, height=FALSE)

        metin = Text(self.sonucPenceresi, width = 73, height= 18)
        metin.delete("1.0", END)

        for indeks in range(len(buyukListe)):
            if indeks in yanlisKelimeIndeksi:
                karakterSayisi = len(metin.get("1.0", END)) - 1
                metin.insert(END, buyukListe[indeks] + " ")
                baslangic = "1.{}".format(karakterSayisi)
                bitis = "1.{}".format(karakterSayisi + len(buyukListe[indeks]))
                metin.tag_add("yanlis", baslangic, bitis)
                
                metin.tag_config("yanlis", background="white", foreground="red")
            else:
                metin.insert(END, buyukListe[indeks] + " ")

        metin.config(state = DISABLED)
        metin.place(relx = 0.01, rely = 0.01)

        self.sonucPenceresi.mainloop()

    def cikis(self, durum = True):
        try:
            if durum:#if'e girerse tüm pencereler kapatılacak demektir.
                self.pencere.destroy()
            self.sonucPenceresi.destroy()                
        except:#Bu kısıma girerse self.sonucPenceresi.destroy() hata verdi demektir.
            pass

    def menuPasifYap(self, *args):#self.menuIslemler için
        for nesne in args:
            self.menuIslemler.entryconfig(nesne, state="disabled")

    def menuAktifYap(self, *args):#self.menuIslemler için
        for nesne in args:
            self.menuIslemler.entryconfig(nesne, state="normal")

    def pencereYap(self):

        self.pencere = Tk()
        self.pencere.title("Yazı Hızını Hesaplama Programı")
        self.pencere.geometry("600x600+100+100")
        self.pencere.resizable(width=FALSE, height=FALSE)

        self.pencere.protocol('WM_DELETE_WINDOW', self.cikis)

        menu1 = Menu(self.pencere)
        self.pencere.config(menu=menu1)

        self.menuIslemler = Menu(menu1, tearoff = 0)
        menu1.add_cascade(label = "İşlemler", menu=self.menuIslemler)
        self.menuIslemler.add_command(label = "Başla", command = self.basla)
        self.menuIslemler.add_command(label = "Bitir", command = self.bitir)
        self.menuIslemler.add_command(label = "Duraklat", command = self.duraklat)
        self.menuIslemler.add_command(label = "Devam", command = self.devam)
        self.menuIslemler.add_command(label = "Baştan Başla", command = self.bastanBasla)
        self.menuIslemler.add_command(label = "Yeni Bir Tane Aç", command = self.yeniAc)
        
        self.seviye = IntVar()
        menuSeviye = Menu(self.menuIslemler, tearoff = 0)
        self.menuIslemler.add_cascade(label = "Zorluk Seviyesi Seçin", menu = menuSeviye)
        menuSeviye.add_radiobutton(label = "Kolay", value = 0, variable = self.seviye)
        menuSeviye.add_radiobutton(label = "Orta", value = 1, variable = self.seviye)
        menuSeviye.add_radiobutton(label = "Zor", value = 2, variable = self.seviye)
        
        menuAciklamalar = Menu(menu1, tearoff = 0)
        menu1.add_cascade(label = "Açıklamalar", menu = menuAciklamalar)
        menuAciklamalar.add_command(label = "Program Hakkında Açıklamalar", command = self.programAciklamasi)
        menuAciklamalar.add_command(label = "Hakkımda", command = self.hakkimda)

        self.gosterilenMetin = Text(self.pencere, state = DISABLED, width = 73, height= 18)
        self.girilenMetin = Text(self.pencere, state = DISABLED, width = 73, height= 18)

        self.gosterilenMetin.place(relx = 0.01, rely = 0.01)
        self.girilenMetin.place(relx = 0.01, rely = 0.505)

        #başlangıçta pasif olanlar
        self.menuPasifYap("Duraklat", "Devam", "Bitir")

        self.pencere.mainloop()

    def basla(self, durum=True):
        try:
            self.cikis(False)#self.sonucPenceresi aktif ise kapatılır.

            if durum:#if'e girerse Baştan Başla tuşuna basıldı demektir.
                self.metinAl()

                ###Zorluk Seviyesine göre cümle sayısı belirlenir.################
                if self.seviye.get() == 0:#Kolay seçilmiş demektir.
                    cumleSayisi = 2
                elif self.seviye.get() == 1:#Orta seçilmiş demektir.
                    cumleSayisi = len(self.__icerik)//4#Tamsayı bölmesi yapılır.
                else:#Zor seçilmiş demektir.
                    cumleSayisi = len(self.__icerik)
                ###################################################################
                metin = random.sample(self.__icerik, cumleSayisi)
                #sample fonksiyonu sayesinde self.icerik listesinden birbirine benzemeyen cumleSayisi kadar eleman alınır.

                self.gosterilenMetin.config(state = NORMAL)
                self.gosterilenMetin.delete("0.0",END)#İçerik temizlenir.

                self.gosterilenMetin.insert(END, metin[0].lstrip(" "))#ilk cümlenin başında olabilecek boşluk karakteri silinir.
                for indeks in range(1, len(metin)):
                    self.gosterilenMetin.insert(END, metin[indeks])
                self.gosterilenMetin.config(state = DISABLED)

            self.__zamanBilgileri[0] = datetime.now()

            self.girilenMetin.config(state = NORMAL)
            self.girilenMetin.delete("1.0", END)

            self.menuAktifYap("Bitir", "Duraklat")
            self.menuPasifYap("Başla", "Devam")
        
        except Exception:
            self.cikis()       

    def bitir(self):
        self.__zamanBilgileri[1] = datetime.now()
        self.__zamanBilgileri[2] += (self.__zamanBilgileri[1] - self.__zamanBilgileri[0]).total_seconds()

        self.menuAktifYap("Zorluk Seviyesi Seçin", "Başla")
        self.menuPasifYap("Duraklat", "Devam", "Bitir")

        self.metinDogruluguHesaplama()     

        self.__zamanBilgileri[2] = 0.0

    def duraklat(self):
        self.__zamanBilgileri[1] = datetime.now()
        self.__zamanBilgileri[2] += (self.__zamanBilgileri[1] - self.__zamanBilgileri[0]).total_seconds()

        self.girilenMetin.config(state = DISABLED)

        self.menuPasifYap("Duraklat")
        self.menuAktifYap("Devam", "Bitir")

    def devam(self):
        self.__zamanBilgileri[0] = datetime.now()

        self.girilenMetin.config(state = NORMAL)

        self.menuPasifYap("Devam")
        self.menuAktifYap("Duraklat", "Bitir")

    def bastanBasla(self):
        if self.gosterilenMetin.get("1.0",END).strip("\n").strip(" ") == "":
            self.basla()
        else:
            self.basla(False)

    def yeniAc(self):
        self.basla()

    def programAciklamasi(self):
        aciklamaMetni = """        Kullanıcının Başla tuşuna basmasıyla birlikte kullanıcıya metin gösterilir.
        Kullanıcı ggösterilen metni alt kutuya yazar. Yazması bittiğinde Bitir tuşuna basar. Ardından kullanıcıya bazı istatistikler gösterilir.
        Bunlar; yazdığı toplam süre (saniye olarak), bir saniyede ortalama yazabildiği kelime sayısı, yazının doğruluk oranı (yüzde olarak).
        Sonra bir pencere açılır. Açılan pencerede kullanıcının yazdıkları arasından yanlış sırada ve yazımda olanlar ile eksik/fazla olan kısımlar kırmızı renk ile gösterilir.

        Duraklat tuşuna basınca program zaman ölçmeyi durdurur. Devam tuşuna basınca tekrardan başlar. Böylece kullanıcı işleme ara verebilir.
        Baştan Başla tuşuna basınca metin aynı kalarak işlemler baştan başlar. 
        Yeni Bir Tane Aç tuşuna basınca yeni bir metinle işlemler baştan başlar.
        Zorluk Seviyesi Seçin -> Kolay/Orta/Zor tuşlarından biri seçilerek zorluk seviyesi belirlenir. Zorluk seviyesi arttıkça kullanıcıya gösterilen cümle sayısı artmaktadır.
        """
        showinfo("Bilgilendirme", aciklamaMetni)

    def hakkimda(self):
        showinfo("Hakkımda","Saffet Murat tarafından yapıldı\n(Created by: Saffet Murat)\n\n{}\n\n{}".format("https://trmsma.wordpress.com","https://github.com/saffetmurat"))

if __name__ == "__main__":
    yhh = YaziHiziHesaplama()
    yhh.pencereYap()