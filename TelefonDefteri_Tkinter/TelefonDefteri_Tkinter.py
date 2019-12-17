from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

import os

class TelefonDefteri():
    __rehberBilgisi = []
    __ekran = []
    __tasinanNesneler = []
    __secimYonTercih = 0
    __secimTurTercih = 0

    def __init__(self, adres=os.getcwd() + os.sep + "TelefonDefteri.csv"):
        self.adres = adres

    def dosyaAc(self, kip="r"):
        if os.path.exists(self.adres):
            dosya = open(self.adres, kip)
            return dosya
        else:
            showerror("Hata","Belirtilen adreste veri kaynağı bulunamıyor.")
            raise Exception

    def rehberBilgisiAlma(self):
        ############ Rehber Bilgisi Alınır ####################################
        dsy = self.dosyaAc("r")
        self.__rehberBilgisi = dsy.readlines()
        dsy.close()

    def menuYapma(self, ekran):
        try:
            self.secimYon = IntVar()
            self.secimTur = IntVar()
            self.secimYon.set(self.__secimYonTercih)
            self.secimTur.set(self.__secimTurTercih)

            menu1 = Menu(ekran)
            ekran.config(menu=menu1)

            menuSecenekler = Menu(menu1,tearoff = 0)
            menu1.add_cascade(label = "Seçenekler", menu = menuSecenekler)#menuSecenekleri menu1'e bağlandı.
            menuSecenekler.add_command(label = "Hepsini Listele", command=self.hepsiniListeleEkrani)
            menuSecenekler.add_command(label = "Ara", command=self.araEkrani)
            menuSecenekler.add_command(label = "Yeni Kişi Ekle", command=self.ekleEkrani)
            menuSecenekler.add_command(label = "Kişi Sil", command=self.silEkrani)
            menuSecenekler.add_command(label = "Düzenle", command=self.duzenEkrani)
            menuSecenekler.add_command(label = "Ekranı Temizle", command=self.ekraniTemizle)

            menuSayi = Menu(menuSecenekler,tearoff = 0)
            menuSecenekler.add_cascade(label = "Kayıt Sayısı", menu = menuSayi)#menuSayi menuSecenekleri'ne bağlandı.
            menuSayi.add_command(label = "Toplam Kayıt Sayısı", command=self.toplamKayitSayisi)
            menuSayi.add_command(label = "Görünen Kayıt Sayısı", command=self.gorunenKayitSayisi)       

            menuSiralama = Menu(menu1, tearoff = 0)
            menu1.add_cascade(label = "Sıralamayı Ayarla", menu = menuSiralama)#menuSiralama menu1'e bağlandı.

            menuSiralamaYon = Menu(menuSiralama, tearoff = 0)#menuSiralamYon menuSiralama'ya bağlandı.
            menuSiralama.add_cascade(label = "Sıralama Yönü Seç", menu = menuSiralamaYon)#menuSiralamYon menuSiralama'ya bağlandı.
            menuSiralamaYon.add_radiobutton(label = "Küçükten Büyüğe Doğru", value=0, variable=self.secimYon, command=self.secim)
            menuSiralamaYon.add_radiobutton(label = "Büyükten Küçüğe Doğru", value=1, variable=self.secimYon, command=self.secim)

            menuSiralamaTur = Menu(menuSiralama, tearoff = 0)#menuSiralamTur menuSiralama'ya bağlandı.
            menuSiralama.add_cascade(label = "Sıralama Türü Seç", menu = menuSiralamaTur)
            menuSiralamaTur.add_radiobutton(label = "Ad Soyada Göre Sırala", value=0, variable=self.secimTur, command=self.secim)
            menuSiralamaTur.add_radiobutton(label = "Telefon Numarasına Göre Sırala", value=1, variable=self.secimTur, command=self.secim)        
            menuSiralamaTur.add_radiobutton(label = "E-Postaya Göre Sırala", value=2, variable=self.secimTur, command=self.secim)

            menuAciklamalar = Menu(menu1, tearoff = 0)
            menu1.add_cascade(label = "Açıklamalar", menu = menuAciklamalar)#menuAciklamalar menu1'e bağlandı.
            menuAciklamalar.add_command(label = "Hakkımda", command=self.hakkimda)
        except:
            pass

    def gorunenKayitSayisi(self):
        showinfo("Bilgilendirme", "Ekranda toplam {} tane kayıt bulunmaktadır.".format(len(self.__rehberBilgisi)))

    def toplamKayitSayisi(self):
        try:
            dsy = self.dosyaAc("r")
            showinfo("Bilgilendirme", "Sistemde toplam {} tane kayıt bulunmaktadır.".format(len(dsy.readlines())))
            dsy.close()
        except:
            pass
        
    def secim(self):
        try:
            self.__secimTurTercih = self.secimTur.get()
            self.__secimYonTercih = self.secimYon.get()
            self.rehberAgaciniGuncelleme(3)#hepsiniListeleEkrani dışındaki tüm ekranlarda 3.indeksteki nesne treeview olduğu için parametre olarak 3 veriliyor.
        except IndexError:
            self.rehberAgaciniGuncelleme(0)#hepsiniListeleEkrani'ndea treeview 0. indekste olduğundan 
        except:
            pass

    def ekraniTemizle(self):#Ekrandaki Entrylerin içeriği temizleniyor.
        for nesne in self.__tasinanNesneler:
            if str(type(nesne)) == "<class 'tkinter.Entry'>":#gelen nesne Entry ise
                if nesne["state"] == DISABLED:
                    nesne.config(state = NORMAL)
                    nesne.delete(0,END)
                    nesne.config(state = DISABLED)
                else:
                    nesne.delete(0,END)
            elif str(type(nesne)) == "<class 'tkinter.ttk.Treeview'>":#gelen nesne treeview ise
                self.__rehberBilgisi = []
                self.rehberBilgisiAlma()
                indeks = self.__tasinanNesneler.index(nesne)
                self.rehberAgaciniGuncelleme(indeks)
            elif str(type(nesne)) == "<class 'int'>":#durum değişkeninin değeri 0'a çekiliyor.
               indeks = self.__tasinanNesneler.index(nesne)
               self.__tasinanNesneler[indeks] = 0

    def scrollVeTreeYapma(self, ekran, agacYukseklik=21, agacGenislik=169):
        self.rehberBilgisiAlma()

        #scrollBar tanımlanıyor.
        dikeyScrollBar = Scrollbar(ekran, orient="vertical")
        yatayScrollBar = Scrollbar(ekran, orient="horizontal")

        rehberAgaci = ttk.Treeview(ekran, show="headings", height=agacYukseklik, yscrollcommand = dikeyScrollBar.set, xscrollcommand = yatayScrollBar.set)

        dikeyScrollBar["command"] = rehberAgaci.yview
        yatayScrollBar["command"] = rehberAgaci.xview
        ###########################################################################

        rehberAgaci['columns'] = ('adSoyad', 'telefonNumarasi', 'ePosta')

        rehberAgaci.column('adSoyad', width=agacGenislik, anchor='center')
        rehberAgaci.heading('adSoyad', text='Ad Soyad')

        rehberAgaci.column('telefonNumarasi', width=agacGenislik, anchor='center')
        rehberAgaci.heading('telefonNumarasi', text='Telefon Numarası')

        rehberAgaci.column('ePosta', width=agacGenislik, anchor='center')
        rehberAgaci.heading('ePosta', text='E-Posta Adresi')

        self.rehberAgacinaVeriEkleme(rehberAgaci)

        return dikeyScrollBar, yatayScrollBar, rehberAgaci

    def rehberAgacinaVeriEkleme(self, rehberAgaci):
        #####################################################################################################
        ############## VERİYİ SIRALAMA KISMI ################################################################
        buyuktenKucugeSiralama=True

        if self.__secimYonTercih == 0:
            buyuktenKucugeSiralama=False
        else:
            buyuktenKucugeSiralama=True
        
        if self.__secimTurTercih == 0:
            indeks0 = 0# ad soyadı temsil edecek
            indeks1 = 1# telefon numarasını temsil edecek
            indeks2 = 2# epostayı temsil edecek
           
        elif self.__secimTurTercih == 1:
            indeks0 = 1# telefon numarasını temsil edecek
            indeks1 = 0# ad soyadı temsil edecek
            indeks2 = 2# epostayı temsil edecek

        else:#self.__secimTurTercih == 2:
            indeks0 = 2# epostayı temsil edecek
            indeks1 = 0# ad soyadı temsil edecek
            indeks2 = 1# telefon numarasını temsil edecek

        #Sıralama için bir sözlük oluşturulacak
        sozluk = {}
        degerler = []
        for rehber in self.__rehberBilgisi:
            degerler.append(str(rehber.split(";")[indeks1].strip("\n")))
            degerler.append(str(rehber.split(";")[indeks2].strip("\n")))
            sozluk[str(rehber.split(";")[indeks0].strip("\n"))] = degerler
            degerler = []

        sozlukSiraliAnahtarListesi = sorted(sozluk, reverse=buyuktenKucugeSiralama)
        ##################################################################################################
        ############## VERİ EKLEME KISMI #################################################################
        #Aşağıdaki yapıda veri eklenecektir.
        #rehberAgaci.insert('', 'end', text='rehberIdsi', values=('adSoyad, telefonNumarasi, ePosta'))
        for anahtar in sozlukSiraliAnahtarListesi:

            if self.__secimTurTercih == 0:
                rehberAgaci.insert('', 'end', text='rehberIdsi', values=(anahtar, sozluk[anahtar][0], sozluk[anahtar][1]))

            elif self.__secimTurTercih == 1:
                rehberAgaci.insert('', 'end', text='rehberIdsi', values=(sozluk[anahtar][0], anahtar, sozluk[anahtar][1]))

            else:
                rehberAgaci.insert('', 'end', text='rehberIdsi', values=(sozluk[anahtar][0], sozluk[anahtar][1], anahtar))
        ##################################################################################################

    def hakkimda(self):
        showinfo("Hakkımda","Saffet Murat tarafından yapıldı\n(Created by: Saffet Murat)\n\n{}\n\n{}".format("https://trmsma.wordpress.com","https://github.com/saffetmurat"))

    def ekranListesiIslemi(self, ekran = ""):
        if ekran != "":
            self.__ekran.append(ekran)
        else:
            try:
                self.__ekran[0].destroy()#Her ekrana girişte bir önceki var olan ekran yıkılır.
                self.__ekran = []
                self.__tasinanNesneler = []#Buraya gelindiğine göre yeni ekrandaki nesneleri taşıması için listenin içeriği temizleniyor.
            except:
                pass
    
    def comboDegisimIslemi(self, event):
        tur = self.__tasinanNesneler[0].get()
        self.__tasinanNesneler[1].config(text = "<= Aranacak {} giriniz.".format(tur))

    def rehberAgaciniGuncelleme(self, nesneIndeksi):
        ############## TREEVİEW'DE VERİ GUNCELLEME KISMI #################################################################
        #Aşağıdaki yapıda veri eklenecektir.
        #rehberAgaci.insert('', 'end', text='rehberIdsi', values=('adSoyad, telefonNumarasi, ePosta'))

        for dugum in self.__tasinanNesneler[nesneIndeksi].get_children(""):#Bu döngü ile treeview boşaltılıyor.
            self.__tasinanNesneler[nesneIndeksi].delete(dugum)

        self.rehberAgacinaVeriEkleme(self.__tasinanNesneler[nesneIndeksi])
        ###################################################################################################################

    def ortakEkranKisimlari(self, baslik, agacYukseklik=21, agacGenislik=169):
        self.ekranListesiIslemi()
        
        ekran = Tk()
        ekran.title(baslik)
        ekran.geometry("550x500+50+50")
        ekran.resizable(width=FALSE, height=FALSE)
        
        self.ekranListesiIslemi(ekran)

        self.menuYapma(ekran)

        dikeyScrollBar, yatayScrollBar, rehberAgaci = self.scrollVeTreeYapma(ekran, agacYukseklik, agacGenislik)

        return ekran, dikeyScrollBar, yatayScrollBar, rehberAgaci

    def tasinanNesnelerDoldur(self, *args):
        for nesne in args:
            self.__tasinanNesneler.append(nesne)

    def hepsiniListeleEkrani(self):
        try:
            anaEkran, dikeyScrollBar, yatayScrollBar, rehberAgaci = self.ortakEkranKisimlari("Telefon Defteri")
                       
            self.tasinanNesnelerDoldur(rehberAgaci)           

            rehberAgaci.place(relx=0.01, rely=0.05)
            dikeyScrollBar.place(relx=0.95, rely=0.05, relheight=0.9)
            yatayScrollBar.place(relx=0.01, rely=0.95, relwidth=0.939)

            anaEkran.mainloop()
        except:
            pass

    def araEkrani(self):
        try:

            anaEkran, dikeyScrollBar, yatayScrollBar, rehberAgaci = self.ortakEkranKisimlari("Telefon Defteri-Arama Kısmı", 18)
           
            aramaTuruLabel = Label(anaEkran, text = "Arama şeklini seçiniz =>")
            aramaTuruCombo = ttk.Combobox(anaEkran, state = 'readonly', values = ["Ad Soyad", "Telefon Numarası", "E-Posta"], width=17)
            aramaTuruCombo.current(0)

            aranacakKelimeLabel = Label(anaEkran, text = "<= Aranacak Adı Soyad giriniz.")
            aranacakKelimeEntry = Entry(anaEkran)

            araButton = Button(anaEkran, text = "Ara", font="Times 13", bg = "orange", width=22, command = self.ara)

            aramaTuruCombo.bind("<<ComboboxSelected>>", self.comboDegisimIslemi)
            
            self.tasinanNesnelerDoldur(aramaTuruCombo, aranacakKelimeLabel, aranacakKelimeEntry, rehberAgaci)

            aramaTuruLabel.place(relx=0.01, rely=0.02)
            aramaTuruCombo.place(relx=0.28, rely=0.02)

            aranacakKelimeEntry.place(relx=0.01, rely=0.09)
            aranacakKelimeLabel.place(relx=0.28, rely=0.09)

            araButton.place(relx=0.57, rely=0.02)


            rehberAgaci.place(relx=0.01, rely=0.18)
            dikeyScrollBar.place(relx=0.95, rely=0.18, relheight=0.77)
            yatayScrollBar.place(relx=0.01, rely=0.96, relwidth=0.939)
            
            anaEkran.mainloop()
        except:
            pass

    def ara(self):
        aranacakTur = self.__tasinanNesneler[0].get()#self.__tasinanNesneler.append(aramaTuruCombo)
        self.__rehberBilgisi = []

        aranacakKelime = self.__tasinanNesneler[2].get()
        dsy = self.dosyaAc()
        icerikler = dsy.readlines()

        if aranacakTur == "Ad Soyad":
            for icerik in icerikler:
                if aranacakKelime in icerik.split(";")[0].strip("\n"):# icerik.split(";")[0].strip("\n") ile her satırdaki ad alınır.
                    self.__rehberBilgisi.append(icerik)
           
        elif aranacakTur == "Telefon Numarası":
            if aranacakKelime.isdigit() or aranacakKelime == "":
                for icerik in icerikler:
                    if aranacakKelime in icerik.split(";")[1].strip("\n"):# icerik.split(";")[1].strip("\n") ile her satırdaki telefon numarası alınır.
                        self.__rehberBilgisi.append(icerik)
            else:
                showerror("Hata","Telefon numarası tam sayılardan oluşmalıdır.")
        else: #aranacakTur == "E-Posta":            
            for icerik in icerikler:
                if aranacakKelime in icerik.split(";")[2].strip("\n"):# icerik.split(";")[2].strip("\n") ile her satırdaki eposta alınır.
                    self.__rehberBilgisi.append(icerik)

        self.rehberAgaciniGuncelleme(3)
        
        dsy.close()

    def ekleEkrani(self):
        try:

            anaEkran, dikeyScrollBar, yatayScrollBar, rehberAgaci = self.ortakEkranKisimlari("Telefon Defteri-Yeni Kişi Ekleme Kısmı", 18)

            adSoyadLabel = Label(anaEkran, text = "Ad Soyad giriniz.")
            adSoyadEntry = Entry(anaEkran)

            telefonNumarasiLabel = Label(anaEkran, text = "Telefon Numarası giriniz.")
            telefonNumarasiEntry = Entry(anaEkran)

            epostaLabel = Label(anaEkran, text = "E-Posta giriniz")
            epostaEntry = Entry(anaEkran)
            

            ekleButton = Button(anaEkran, text = "Ekle", font="Times 13", fg="white", bg = "gray64", width=22, command = self.ekle)
            
            self.tasinanNesnelerDoldur(adSoyadEntry, telefonNumarasiEntry, epostaEntry, rehberAgaci)

            adSoyadLabel.place(relx=0.01, rely=0.02)
            adSoyadEntry.place(relx=0.3, rely=0.01)

            telefonNumarasiLabel.place(relx=0.01, rely=0.075)
            telefonNumarasiEntry.place(relx=0.3, rely=0.065)

            epostaLabel.place(relx=0.01, rely=0.135)
            epostaEntry.place(relx=0.3, rely=0.125)
            
            ekleButton.place(relx=0.57, rely=0.05)

            rehberAgaci.place(relx=0.01, rely=0.18)
            dikeyScrollBar.place(relx=0.95, rely=0.18, relheight=0.77)
            yatayScrollBar.place(relx=0.01, rely=0.96, relwidth=0.939)
            
            anaEkran.mainloop()
        except:
            pass

    def kayitKurallari(self, adSoyad, telNum, ePosta):
        if adSoyad == "":
            showwarning("Uyarı", "Lütfen Ad Soyad bilgisini doldurun")
            return False
        elif telNum == "":
            showwarning("Uyarı", "Lütfen Telefon Numarası bilgisini doldurun")   
            return False     
        elif not telNum.isdigit():
            showerror("Hata", "Telefon Numarası Rakamlardan oluşmalıdır.")     
            return False   
        elif telNum[0] == "0":
            showwarning("Uyarı", "Telefon Numarasının başında 0 (sıfır) olmamalıdır.")
            return False
        elif ePosta == "":
            showwarning("Uyarı", "Lütfen E-Posta bilgisini doldurun")
            return False
        elif "@" == ePosta[0]:
            showerror("Hata", "E-Postanın ilk harfi @ işareti ile başlayamaz.")
            return False
        elif not "@" in ePosta:
            showwarning("Uyarı", "E-Posta adresinde @ işareti bulunmalıdır.")   
            return False
        elif not ePosta.endswith(".com"):
            showwarning("Uyarı", "E-Posta adresinin sonunda .com ifadesi bulunmalıdır.")   
            return False
        else:
            return True

    def ekle(self):

        adSoyad = self.__tasinanNesneler[0].get()
        telNum = self.__tasinanNesneler[1].get()
        ePosta = self.__tasinanNesneler[2].get()
       
        if not self.kayitKurallari(adSoyad, telNum, ePosta):
            return False

        dsy = self.dosyaAc("+a")
        dsy.seek(0)#imlec başa getirilir.
        icerikler = dsy.readlines()
        dsy.seek(0)#imlec başa getirilir.

        for icerik in icerikler:
            icerikAS = icerik.split(";")[0].strip("\n")
            icerikTN = icerik.split(";")[1].strip("\n")
            icerikEP = icerik.split(";")[2].strip("\n")

            if adSoyad == icerikAS:
                showwarning("Uyarı", "Girilen => {} <= adı ve soyadına sahip bir kayıt bulunmaktadır.\nBu yüzden bu işlem yapılamaz!".format(adSoyad))
                showinfo("Bilgilendirme", "Bu kayıt aşağıda verilmektedir.=>\nAd Soyad = {}".format(icerikAS + "\nTelefon Numarası = " + icerikTN + "\nE-Posta = " + icerikEP))
                return False
            elif telNum == icerikTN:
                showwarning("Uyarı", "Girilen => {} <= telefon numarasına sahip bir kayıt bulunmaktadır.\nBu yüzden bu işlem yapılamaz!".format(telNum))
                showinfo("Bilgilendirme", "Bu kayıt aşağıda verilmektedir.=>\nAd Soyad = {}".format(icerikAS + "\nTelefon Numarası = " + icerikTN + "\nE-Posta = " + icerikEP))
                return False
            elif ePosta == icerikEP:
                showwarning("Uyarı", "Girilen => {} <= e-posta adresine sahip bir kayıt bulunmaktadır.\nBu yüzden bu işlem yapılamaz!".format(ePosta))
                showinfo("Bilgilendirme", "Bu kayıt aşağıda verilmektedir.=>\nAd Soyad = {}".format(icerikAS + "\nTelefon Numarası = " + icerikTN + "\nE-Posta = " + icerikEP))
                return False 

        icerikler.append(adSoyad+";"+telNum+";"+ePosta+"\n")

        dsy.truncate()#dosyanın yapısı bozulmadan içeriği siliniyor.
        
        dsy.writelines(icerikler)
        dsy.close()
        
        self.__rehberBilgisi = []

        self.rehberBilgisiAlma()
        self.rehberAgaciniGuncelleme(3)

    def silEkrani(self):
        try:

            anaEkran, dikeyScrollBar, yatayScrollBar, rehberAgaci = self.ortakEkranKisimlari("Telefon Defteri-Kişi Silme Kısmı", 17)


            aramaTuruLabel = Label(anaEkran, text = "Arama şeklini seçiniz =>")
            aramaTuruCombo = ttk.Combobox(anaEkran, state = 'readonly', values = ["Ad Soyad", "Telefon Numarası", "E-Posta"], width=17)
            aramaTuruCombo.current(0)

            aranacakKelimeLabel = Label(anaEkran, text = "<= Aranacak Adı Soyad giriniz.")
            aranacakKelimeEntry = Entry(anaEkran)

            araButton = Button(anaEkran, text = "Ara", font="Times 13", bg = "orange", width=16, command = self.ara)
            
            adSoyadEntry = Entry(anaEkran, state=DISABLED)
            telefonNumarasiEntry =Entry(anaEkran, state=DISABLED)
            ePostaEntry = Entry(anaEkran, state=DISABLED)

            silButton = Button(anaEkran, text = "Kişiyi Sil", font = "Times 12", width = 11, bg = "gray77", fg = "black", command = self.sil)

            durum = 0#durum sıfırsa rehberAgacından bir seçim yapılmamış demektir.
            self.tasinanNesnelerDoldur(aramaTuruCombo, aranacakKelimeLabel, aranacakKelimeEntry, rehberAgaci, adSoyadEntry, telefonNumarasiEntry, ePostaEntry, durum)

            aramaTuruCombo.bind("<<ComboboxSelected>>", self.comboDegisimIslemi)
            rehberAgaci.bind("<<TreeviewSelect>>", self.agactanKisiAktarSilIcin)

            aramaTuruLabel.place(relx=0.01, rely=0.01)
            aramaTuruCombo.place(relx=0.28, rely=0.01)

            aranacakKelimeEntry.place(relx=0.01, rely=0.06)
            aranacakKelimeLabel.place(relx=0.28, rely=0.06)

            araButton.place(relx=0.67, rely=0.01)


            rehberAgaci.place(relx=0.01, rely=0.119)
            dikeyScrollBar.place(relx=0.95, rely=0.119, relheight=0.73)
            yatayScrollBar.place(relx=0.01, rely=0.86, relwidth=0.939)

            adSoyadEntry.place(relx=0.01, rely=0.91)
            telefonNumarasiEntry.place(relx=0.25, rely=0.91)
            ePostaEntry.place(relx=0.49, rely=0.91)

            silButton.place(relx=0.74, rely=0.895)        
            anaEkran.mainloop()
        except:
            pass
    
    def agactanKisiAktarSilIcin(self, event):
        #Entryler pasif haldeyken içeriğine veri yazılamıyor. Bu yüzden aktif hale getiriliyor.

        for indeks in [4,5,6]:#İşleme girecek olan Entry'ler self.__tasinanNesneler llistesinde 4, 5, ve 6. indekserde bulunuyor.
            self.__tasinanNesneler[indeks].config(state = NORMAL)#Entryler aktif hale getiriliyor
            self.__tasinanNesneler[indeks].delete(0, END)#Entrylerin içeriği temizlenir.

        dugum = event.widget.selection()#Seçilen kaydın id'sini verir. ÖR= (I004,)
        #self.__tasinanNesneler[3].item(dugum[0]) ile seçilen kaydın özelliklerine ulaşılır. ÖR= {'text': 'rehberIdsi', 'image': '', 'values': ['Fatih Bey', 5987542160, 'fa98@gmail.com'], 'open': 0, 'tags': ''}
        self.__tasinanNesneler[4].insert(0, self.__tasinanNesneler[3].item(dugum[0])["values"][0])
        self.__tasinanNesneler[5].insert(0, self.__tasinanNesneler[3].item(dugum[0])["values"][1])
        self.__tasinanNesneler[6].insert(0, self.__tasinanNesneler[3].item(dugum[0])["values"][2])     

        self.__tasinanNesneler[7] = 1  

        for indeks in [4,5,6]:#İşleme girecek olan Entry'ler self.__tasinanNesneler llistesinde 4, 5, ve 6. indekserde bulunuyor.
            self.__tasinanNesneler[indeks].config(state = DISABLED)#Entryler tekrardan pasif hale getiriliyor

    def sil(self):
        
        # self.__tasinanNesneler.append(aramaTuruCombo) 0.indeks
        # self.__tasinanNesneler.append(aranacakKelimeLabel) 1.indeks
        # self.__tasinanNesneler.append(aranacakKelimeEntry) 2.indeks
        # self.__tasinanNesneler.append(rehberAgaci) 3.indeks
        # self.__tasinanNesneler.append(adSoyadEntry) 4.indeks
        # self.__tasinanNesneler.append(telefonNumarasiEntry) 5.indeks
        # self.__tasinanNesneler.append(ePostaEntry) 6 .indeks

        if self.__tasinanNesneler[7] == 0:
            showwarning("Uyarı", "Silmek istediğiniz kaydı listeden seçiniz!")
            return False

        adSoyad = self.__tasinanNesneler[4].get()
        telNum = self.__tasinanNesneler[5].get()
        ePosta = self.__tasinanNesneler[6].get()

        dsy = self.dosyaAc("+a")
        dsy.seek(0)
        icerikler = dsy.readlines()

        for icerik in icerikler:
            icerikAS = icerik.split(";")[0].strip("\n")
            icerikTN = icerik.split(";")[1].strip("\n")
            icerikEP = icerik.split(";")[2].strip("\n")

            if adSoyad == icerikAS and telNum == icerikTN and ePosta == icerikEP:
                icerikler.remove(icerik)
                showinfo("Bilgilendirme", "Ad Soyad = {}\nTelefon Numarası = {}\nE-Posta = {}\nolan kayıt başarılı bir şekilde silindi.".format(adSoyad, telNum, ePosta))
                break
        
        dsy.seek(0)
        dsy.truncate()
        dsy.writelines(icerikler)
        dsy.close()

        self.__rehberBilgisi = []

        self.rehberBilgisiAlma()
        self.rehberAgaciniGuncelleme(3)

        self.__tasinanNesneler[7] = 0

    def duzenEkrani(self):
        try:
            anaEkran, dikeyScrollBar, yatayScrollBar, rehberAgaci = self.ortakEkranKisimlari("Telefon Defteri-Kişi Düzenleme Kısmı", 17)

            aramaTuruLabel = Label(anaEkran, text = "Arama şeklini seçiniz =>")
            aramaTuruCombo = ttk.Combobox(anaEkran, state = 'readonly', values = ["Ad Soyad", "Telefon Numarası", "E-Posta"], width=17)
            aramaTuruCombo.current(0)

            aranacakKelimeLabel = Label(anaEkran, text = "<= Aranacak Adı Soyad giriniz.")
            aranacakKelimeEntry = Entry(anaEkran)

            araButton = Button(anaEkran, text = "Ara", font="Times 13", bg = "orange", width=16, command = self.ara)
            
            adSoyadEntry = Entry(anaEkran)
            telefonNumarasiEntry =Entry(anaEkran)
            ePostaEntry = Entry(anaEkran)

            duzenleButton = Button(anaEkran, text = "Kişiyi Düzenle", font = "Times 12", width = 11, bg = "gray77", fg = "black", command = self.duzenle)

            durum = 0#durum sıfırsa rehberAgacından bir seçim yapılmamış demektir.
            self.tasinanNesnelerDoldur(aramaTuruCombo, aranacakKelimeLabel, aranacakKelimeEntry, rehberAgaci, adSoyadEntry, telefonNumarasiEntry, ePostaEntry, durum)

            aramaTuruCombo.bind("<<ComboboxSelected>>", self.comboDegisimIslemi)
            rehberAgaci.bind("<<TreeviewSelect>>", self.agactanKisiAktarDuzenIcin)

            aramaTuruLabel.place(relx=0.01, rely=0.01)
            aramaTuruCombo.place(relx=0.28, rely=0.01)

            aranacakKelimeEntry.place(relx=0.01, rely=0.06)
            aranacakKelimeLabel.place(relx=0.28, rely=0.06)

            araButton.place(relx=0.67, rely=0.01)


            rehberAgaci.place(relx=0.01, rely=0.119)
            dikeyScrollBar.place(relx=0.95, rely=0.119, relheight=0.73)
            yatayScrollBar.place(relx=0.01, rely=0.86, relwidth=0.939)

            adSoyadEntry.place(relx=0.01, rely=0.91)
            telefonNumarasiEntry.place(relx=0.25, rely=0.91)
            ePostaEntry.place(relx=0.49, rely=0.91)

            duzenleButton.place(relx=0.74, rely=0.895)        
            anaEkran.mainloop()
        except:
            pass

    def agactanKisiAktarDuzenIcin(self, event):
        
        for indeks in [4,5,6]:#İşleme girecek olan Entry'ler self.__tasinanNesneler llistesinde 4, 5, ve 6. indekserde bulunuyor.
            self.__tasinanNesneler[indeks].delete(0, END)#Entrylerin içeriği temizlenir.

        dugum = event.widget.selection()#Seçilen kaydın id'sini verir. ÖR= (I004,)
        #self.__tasinanNesneler[3].item(dugum[0]) ile seçilen kaydın özelliklerine ulaşılır. ÖR= {'text': 'rehberIdsi', 'image': '', 'values': ['Fatih Bey', 5987542160, 'fa98@gmail.com'], 'open': 0, 'tags': ''}
        self.__tasinanNesneler[4].insert(0, self.__tasinanNesneler[3].item(dugum[0])["values"][0])
        self.__tasinanNesneler[5].insert(0, self.__tasinanNesneler[3].item(dugum[0])["values"][1])
        self.__tasinanNesneler[6].insert(0, self.__tasinanNesneler[3].item(dugum[0])["values"][2])   
        self.__tasinanNesneler[7] = 1    
        
        if len(self.__tasinanNesneler) > 8:
            self.__tasinanNesneler.pop()
        
        kayıt = []
        kayıt.append(self.__tasinanNesneler[4].get())#ad soyad ekleniyor.
        kayıt.append(self.__tasinanNesneler[5].get())#telefon numarası ekleniyor.
        kayıt.append(self.__tasinanNesneler[6].get())#eposta ekleniyor.
        self.__tasinanNesneler.append(kayıt)#Düzenlenecek olan kayıdın asıl hali

    def duzenle(self):
        
        # self.__tasinanNesneler.append(aramaTuruCombo) 0.indeks
        # self.__tasinanNesneler.append(aranacakKelimeLabel) 1.indeks
        # self.__tasinanNesneler.append(aranacakKelimeEntry) 2.indeks
        # self.__tasinanNesneler.append(rehberAgaci) 3.indeks
        # self.__tasinanNesneler.append(adSoyadEntry) 4.indeks
        # self.__tasinanNesneler.append(telefonNumarasiEntry) 5.indeks
        # self.__tasinanNesneler.append(ePostaEntry) 6.indeks 

        if self.__tasinanNesneler[7] == 0:
            showwarning("Uyarı", "Düzenleme yapmak için listeden bir kayıt seçiniz!")
            return False

        #Düzenlenmiş kayıt bilgileri
        adSoyad = self.__tasinanNesneler[4].get()
        telNum = self.__tasinanNesneler[5].get()
        ePosta = self.__tasinanNesneler[6].get()
        #########################################

        #Asıl kayıt bilgileri
        AsilAdSoyad = self.__tasinanNesneler[8][0]
        AsilTelNum = self.__tasinanNesneler[8][1]
        AsilEPosta = self.__tasinanNesneler[8][2]
        #########################################

        if AsilAdSoyad == adSoyad and AsilTelNum ==  telNum and AsilEPosta == ePosta:
            showwarning("Uyarı","Seçtiğiniz kayıtta herhangi bir güncelleme yapmadınız.")
            return False

        if not self.kayitKurallari(adSoyad, telNum, ePosta):
            return False
        
        dsy = self.dosyaAc("+a")
        dsy.seek(0)
        icerikler = dsy.readlines()

        adSoyadListesi = []
        telefonListesi = []
        ePostaListesi = []

        for icerik in icerikler:
            adSoyadListesi.append(icerik.split(";")[0].strip("\n"))
            telefonListesi.append(icerik.split(";")[1].strip("\n"))
            ePostaListesi.append(icerik.split(";")[2].strip("\n"))

        adSoyadListesi.remove(AsilAdSoyad)
        telefonListesi.remove(AsilTelNum)
        ePostaListesi.remove(AsilEPosta)

        if adSoyad in adSoyadListesi:
            showwarning("Uyarı", "Girdiğiniz Ad ve Soyada sahip bir kayıt var.\nBu yüzden işleminiz yapılmıyor.")
            return False

        if telNum in telefonListesi:
            showwarning("Uyarı", "Girdiğiniz Telefon Numarasına sahip bir kayıt var.\nBu yüzden işleminiz yapılmıyor.")
            return False

        if ePosta in ePostaListesi:
            showwarning("Uyarı", "Girdiğiniz E-Postaya sahip bir kayıt var.\nBu yüzden işleminiz yapılmıyor.")
            return False

        icerikler.remove(AsilAdSoyad + ";" + AsilTelNum + ";" + AsilEPosta + "\n")
        icerikler.append(adSoyad + ";" + telNum + ";" + ePosta + "\n")
                
        showinfo("Bilgilendirme", "Ad Soyad = {}, Telefon Numarası = {}, E-Posta = {} olan kayıt \nAd Soyad = {}, Telefon Numarası = {}, E-Posta = {} olacak şekilde güncellendi.".format(AsilAdSoyad, AsilTelNum, AsilEPosta, adSoyad, telNum, ePosta))
        
        dsy.seek(0)
        dsy.truncate()
        dsy.writelines(icerikler)
        dsy.close()

        self.__rehberBilgisi = []

        self.rehberBilgisiAlma()
        self.rehberAgaciniGuncelleme(3)

        self.__tasinanNesneler[7] = 0
        self.__tasinanNesneler.pop(8) 

        #Entrylerin içeriği temizlenir.
        for indeks in [4,5,6]:#İşleme girecek olan Entry'ler self.__tasinanNesneler llistesinde 4, 5, ve 6. indekserde bulunuyor.
            self.__tasinanNesneler[indeks].delete(0, END)        

if __name__ == "__main__":
    td = TelefonDefteri()
    td.hepsiniListeleEkrani()
