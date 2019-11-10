from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import os
from ctypes import windll
import string
import subprocess

class DosyaKlasorArama():
    __ayarSecenekleri={
        "sürücü" : "Hepsinde",
        "aramaTuru" : "Tüm arama seçeneklerini dikkate al.",
        "yazdirmaTuru" : "Tüm yazdırma seçeneklerini dikkate al.",
        "uzantiDurum" : "Dosya uzantılarına dikkat et.",
        "dosyaTipi" : "Dosya",
        "ciktiSeceneği": "Tüm sonuçların çıktısını al.",
        }

    __sonuclar=[{},{}]
    #1. sözlük birebir benzerleri tutacak
    #2. sözlük birbirine yakın olanları tutacak

    __aramaSecenekleri=[
        "Tüm arama seçeneklerini dikkate al.",
        "Birebir benzer isimdeki dosyaları bul.",
        "Birbirine yakın isimdeki dosyaları bul.",
    ]

    __yazdirmaSecenekleri=[
        "Tüm yazdırma seçeneklerini dikkate al.",
        "Birebir benzer isimdeki dosyaları yazdır.",
        "Birbirine yakın isimdeki dosyaları yazdır.",
    ]

    __ciktiSecenekleri=[
        "Tüm sonuçların çıktısını al.",
        "Birebir benzer isimde bulunan dosyaların çıktısını al.",
        "Birbirine yakın isimde bulunan dosyaların çıktısını al.",
    ]

    __dosyaTipSecenekleri=[
        "Dosya",
        "Klasör",
    ]    

    __toplamBulunanlarSayisi=[]

    def __init__(self):
        self.anaPencereYap()
        self.anaPencereNesneleri()
        self.anaPencere.mainloop()

    def anaPencereYap(self):
        self.anaPencere=Tk()
        self.anaPencere.title("Dosya/Klasör Bulma Programı")
        self.anaPencere.geometry("700x600+100+150")
        self.anaPencere.resizable(width=FALSE,height=FALSE)

    def anaPencereNesneleri(self):
        menu1 = Menu(self.anaPencere)
        self.anaPencere.config( menu = menu1 )
        
        menuSecenekler = Menu(menu1, tearoff = 0)
        menu1.add_cascade(label = "Seçenekler", menu = menuSecenekler)
        menuSecenekler.add_command(label = "Ayarlar", command = self.ayarlar)
        menuSecenekler.add_separator()
        menuSecenekler.add_command(label = "Ekranı Temizle", command = self.temizle)
        menuSecenekler.add_command(label = "Sonuçların Çıktısını Al", command = self.ciktiAl)
        menuSecenekler.add_command(label = "Bilgilendirme", command = self.bilgilendirme)
        menuSecenekler.add_separator()
        menuSecenekler.add_command(label = "Hakkımda", command = self.hakkimda)

        self.etiketAciklama = Label(self.anaPencere, text="Aşağıya aramak istediğiniz {} ismini yazınız.".format(self.__ayarSecenekleri["dosyaTipi"]))

        etiketAd = Label(self.anaPencere,text="Adı giriniz : ")

        self.entryAranan = Entry(self.anaPencere, width = 80)

        buttonArama = Button(self.anaPencere, text="Aramaya Başla", width=13, command=self.ara)

        #scrollbar kısmı 
        dikeyScrollBar = Scrollbar(self.anaPencere, orient="vertical")
        yatayScrollBar = Scrollbar(self.anaPencere, orient="horizontal")

        #listbox'a scrollbar ekleme
        self.ListSonuclar = Listbox(self.anaPencere, yscrollcommand = dikeyScrollBar.set, xscrollcommand = yatayScrollBar.set, width = 110, height = 32)

        dikeyScrollBar["command"] = self.ListSonuclar.yview
        yatayScrollBar["command"] = self.ListSonuclar.xview
        #####################################################################

        self.ListSonuclar.bind('<Double-Button>', self.ac)

        self.etiketAciklama.place(relx=0.01,rely=0.01)
        etiketAd.place(relx=0.01,rely=0.05)

        self.entryAranan.place(relx=0.11,rely=0.05)
        buttonArama.place(relx=0.815,rely=0.042)


        self.ListSonuclar.place(relx=0.01,rely=0.1)
        dikeyScrollBar.place(relx=0.965,rely=0.1, relheight = 0.85)
        yatayScrollBar.place(relx=0.01,rely= 0.965, relwidth = 0.95)

    def ac(self, event):
        deger = self.ListSonuclar.get(ACTIVE)
        if deger:
            if self.__ayarSecenekleri["dosyaTipi"] == "Dosya":#Dosya aranacak
                deger = os.path.dirname(deger)

            subprocess.Popen(['explorer.exe', deger])

    def temizle(self):
        self.entryAranan.delete(0,END)
        self.ListSonuclar.delete(0,END)

    def ciktiAl(self):
        pencere = Toplevel()
        pencere.geometry("420x140+500+100")
        pencere.resizable(width=FALSE, height=FALSE)
        pencere.title("Sonuçların Çıktısını Alma Ekranı")

        etiketAdres=Label(pencere, text="""Aşağıdaki alana geçmiş işlemlerin kaydedilmesi istenen yeri giriniz.
        Örneğin; C:\Klasör\cıktı.
        Burada C:\Klasör\ dosyanın kaydedileceği konum cıktı ise dosyanın adıdır.""")

        self.entryAdres=Entry(pencere,width=68)

        buttonDosyaKaydet = Button(pencere, text = "Kaydet", command=self.dosyaKaydet)
        buttonDosyaAc = Button(pencere, text = "Dosyayı Aç", command=self.dosyaAc)


        etiketAdres.place(relx=0.0,rely=0.01)
        buttonDosyaKaydet.place(relx=0.1,rely=0.78)
        buttonDosyaAc.place(relx=0.7,rely=0.78)
        self.entryAdres.place(relx=0.01,rely=0.6)

        pencere.mainloop()

    def dosyaKaydet(self):
        import datetime

        kayitYeri = self.entryAdres.get()

        try:
            if kayitYeri=="":
                showwarning("Uyarı","Lütfen Kayıt yeri ve dosya adını giriniz.")

            elif os.path.exists((kayitYeri +".txt")):
                showerror("Hata","Bu adreste aynı ada sahip başka bir dosya var. Bu yüzden başka bir dosya adı giriniz.")

            else:
                #dosya açılıyor.
                dosya = open((kayitYeri +".txt"),"w")

                #Tarih bilgisi ekleniyor.
                gecici = datetime.datetime.now()
                tarih = "{}.{}.{} tarihinde {}:{} saatinde dosyaya eklenenler =>\n\n".format(gecici.day,gecici.month,gecici.year,gecici.hour,gecici.minute)
                dosya.write(tarih)
                #işlemler ekleniyor.
                if self.__ayarSecenekleri["ciktiSeceneği"] == "Tüm sonuçların çıktısını al.":
                    for sonuc in self.__sonuclar[0].keys():
                        dosya.write(sonuc + "\n")
                    
                    dosya.write("\n")

                    for sonuc in self.__sonuclar[1].keys():
                        dosya.write(sonuc + "\n")
                
                elif self.__ayarSecenekleri["ciktiSeceneği"] == "Birebir benzer isimde bulunan dosyaların çıktısını al.":              
                    for sonuc in self.__sonuclar[0].keys():
                        dosya.write(sonuc + "\n")
                
                else:
                    for sonuc in self.__sonuclar[1].keys():
                        dosya.write(sonuc + "\n")               

                #dosya kapanıyor.
                dosya.close()

                showinfo("Bilgilendirme","Dosya oluşturularak geçmiş bilgileri kaydedildi.")

        except:
           showerror("Hata","Sonuçlar kaydedilirken anlaşılamayan bir hata oluştu")

    def dosyaAc(self):
        kayitYeri=self.entryAdres.get()

        try:
            if kayitYeri=="":
                showwarning("Uyarı","Lütfen Kayıt yeri ve dosya adını giriniz.")

            elif os.path.exists((kayitYeri +".txt")):
                os.system("notepad " + (kayitYeri+".txt") )
            else:
                showerror("Hata","Bu adreste dosya bulunamadı.")
        except:
            showerror("Hata","Dosya açılırken anlaşılamayan bir hata oluştu")

    def bilgilendirme(self):
        showinfo("Bilgilendirme", "Arama sonucunda toplamda {} sonuç bulundu.\nBunlardan {} tanesinin adları birebir benzer\n   {} tanesinin adları yaklaşık benzerdir.".format((self.__toplamBulunanlarSayisi[0] + self.__toplamBulunanlarSayisi[1]),self.__toplamBulunanlarSayisi[0],self.__toplamBulunanlarSayisi[1]))

    def ayarlar(self):
        self.ayarPenceresi = Tk()
        self.ayarPenceresi.title("Ayarlar Ekranı")
        self.ayarPenceresi.geometry("700x500+100+150")
        self.ayarPenceresi.resizable(width=FALSE,height=FALSE)

        etiketSurucu = Label( self.ayarPenceresi, text="Sistemde bulunan sürücüler aşağıdadır. Bunlardan hangisinde arama yapılsın? ")

        suruculer = self.suruculeriBul()
        suruculer.insert(0,"Hepsinde")
        self.comboSurucu = ttk.Combobox( self.ayarPenceresi, state = 'readonly', values = suruculer, width=110)
        ######################################################
        #kullanılan seçeneğin aktif olarak gösterilmesi için
        indeks = suruculer.index(self.__ayarSecenekleri["sürücü"])
        self.comboSurucu.current(indeks)
        ######################################################

        buttonOnay = Button(self.ayarPenceresi, text="Değişiklikleri Onayla", command=self.onay, width=97)

        etiketTip = Label( self.ayarPenceresi, text="Aşağıdaki türlerden hangisine göre arama yapılsın?")

        self.comboTur = ttk.Combobox( self.ayarPenceresi, state = 'readonly', values = self.__dosyaTipSecenekleri, width=110)
        ######################################################
        #kullanılan seçeneğin aktif olarak gösterilmesi için
        indeks = self.__dosyaTipSecenekleri.index(self.__ayarSecenekleri["dosyaTipi"])
        self.comboTur.current(indeks)
        ######################################################

        etiketArama = Label( self.ayarPenceresi, text="Aşağıdaki koşullardan hangisine göre arama yapılsın?")

        self.comboArama = ttk.Combobox( self.ayarPenceresi, state = 'readonly', values = self.__aramaSecenekleri, width=110)
        ######################################################
        #kullanılan seçeneğin aktif olarak gösterilmesi için
        indeks = self.__aramaSecenekleri.index(self.__ayarSecenekleri["aramaTuru"])
        self.comboArama.current(indeks)
        ######################################################

        etiketYazdirma = Label( self.ayarPenceresi, text="Aşağıdaki koşullardan hangisine göre yazdırma yapılsın?")

        self.comboYazdirma = ttk.Combobox( self.ayarPenceresi, state = 'readonly', values = self.__yazdirmaSecenekleri, width=110)
        ######################################################
        #kullanılan seçeneğin aktif olarak gösterilmesi için
        indeks = self.__yazdirmaSecenekleri.index(self.__ayarSecenekleri["yazdirmaTuru"])
        self.comboYazdirma.current(indeks)
        ######################################################

        etiketCikti = Label( self.ayarPenceresi, text="Aşağıdaki koşullardan hangisine göre çıktı alınsın?")

        self.comboCikti = ttk.Combobox( self.ayarPenceresi, state = 'readonly', values = self.__ciktiSecenekleri, width=110)
        ######################################################
        #kullanılan seçeneğin aktif olarak gösterilmesi için
        indeks = self.__ciktiSecenekleri.index(self.__ayarSecenekleri["ciktiSeceneği"])
        self.comboCikti.current(indeks)
        ######################################################

        etiketSurucu.place(relx=0.01,rely=0.01)
        self.comboSurucu.place(relx=0.01,rely=0.05)
        
        etiketArama.place(relx=0.01,rely=0.19)
        self.comboArama.place(relx=0.01,rely=0.23)

        etiketYazdirma.place(relx=0.01,rely=0.38)
        self.comboYazdirma.place(relx=0.01,rely=0.42)

        etiketTip.place(relx=0.01,rely=0.56)
        self.comboTur.place(relx=0.01,rely=0.60)

        etiketCikti.place(relx=0.01,rely=0.71)
        self.comboCikti.place(relx=0.01,rely=0.75)

        buttonOnay.place(relx=0.01,rely=0.9)

        self.ayarPenceresi.mainloop()

    def onay(self):
        self.__ayarSecenekleri["sürücü"] = self.comboSurucu.get()
        self.__ayarSecenekleri["aramaTuru"] = self.comboArama.get()
        self.__ayarSecenekleri["yazdirmaTuru"] = self.comboYazdirma.get()
        self.__ayarSecenekleri["dosyaTipi"] = self.comboTur.get()
        self.__ayarSecenekleri["ciktiSeceneği"] = self.comboCikti.get()

        self.etiketAciklama.config(text="Aşağıya aramak istediğiniz {} ismini yazınız.".format(self.__ayarSecenekleri["dosyaTipi"]))

        self.ayarPenceresi.destroy()

    def suruculeriBul(self):
        suruculer = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                suruculer.append(letter)
            bitmask >>= 1

        return suruculer

    def araBul(self, aranan, suruculer):

        indeks = self.__aramaSecenekleri.index(self.__ayarSecenekleri["aramaTuru"])#seçili arama türü belirleniyor.
        for kokDizin, altDizin, dosya in os.walk(suruculer):

            if self.__ayarSecenekleri["dosyaTipi"] == "Dosya":#Dosya aranacak
                if len(dosya) > 0: #yani bu dizinde dosya var demektir.
                    for dos in dosya:
                        ad, uzanti = os.path.splitext(dos)

                        if indeks == 0:

                            if aranan == ad:
                                dosyaninYeri = os.sep.join([kokDizin,dos])
                                self.__sonuclar[0][dosyaninYeri] = dos

                            elif aranan in ad:
                                dosyaninYeri = os.sep.join([kokDizin,dos])
                                self.__sonuclar[1][dosyaninYeri] = dos  
                        
                        elif indeks == 1:
                            if aranan == ad:
                                dosyaninYeri = os.sep.join([kokDizin,dos])
                                self.__sonuclar[0][dosyaninYeri] = dos
                        else:
                            if aranan in ad:
                                dosyaninYeri = os.sep.join([kokDizin,dos])
                                self.__sonuclar[1][dosyaninYeri] = dos 

            else:#Klasör aranacak
                if len(altDizin) > 0: #yani bu dizinde dosya var demektir.
                    for altD in altDizin:

                        if indeks == 0:

                            if aranan == altD:
                                dosyaninYeri = os.sep.join([kokDizin,altD])
                                self.__sonuclar[0][dosyaninYeri] = altD

                            elif aranan in altD:
                                dosyaninYeri = os.sep.join([kokDizin,altD])
                                self.__sonuclar[1][dosyaninYeri] = altD  
                        
                        elif indeks == 1:
                            if aranan == altD:
                                dosyaninYeri = os.sep.join([kokDizin,altD])
                                self.__sonuclar[0][dosyaninYeri] = altD
                        else:
                            if aranan in altD:
                                dosyaninYeri = os.sep.join([kokDizin,altD])
                                self.__sonuclar[1][dosyaninYeri] = altD 

    def ara(self):
        self.ListSonuclar.delete(0,END)
        self.__sonuclar[0] = {}
        self.__sonuclar[1] = {}

        aranan = self.entryAranan.get()
        
        if not aranan:
            showwarning("Dikkat","Arama yapmak için bir {} ismi girmediniz...".format(self.__ayarSecenekleri["dosyaTipi"]))
            return False

        showinfo("Bilgilendirme","İşleme başlanıyor! Tamam tuşuna bastıktan sonra sonuçlar elde edilinceye kadar bekleyiniz...")

        self.__toplamBulunanlarSayisi=[]
        gecici1 = gecici2 = 0

        if self.__ayarSecenekleri["sürücü"] != "Hepsinde":                
            self.araBul(aranan, self.__ayarSecenekleri["sürücü"] + ":" + os.sep)
            
            gecici1 = len(self.__sonuclar[0])
            gecici2 = len(self.__sonuclar[1])             

            self.yazdir(self.__ayarSecenekleri["sürücü"])

        else:#Hepsinde arama yapılacak demektir.

            suruculer = self.suruculeriBul()
            for surucu in suruculer:
                self.__sonuclar[0] = {}
                self.__sonuclar[1] = {}
                self.araBul(aranan, surucu + ":" + os.sep)

                gecici1 += len(self.__sonuclar[0])
                gecici2 += len(self.__sonuclar[1]) 

                self.yazdir(surucu)

        self.__toplamBulunanlarSayisi.append(gecici1)
        self.__toplamBulunanlarSayisi.append(gecici2)

        showinfo("Bilgilendirme","İşlem Tamamlandı.\nElde edilen sonuçlardan birine çift tıklandığında onun bulunduğu klasör açılacaktır...")
        
        
    def yazdir(self, surucu):

        if not self.__sonuclar[0] and not self.__sonuclar[1]:
            showinfo("Bilgilendirme", "{} sürücüsünde herhangi bir sonuç bulunamadı...\nİşleme devam ediliyor..".format(surucu))
            return False

        indeks = self.__yazdirmaSecenekleri.index(self.__ayarSecenekleri["yazdirmaTuru"])#seçili yazdirma türü belirleniyor.

        if indeks == 0:
            
            for sonuc in self.__sonuclar[0].keys():
                self.ListSonuclar.insert(0,sonuc)
            
            self.ListSonuclar.insert(END," ")

            for sonuc in self.__sonuclar[1].keys():
                self.ListSonuclar.insert(END,sonuc)

        elif indeks == 1:

            for sonuc in self.__sonuclar[0].keys():
                self.ListSonuclar.insert(0,sonuc)

        else:

            for sonuc in self.__sonuclar[1].keys():
                self.ListSonuclar.insert(0,sonuc)            

    def hakkimda(self):
        showinfo("Hakkımda", "Saffet Murat tarafından yapıldı\n(Created by: Saffet Murat)\n\n{}\n\n{}".format("https://trmsma.wordpress.com","https://github.com/saffetmurat"))

if __name__ == "__main__":
    DosyaKlasorArama()
