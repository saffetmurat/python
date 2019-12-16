from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk # Combobox kullanımı için

import random
import VeritabaniIslemleri

class Bankamatik():

    __pencereListesi=[]
    __nesneler=[]#Her fonksiyon için gerekli olan nesneleri tutacak Geri tuşuna basıldığında içi silinecek

    def __init__(self):
        self.girisEkrani()

    def hesapBilgisiAlma(self, hesapNumarasi=False):
        ############ Hesap Bilgisi Alınır ####################################
        self.hesaplarBilgisi=[]
        vti = VeritabaniIslemleri.VeritabaniIslemleri()
        self.hesaplarBilgisi = vti.hesapBilgisiAl(self.musteriBilgisi[0][0])#self.musteriBilgisi[0][0] ile giriş yapan müşterinin müşteri ID'si alınır.
        #self.hesaplarBilgisi müşteriye ait tüm hesapları tutuyor.
        ######################################################################
        if hesapNumarasi:
            for hesap in self.hesaplarBilgisi:
                if str(hesap[1]) == hesapNumarasi:
                    hesapId = hesap[0]
                    hesaptakiTutar = hesap[2]
                    hesapTuru = hesap[3]
                    return hesapId, hesaptakiTutar, hesapTuru, hesapNumarasi

    def anaPencereEkrani(self):
        self.anaPencere = Tk()
        self.anaPencere.title("Bankamatik Uygulaması - Ana Ekran")
        self.anaPencere.geometry("600x600+200+200")
        self.anaPencere.resizable(width=FALSE, height=FALSE)

        self.anaPencere.protocol('WM_DELETE_WINDOW', self.cikis)

        self.hesapBilgisiAlma()

        selamLabel = Label(self.anaPencere, text="Merhabalar {} {} ! ".format(self.musteriBilgisi[0][2],self.musteriBilgisi[0][3]), font="Times 16")
        aciklaLabel = Label(self.anaPencere, text="\nBu uygulama ile aşağıdaki İşlemleri yapabilirsiniz!", font="Times 14")

        bttnHesapGoster = Button(self.anaPencere, text="Mevcut Hesapları Göster", font="Times 15", width=50, command=self.hesapGosterEkrani)
        bttnParaCek = Button(self.anaPencere, text="Para Çek", font="Times 15", width=50, command=self.paraCekEkrani)
        bttnParaYatır = Button(self.anaPencere, text="Para Yatır", font="Times 15", width=50, command=self.paraYatirEkrani)
        bttnParaTransferi = Button(self.anaPencere, text="Hesaplar Arası Para Transferi Yap", font="Times 15", width=50, command=self.paraTransferiEkrani)
        bttnHesapAc = Button(self.anaPencere, text="Yeni Bir Hesap Aç", font="Times 15", width=50, command=self.hesapAcEkrani)
        bttnHesapSil = Button(self.anaPencere, text="Hesap Sil", font="Times 15", width=50, command=self.hesapSilEkrani)
        bttnBorcOde = Button(self.anaPencere, text="Borç Öde", font="Times 15", width=50, command=self.borcOdeEkrani)
        bttnCikis = Button(self.anaPencere, text="Çıkış", font="Times 15", width=50, bg="red", fg="white", command=self.cikis)

        selamLabel.place(relx=0.05,rely=0.01)
        aciklaLabel.place(relx=0.1,rely=0.05)

        bttnHesapGoster.place(relx=0.03,rely=0.19)
        bttnParaCek.place(relx=0.03,rely=0.29)
        bttnParaYatır.place(relx=0.03,rely=0.39)
        bttnParaTransferi.place(relx=0.03,rely=0.49)
        bttnHesapAc.place(relx=0.03,rely=0.59)
        bttnHesapSil.place(relx=0.03,rely=0.69)
        bttnBorcOde.place(relx=0.03,rely=0.79)
        bttnCikis.place(relx=0.03,rely=0.89)

        self.anaPencere.mainloop()

    def nesneDoldur(self, *args):
        for nesne in args:
            self.__nesneler.append(nesne)

    def ortakPencereKisimlari(self, baslik, boyutlar, agacYukseklik=18, agacGenislik=186, butonFont="Times 14", butonGenislik=26):
        self.anaPencere.destroy()

        hesapPencere = Tk()
        hesapPencere.title(baslik)
        hesapPencere.geometry(boyutlar)
        hesapPencere.resizable(width=FALSE, height=FALSE)

        hesapPencere.protocol('WM_DELETE_WINDOW', self.geri) #Penceredeki X işaretine yeni bir işlem yüklendi.

        self.__pencereListesi.append(hesapPencere)#Böyle yaparak ayrı ayrı self.geri() fonksiyonu yazılmayacak.

        aciklamaLabel = Label(hesapPencere, text="Size ait Mevcut Hesaplar aşağıda listelenmektedir.", font="Times 14")

        #scrollBar tanımlanıyor.
        dikeyScrollBar = Scrollbar(hesapPencere, orient="vertical")
        yatayScrollBar = Scrollbar(hesapPencere, orient="horizontal")

        hesapAgaci = ttk.Treeview(hesapPencere, show="headings", height=agacYukseklik, yscrollcommand = dikeyScrollBar.set, xscrollcommand = yatayScrollBar.set)

        dikeyScrollBar["command"] = hesapAgaci.yview
        yatayScrollBar["command"] = hesapAgaci.xview
        ###########################################################################

        hesapAgaci['columns'] = ('hesapNumarası', 'hesaptakiTutar', 'hesapTuru')

        hesapAgaci.column('hesapNumarası', width=agacGenislik, anchor='center')
        hesapAgaci.heading('hesapNumarası', text='Hesap Numarası')

        hesapAgaci.column('hesaptakiTutar', width=agacGenislik, anchor='center')
        hesapAgaci.heading('hesaptakiTutar', text='Hesaptaki Tutar')

        hesapAgaci.column('hesapTuru', width=agacGenislik, anchor='center')
        hesapAgaci.heading('hesapTuru', text='Hesap Türü')

        ############## VERİ EKLEME KISMI #################################################################
        #Aşağıdaki yapıda veri eklenecektir.
        #hesapAgaci.insert('', 'end', text='hesapIdsi', values=('hesapNumarası hesaptakiTutar hesapTuru'))
        for hesap in self.hesaplarBilgisi:
            hesapAgaci.insert('', 'end', text='hesapIdsi', values=(str(hesap[1]), str(hesap[2]), hesap[3]))
        ###################################################################################################

        buttonGeri = Button(hesapPencere, text="Geri", font="{}".format(butonFont), bg="white", width=butonGenislik, command=self.geri)

        return buttonGeri, aciklamaLabel, hesapAgaci, dikeyScrollBar, yatayScrollBar

    def hesapAgaciniGuncelleme(self, nesneIndeksi):
        self.hesapBilgisiAlma()#Müşteriye ait hesap bilgisi alınıyor.

        ############## TREEVİEW'DE VERİ GUNCELLEME KISMI #################################################################
        #Aşağıdaki yapıda veri eklenecektir.
        #hesapAgaci.insert('', 'end', text='hesapIdsi', values=('hesapNumarası hesaptakiTutar hesapTuru'))

        for dugum in self.__nesneler[nesneIndeksi].get_children(""):#Bu döngü ile treeview boşaltılıyor.
            self.__nesneler[nesneIndeksi].delete(dugum)

        for hesap in self.hesaplarBilgisi:
            self.__nesneler[nesneIndeksi].insert('', 'end', text='hesapIdsi', values=(str(hesap[1]), str(hesap[2]), hesap[3]))
        ###################################################################################################################
        
    def hesapGosterEkrani(self):
        buttonGeri, aciklamaLabel, hesapAgaci, dikeyScrollBar, yatayScrollBar = self.ortakPencereKisimlari("Bankamatik Uygulaması - Hesaplar Ekranı", "600x600+200+200", 22, 187, "Times 15", 50)

        aciklamaLabel.place(relx=0.039,rely=0.01)
        hesapAgaci.place(relx=0.03,rely=0.07)
        buttonGeri.place(relx=0.03,rely=0.89)

        dikeyScrollBar.place(relx=0.97,rely=0.068, relheight = 0.78)
        yatayScrollBar.place(relx=0.03,rely= 0.855, relwidth = 0.94)

        self.__pencereListesi[0].mainloop()

    def geri(self):
        self.__pencereListesi[0].destroy()#Oluşturulan pencere buradan silinir.
                                          #Böylece her pencere için ayrı ayrı geri() fonksiyonu yazılmaz.
                                          #Ayrıca her pencereye ayrı ayrı self özelliği verilmemiş olundu
        self.__pencereListesi = []
        self.__nesneler=[]#O pencere içinde oluşturulan nesnelerde kaldırılıyor.
        self.anaPencereEkrani()

    def paraCekEkrani(self):
        buttonGeri, aciklamaLabel, hesapAgaci, dikeyScrollBar, yatayScrollBar = self.ortakPencereKisimlari("Bankamatik Uygulaması - Para Çekme Ekranı", "600x600+200+200")

        paraCekLabel = Label(self.__pencereListesi[0], text="Paranın Çekileceği Hesap Numarasını seçiniz ", font="Times 12")
        comboHesapNo = ttk.Combobox( self.__pencereListesi[0], state = 'readonly', values = [hesap[1] for hesap in self.hesaplarBilgisi], width=15)
        comboHesapNo.current(0)

        tutarLabel = Label(self.__pencereListesi[0], text="Tutarı giriniz ", font="Times 12")
        tutarEntry = Entry(self.__pencereListesi[0])
       
        hesapTurLabel = Label(self.__pencereListesi[0], text="{}".format(self.hesaplarBilgisi[0][3]), font="Times 12")#Başlangıçta ilk kayıttaki hesap türü alınır.

        self.nesneDoldur(comboHesapNo, hesapTurLabel, tutarEntry, hesapAgaci)

        comboHesapNo.bind("<<ComboboxSelected>>", self.combodanGelen)

        buttonCek = Button(self.__pencereListesi[0], text="Parayı Çek", font="Times 14", bg="lightblue", width=26, command=self.paraCek)

        aciklamaLabel.place(relx=0.039,rely=0.01)
        hesapAgaci.place(relx=0.03,rely=0.07)

        paraCekLabel.place(relx=0.03,rely=0.77)
        comboHesapNo.place(relx=0.50,rely=0.774)

        tutarLabel.place(relx=0.03,rely=0.83)
        tutarEntry.place(relx=0.17,rely=0.835)
        hesapTurLabel.place(relx=0.385,rely=0.83)

        buttonGeri.place(relx=0.03,rely=0.89)
        buttonCek.place(relx=0.52,rely=0.89)

        dikeyScrollBar.place(relx=0.97,rely=0.068, relheight = 0.645)
        yatayScrollBar.place(relx=0.03,rely= 0.725, relwidth = 0.94)

        self.__pencereListesi[0].mainloop()

    def combodanGelen(self, event):#combobaxtaki değişime göre güncelleme yapıyor.
        hesapNumarasi = self.__nesneler[0].get()#self.__nesneler[0]=comboHesapNo
        for hesap in self.hesaplarBilgisi:
            if str(hesap[1]) == hesapNumarasi:
                self.__nesneler[1].config(text=str(hesap[3]))#self.__nesneler[1]=hesapTurLabel
    
    def paraCek(self):
        #self.__nesneler[0].get()#comboHesapNo bulunuyor.
        hesapId, hesaptakiTutar, hesapTuru, hesapNumarasi = self.hesapBilgisiAlma(self.__nesneler[0].get())

        girilenTutar = self.__nesneler[2].get()#tutarEntry bulunuyor.
        if girilenTutar == "":
            showwarning("Uyarı","Lütfen bir tutar giriniz!")
        
        elif not girilenTutar.isdigit():
            showwarning("Uyarı","Lütfen pozitif bir sayı giriniz!")     

        elif hesaptakiTutar < int(girilenTutar):
            showwarning("Uyarı","Çekmek istediğiniz kadar tutar hesabınızda yoktur.\nBu yüzden bu işlem yapılmıyor.")
        else:
            showinfo("Bilgilendirme","İşleminiz Onaylandı.\nParanızı aldıktan sonra Tamam tuşuna basınız...")
            vti = VeritabaniIslemleri.VeritabaniIslemleri()
            hesaptakiTutar = hesaptakiTutar-int(girilenTutar)
            vti.hesapBilgisiTutarGuncelle(hesapId,hesaptakiTutar)

            self.hesapAgaciniGuncelleme(3)

    def paraYatirEkrani(self):
        buttonGeri, aciklamaLabel, hesapAgaci, dikeyScrollBar, yatayScrollBar = self.ortakPencereKisimlari("Bankamatik Uygulaması - Para Yatırma Ekranı", "600x600+200+200")
                
        paraYatirLabel = Label(self.__pencereListesi[0], text="Paranın Yatırılacağı Hesap Numarasını seçiniz ", font="Times 12")
        comboHesapNo = ttk.Combobox( self.__pencereListesi[0], state = 'readonly', values = [hesap[1] for hesap in self.hesaplarBilgisi], width=15)
        comboHesapNo.current(0)

        tutarLabel = Label(self.__pencereListesi[0], text="Tutarı giriniz ", font="Times 12")
        tutarEntry = Entry(self.__pencereListesi[0])
       
        hesapTurLabel = Label(self.__pencereListesi[0], text="{}".format(self.hesaplarBilgisi[0][3]), font="Times 12")#Başlangıçta ilk kayıttaki hesap türü alınır.

        self.nesneDoldur(comboHesapNo, hesapTurLabel, tutarEntry, hesapAgaci)

        comboHesapNo.bind("<<ComboboxSelected>>", self.combodanGelen)

        buttonYatir = Button(self.__pencereListesi[0], text="Parayı Yatır", font="Times 14", bg="lightblue", width=26, command=self.paraYatir)

        aciklamaLabel.place(relx=0.039,rely=0.01)
        hesapAgaci.place(relx=0.03,rely=0.07)

        paraYatirLabel.place(relx=0.03,rely=0.77)
        comboHesapNo.place(relx=0.50,rely=0.774)

        tutarLabel.place(relx=0.03,rely=0.83)
        tutarEntry.place(relx=0.17,rely=0.835)
        hesapTurLabel.place(relx=0.385,rely=0.83)

        buttonGeri.place(relx=0.03,rely=0.89)
        buttonYatir.place(relx=0.52,rely=0.89)

        dikeyScrollBar.place(relx=0.97,rely=0.068, relheight = 0.645)
        yatayScrollBar.place(relx=0.03,rely= 0.725, relwidth = 0.94)

        self.__pencereListesi[0].mainloop()

    def paraYatir(self):
        hesapId, hesaptakiTutar, hesapTuru, hesapNumarasi = self.hesapBilgisiAlma(self.__nesneler[0].get())

        girilenTutar = self.__nesneler[2].get()#tutarEntry bulunuyor.
        if girilenTutar == "":
            showwarning("Uyarı","Lütfen bir tutar giriniz!")
        
        elif not girilenTutar.isdigit():
            showwarning("Uyarı","Lütfen pozitif bir sayı giriniz!")     

        else:
            showinfo("Bilgilendirme","İşleminiz Onaylandı.\nParanızı para giriş kısmına koyduktan sonra Tamam tuşuna basınız...")
            vti = VeritabaniIslemleri.VeritabaniIslemleri()
            hesaptakiTutar = hesaptakiTutar+int(girilenTutar)
            vti.hesapBilgisiTutarGuncelle(hesapId,hesaptakiTutar)

            self.hesapAgaciniGuncelleme(3)
            
    def paraTransferiEkrani(self):
        buttonGeri, aciklamaLabel, hesapAgaci, dikeyScrollBar, yatayScrollBar = self.ortakPencereKisimlari("Bankamatik Uygulaması - Para Transfer Etme Ekranı", "600x600+200+200", 13)
        
        paraCekLabel = Label(self.__pencereListesi[0], text="Paranın Çekileceği Hesap Numarasını seçiniz ", font="Times 12")
        comboHesapNo1 = ttk.Combobox( self.__pencereListesi[0], state = 'readonly', values = [hesap[1] for hesap in self.hesaplarBilgisi], width=15)
        comboHesapNo1.current(0)

        self.var = IntVar()
        radioButton1=Radiobutton(self.__pencereListesi[0], text="Kendi Hesabıma Yatır", variable=self.var, value=1, font="Times 12", command=self.secim)
        radioButton2=Radiobutton(self.__pencereListesi[0], text="Başka Bir Hesaba Yatır", variable=self.var, value=2, font="Times 12", command=self.secim)

        paraYatirKendiLabel = Label(self.__pencereListesi[0], text="Paranın Yatırılacağı Hesap Numarasını seçiniz ",state=DISABLED, font="Times 12")
        comboHesapNo2 = ttk.Combobox( self.__pencereListesi[0], state = 'disabled', values = [hesap[1] for hesap in self.hesaplarBilgisi], width=15)
        comboHesapNo2.current(0)

        paraYatirBaskaLabel = Label(self.__pencereListesi[0], text="Paranın Yatırılacağı Hesap Numarasını yazınız ",state=DISABLED, font="Times 12")
        hesapNumarasiEntry = Entry(self.__pencereListesi[0], state='disabled')

        tutarLabel = Label(self.__pencereListesi[0], text="Gönderilecek Tutarı giriniz ", font="Times 12")
        tutarEntry = Entry(self.__pencereListesi[0])
       
        hesapTurLabel = Label(self.__pencereListesi[0], text="{}".format(self.hesaplarBilgisi[0][3]), font="Times 12")#Başlangıçta ilk kayıttaki hesap türü alınır.

        self.nesneDoldur(comboHesapNo1, hesapTurLabel, tutarEntry, hesapAgaci, comboHesapNo2, paraYatirKendiLabel, paraYatirBaskaLabel, hesapNumarasiEntry)
        
        comboHesapNo1.bind("<<ComboboxSelected>>", self.combodanGelen)

        buttonTransfer = Button(self.__pencereListesi[0], text="Parayı Transfer Et", font="Times 14", bg="lightblue", width=26, command=self.paraTransfer)

        aciklamaLabel.place(relx=0.039,rely=0.01)
        hesapAgaci.place(relx=0.03,rely=0.07)

        paraCekLabel.place(relx=0.03,rely=0.597)
        comboHesapNo1.place(relx=0.50,rely=0.600)

        radioButton1.place(relx=0.03,rely=0.64)
        paraYatirKendiLabel.place(relx=0.13,rely=0.68)
        comboHesapNo2.place(relx=0.60,rely=0.685)

        radioButton2.place(relx=0.03,rely=0.72)
        paraYatirBaskaLabel.place(relx=0.13,rely=0.759)
        hesapNumarasiEntry.place(relx=0.60,rely=0.764)

        tutarLabel.place(relx=0.03,rely=0.83)
        tutarEntry.place(relx=0.315,rely=0.835)
        hesapTurLabel.place(relx=0.54,rely=0.83)

        buttonGeri.place(relx=0.03,rely=0.89)
        buttonTransfer.place(relx=0.52,rely=0.89)

        dikeyScrollBar.place(relx=0.97,rely=0.068, relheight = 0.48)
        yatayScrollBar.place(relx=0.03,rely= 0.55, relwidth = 0.94)

        self.__pencereListesi[0].mainloop()

    def secim(self):#radioButton'lara göre durumun değişmesi sağlanıyor.
        if self.var.get() == 1:
            self.__nesneler[4].config(state='readonly')#comboHesapNo2
            self.__nesneler[5].config(state=ACTIVE)#paraYatirKendiLabel
            self.__nesneler[6].config(state=DISABLED)#paraYatirBaskaLabel
            self.__nesneler[7].config(state='disabled')#hesapNumarasiEntry
        else:
            self.__nesneler[4].config(state='disabled')#comboHesapNo2
            self.__nesneler[5].config(state=DISABLED)#paraYatirKendiLabel
            self.__nesneler[6].config(state=ACTIVE)#paraYatirBaskaLabel
            self.__nesneler[7].config(state='normal')#paraYatirBaskaLabel

    def paraTransfer(self):
 
        ## GÖNDERECEK HESAP #############################################
        hesapId1, hesaptakiTutar1, hesapTuru1, hesapNumarasi1 = self.hesapBilgisiAlma(self.__nesneler[0].get())
        #################################################################
        
        girilenTutar = self.__nesneler[2].get()#self.__nesneler.append(tutarEntry)
        if girilenTutar == "":
            showwarning("Uyarı","Lütfen bir tutar giriniz!")
            return False
        
        elif not girilenTutar.isdigit():
            showwarning("Uyarı","Lütfen pozitif bir sayı giriniz!")   
            return False  
        elif hesaptakiTutar1 < int(girilenTutar):
            showwarning("Uyarı","Çekmek istediğiniz kadar tutar hesabınızda yoktur.\nBu yüzden bu işlem yapılmıyor.")
            return False

        ## ALACAK HESAP #################################################
        if self.var.get() == 1:#radioButton1 aktifse yani "Kendi Hesabıma Yatır" işlemi yapılacaksa
            #self.__nesneler[4].get()==self.__nesneler.append(comboHesapNo2)
            hesapId2, hesaptakiTutar2, hesapTuru2, hesapNumarasi2 = self.hesapBilgisiAlma(self.__nesneler[4].get())

            if hesapNumarasi1 == hesapNumarasi2:
                showerror("Hata", "Gönderen {} nolu hesap ile alan {} nolu hesap aynı kişiye ait olduğu için işlem yapılmadı.".format(hesapNumarasi1,hesapNumarasi2))

            elif hesapTuru1 == hesapTuru2:
                vti = VeritabaniIslemleri.VeritabaniIslemleri()
                hesaptakiTutar1 = hesaptakiTutar1-int(girilenTutar)
                vti.hesapBilgisiTutarGuncelle(hesapId1,hesaptakiTutar1)

                hesaptakiTutar2 = hesaptakiTutar2+int(girilenTutar)
                vti.hesapBilgisiTutarGuncelle(hesapId2,hesaptakiTutar2)
            else:
                vti = VeritabaniIslemleri.VeritabaniIslemleri()
                kuradi = hesapTuru1+"_"+hesapTuru2
                oran = vti.kurBilgisiAl(kuradi)[0][0]#Gelen listenin içindeki tupledan eleman almak için

                hesaptakiTutar1 = hesaptakiTutar1-int(girilenTutar)
                hesaptakiTutar2 = hesaptakiTutar2+round(int(girilenTutar)*oran)

                vti.hesapBilgisiTutarGuncelle(hesapId1,hesaptakiTutar1)
                vti.hesapBilgisiTutarGuncelle(hesapId2,hesaptakiTutar2)

                showinfo("Bilgilendirme","{} {} kadar para, bankanın kur oranına (1 {} = {} {}) göre \
{} {} olacak şekilde çevrilerek işlemler yapıldı.\nNOT:Hesaplamada {} {} yuvarlanarak {} {} yapıldı ve böyle işlem gördü \
".format(girilenTutar, hesapTuru1, hesapTuru1, oran, hesapTuru2, int(girilenTutar)*oran, hesapTuru2, int(girilenTutar)*oran, hesapTuru2,round(int(girilenTutar)*oran),hesapTuru2))


        elif self.var.get() == 2:#radioButton2 aktifse yani "Başka Bir Hesaba Yatır" işlemi yapılacaksa
            hesapNumarasi = self.__nesneler[7].get()#self.__nesneler.append(hesapNumarasiEntry)
            if not hesapNumarasi:
                showwarning("Uyarı","Lütfen hesap numarasını giriniz!") 
                return False
            
            vti = VeritabaniIslemleri.VeritabaniIslemleri()
            hesaptakiTutar1 = hesaptakiTutar1-int(girilenTutar)
            vti.hesapBilgisiTutarGuncelle(hesapId1,hesaptakiTutar1)

            showinfo("Bilgilendirme", "{} {} kadar para girilen {} nolu hesaba aktarıldı.".format(girilenTutar, hesapTuru1, hesapNumarasi))

        else:
            showwarning("Uyarı","Lütfen gönderilecek bir hesap belirtin")
            return False
        
        self.hesapAgaciniGuncelleme(3)

    def hesapAcEkrani(self):
        buttonGeri, aciklamaLabel, hesapAgaci, dikeyScrollBar, yatayScrollBar = self.ortakPencereKisimlari("Bankamatik Uygulaması - Hesap Açma Ekranı", "600x600+200+200", 19)
                
        hesapTurLabel = Label(self.__pencereListesi[0], text="Hesabın türünü seçiniz", font="Times 12")
        comboHesapTur = ttk.Combobox( self.__pencereListesi[0], state = 'readonly', values = ["TL","EURO","USD"], width=15)
        comboHesapTur.current(0)

        self.nesneDoldur(comboHesapTur, hesapTurLabel, hesapAgaci)

        buttonAc = Button(self.__pencereListesi[0], text="Hesabı Aç", font="Times 14", bg="lightblue", width=26, command=self.hesapAc)

        aciklamaLabel.place(relx=0.039,rely=0.01)
        hesapAgaci.place(relx=0.03,rely=0.07)

        hesapTurLabel.place(relx=0.03,rely=0.8)
        comboHesapTur.place(relx=0.28,rely=0.803)

        buttonGeri.place(relx=0.03,rely=0.89)
        buttonAc.place(relx=0.52,rely=0.89)

        dikeyScrollBar.place(relx=0.97,rely=0.068, relheight = 0.68)
        yatayScrollBar.place(relx=0.03,rely= 0.755, relwidth = 0.94)

        self.__pencereListesi[0].mainloop()

    def hesapAc(self):
        while True:
            yeniHesapNumarasi = random.randint(1,10000000000)
            for hesap in self.hesaplarBilgisi:
                if hesap[1] == yeniHesapNumarasi:
                    break;
            else:
                break;
        hesapTur = self.__nesneler[0].get()#self.__nesneler.append(comboHesapTur)

        self.musteriBilgisi[0][0]#self.musteriBilgisi[0][0] ile giriş yapan müşterinin müşteri ID'si alınır.

        vti = VeritabaniIslemleri.VeritabaniIslemleri()
        vti.yeniHesapAc(self.musteriBilgisi[0][0], yeniHesapNumarasi, hesapTur)

        showinfo("Bilgilendirme", "{} numaralı {} türündeki hesabınız başarılı bir şekilde oluşturuldu.".format(yeniHesapNumarasi, hesapTur))

        self.hesapAgaciniGuncelleme(2)

    def hesapSilEkrani(self):
        buttonGeri, aciklamaLabel, hesapAgaci, dikeyScrollBar, yatayScrollBar = self.ortakPencereKisimlari("Bankamatik Uygulaması - Hesap Silme Ekranı", "600x600+200+200", 19)
        
        hesapNumarasiLabel = Label(self.__pencereListesi[0], text="Silmek istediğiniz hesabı seçiniz", font="Times 12")
        comboHesapNo = ttk.Combobox( self.__pencereListesi[0], state = 'readonly', values = [hesap[1] for hesap in self.hesaplarBilgisi], width=15)
        comboHesapNo.current(0)

        self.nesneDoldur(comboHesapNo, hesapNumarasiLabel, hesapAgaci)

        buttonSil = Button(self.__pencereListesi[0], text="Hesabı Sil", font="Times 14", bg="lightblue", width=26, command=self.hesapSil)

        aciklamaLabel.place(relx=0.039,rely=0.01)
        hesapAgaci.place(relx=0.03,rely=0.07)

        hesapNumarasiLabel.place(relx=0.03,rely=0.8)
        comboHesapNo.place(relx=0.36,rely=0.803)

        buttonGeri.place(relx=0.03,rely=0.89)
        buttonSil.place(relx=0.52,rely=0.89)

        dikeyScrollBar.place(relx=0.97,rely=0.068, relheight = 0.68)
        yatayScrollBar.place(relx=0.03,rely= 0.755, relwidth = 0.94)

        self.__pencereListesi[0].mainloop()

    def hesapSil(self):
        hesapId, hesaptakiTutar, hesapTuru, hesapNumarasi = self.hesapBilgisiAlma(self.__nesneler[0].get())#self.__nesneler[0].get()==comboHesapNo bulunuyor.
        
        if hesaptakiTutar > 0:
            showwarning("Uyarı","Silmek istediğiniz {} numaralı hesapta para bulunduğundan dolayı silinmiyor.\nLütfen {} numaralı hesaptaki parayı çekip tekrar deneyiniz.".format(hesapNumarasi, hesapNumarasi))
            return False
        
        if len(self.hesaplarBilgisi) < 2:
            showinfo("Bilgilendirme","Bir hesabı silebilmek için toplam hesap sayınızın 1'den fazla olması gerekir.")
            showwarning("Uyarı","Toplam hesap sayınız 1'den fazla olmadığı için bu işlem yapılmıyor.")
            return False
        
        vti = VeritabaniIslemleri.VeritabaniIslemleri()
        vti.hesapSil(hesapId)
        showinfo("Bilgilendirme", "{} numaralı {} türündeki hesabınız başarılı bir şekilde silindi".format(hesapNumarasi,hesapTuru))

        self.hesapAgaciniGuncelleme(2)

        self.__nesneler[0].config(values = [hesap[1] for hesap in self.hesaplarBilgisi])#hesapSilEkrani'ndanki comboHesapNo güncelleniyor.
        self.__nesneler[0].current(0)

    def borcOdeEkrani(self):
        buttonGeri, aciklamaLabel, hesapAgaci, dikeyScrollBar, yatayScrollBar = self.ortakPencereKisimlari("Bankamatik Uygulaması - Hesap Silme Ekranı", "600x600+200+200", 15)
        
        odemeTuruLabel = Label(self.__pencereListesi[0], text = "Ödeme Türünü seçiniz", font="Times 12")
        comboOdemeTur = ttk.Combobox( self.__pencereListesi[0], state = 'readonly', values = ["Elektrik","Su","Doğal Gaz","İnternet"], width=15)
        comboOdemeTur.current(0)

        vti = VeritabaniIslemleri.VeritabaniIslemleri()
        kurumAdListesi = vti.kurumAdlari(comboOdemeTur.get())#gelen listenin içindeki tupleın ilk elemanı Id, ikincisi Ad
        kurumAdiLabel = Label(self.__pencereListesi[0], text = "Kurum Adını seçiniz", font="Times 12")
        comboKurumAdi = ttk.Combobox( self.__pencereListesi[0], state = 'readonly', values = [kurum[1] for kurum in kurumAdListesi], width=23)
        comboKurumAdi.current(0)

        sozlesmeNoLabel = Label(self.__pencereListesi[0], text="Sözleşme Numarasını giriniz ", font="Times 12")
        sozlesmeNoEntry = Entry(self.__pencereListesi[0])
        buttonSozlesmeSorgula = Button(self.__pencereListesi[0], text="Borcu Sorgula", font="Times 10", bg="cornsilk2", width=20, command=self.borcSorgula)
        
        paraCekLabel = Label(self.__pencereListesi[0], text="Paranın Çekileceği Hesap Numarasını seçiniz ", font="Times 12")
        comboHesapNo = ttk.Combobox( self.__pencereListesi[0], state = 'readonly', values = [hesap[1] for hesap in self.hesaplarBilgisi], width=15)
        comboHesapNo.current(0)

        tutarLabel = Label(self.__pencereListesi[0], text="Tutarı giriniz ", font="Times 12")
        tutarEntry = Entry(self.__pencereListesi[0])
        hesapTurLabel = Label(self.__pencereListesi[0], text="{}".format(self.hesaplarBilgisi[0][3]), font="Times 12")#Başlangıçta ilk kayıttaki hesap türü alınır.

        self.nesneDoldur(comboHesapNo, hesapTurLabel, hesapAgaci, comboOdemeTur, comboKurumAdi, tutarEntry, sozlesmeNoEntry)

        comboHesapNo.bind("<<ComboboxSelected>>", self.combodanGelen)
        comboOdemeTur.bind("<<ComboboxSelected>>", self.combodanGelen1)

        buttonOde = Button(self.__pencereListesi[0], text="Borç Öde", font="Times 14", bg="lightblue", width=26, command=self.borcOde)

        aciklamaLabel.place(relx=0.039,rely=0.01)
        hesapAgaci.place(relx=0.03,rely=0.07)

        odemeTuruLabel.place(relx=0.03,rely=0.68)
        comboOdemeTur.place(relx=0.28,rely=0.683)


        kurumAdiLabel.place(relx=0.48,rely=0.68)
        comboKurumAdi.place(relx=0.7,rely=0.683)

        sozlesmeNoLabel.place(relx=0.03,rely=0.73)
        sozlesmeNoEntry.place(relx=0.33,rely=0.735) 
        buttonSozlesmeSorgula.place(relx=0.55,rely=0.73)       

        paraCekLabel.place(relx=0.03,rely=0.78)
        comboHesapNo.place(relx=0.5,rely=0.783)
        
        tutarLabel.place(relx=0.03,rely=0.83)
        tutarEntry.place(relx=0.17,rely=0.835)
        hesapTurLabel.place(relx=0.385,rely=0.83)

        buttonGeri.place(relx=0.03,rely=0.89)
        buttonOde.place(relx=0.52,rely=0.89)

        dikeyScrollBar.place(relx=0.97,rely=0.068, relheight = 0.545)
        yatayScrollBar.place(relx=0.03,rely= 0.62, relwidth = 0.94)
 
        self.__pencereListesi[0].mainloop()

    def combodanGelen1(self, event):
        vti = VeritabaniIslemleri.VeritabaniIslemleri()
        #odemeTuru = self.__nesneler[3].get()#comboOdemeTur
        kurumAdListesi = vti.kurumAdlari(self.__nesneler[3].get())#gelen listenin içindeki tupleın ilk elemanı Id, ikincisi Ad
        self.__nesneler[4].config(values = [kurum[1] for kurum in kurumAdListesi])
        self.__nesneler[4].current(0)#self.__nesneler.append(comboKurumAdi)

    def borcSorgula(self):
        borc = random.randint(0,1000)
        if self.__nesneler[6].get() == "":
            showwarning("Uyarı","Sözleşme Numarasını giriniz!")
        elif not self.__nesneler[6].get().isdigit():
            showwarning("Uyarı","Sözleşme Numarası pozitif tam sayılardan oluşmalıdır!")
        else:
            showinfo("Bilgilendirme","{} numaralı sözleşmeye ait toplamda {} TL borç bulunmaktadır.".format(self.__nesneler[6].get(), borc))

    def borcOde(self):
        hesapId, hesaptakiTutar, hesapTuru, hesapNumarasi = self.hesapBilgisiAlma(self.__nesneler[0].get())#self.__nesneler[0].get()==comboHesapNo bulunuyor.

        girilenTutar = self.__nesneler[5].get()#tutarEntry bulunuyor.
        
        if self.__nesneler[6].get() == "":#self.__nesneler.append(sozlesmeNoEntry)
            showwarning("Uyarı","Sözleşme Numarasını giriniz!")
        
        elif not self.__nesneler[6].get().isdigit():
            showwarning("Uyarı","Sözleşme Numarası pozitif tam sayılardan oluşmalıdır!")

        elif girilenTutar == "":
            showwarning("Uyarı","Lütfen bir tutar giriniz!")
        
        elif not girilenTutar.isdigit():
            showwarning("Uyarı","Lütfen pozitif bir sayı giriniz!")     

        elif hesaptakiTutar < int(girilenTutar):
            showwarning("Uyarı","Çekmek istediğiniz kadar tutar hesabınızda yoktur.\nBu yüzden bu işlem yapılmıyor.")
        
        else:
            showinfo("Bilgilendirme","İşleminiz Onaylandı.\n{} {} kadar para ilgili borçun kapatılması için hesabınızdan çekildi.\nEn kısa sürede borç için yatırılacaktır.".format(girilenTutar, hesapTuru))
            vti = VeritabaniIslemleri.VeritabaniIslemleri()
            hesaptakiTutar = hesaptakiTutar-int(girilenTutar)
            vti.hesapBilgisiTutarGuncelle(hesapId,hesaptakiTutar)

            self.hesapAgaciniGuncelleme(2)

    def cikis(self):
        self.anaPencere.destroy()
        self.girisEkrani()

    def giris(self):

        musteriNo = self.musteriNoEntry.get()#musteriNo alınır.
        sifreNo = self.sifreEntry.get()#şifre alnır.

        if not musteriNo:
            showwarning("Uyarı","Lütfen MÜŞTERİ NUMARANIZI giriniz.")
            return False

        if not sifreNo:
            showwarning("Uyarı","Lütfen ŞİFRENİZİ giriniz.")
            return False

        vti = VeritabaniIslemleri.VeritabaniIslemleri()
        self.musteriBilgisi = vti.musteriBilgisiAl(musteriNo)#liste içinde tek bir tuple olacaktır.

        if self.musteriBilgisi == []:
            #Müşteri numarası yanlışsa buradaki mesaj gösterilir.
            showerror("Hata","Girilen bilgiler geçersizdir.\nLütfen Bilgilerinizi kontrol ediniz.")
        elif self.musteriBilgisi == False:
            pass               #Buraya girdiyse veritabanında sıkıntı var demektir.
        elif sifreNo == self.musteriBilgisi[0][4]:
            self.girisPenceresi.destroy()
            self.anaPencereEkrani()
        else:
            #Şifre yanlışsa buradaki mesaj gösterilir.
            showwarning("Uyarı","Girdiğiniz bilgiler yanlış!\nTekrar deneyiniz!")

    def hakkimda(self):
        showinfo("Hakkımda","Saffet Murat tarafından yapıldı\n(Created by: Saffet Murat)\n\n{}\n\n{}".format("https://trmsma.wordpress.com","https://github.com/saffetmurat"))

    def girisEkrani(self):
        self.girisPenceresi = Tk()
        self.girisPenceresi.title("Bankamatik Uygulaması - Giriş Ekranı")
        self.girisPenceresi.geometry("500x80+400+400")
        self.girisPenceresi.resizable(width=FALSE, height=FALSE)

        aciklamaLabel = Label(self.girisPenceresi,text="Merhabalar,")

        musteriLabel = Label(self.girisPenceresi, text="Müşteri Numaranızı giriniz :")
        self.musteriNoEntry = Entry(self.girisPenceresi)

        kartLabel = Label(self.girisPenceresi, text="Şifrenizi giriniz :")
        self.sifreEntry = Entry(self.girisPenceresi)

        onayButton = Button(self.girisPenceresi, text = "Giriş Yap", font="6", width=19, command =self.giris)
        hakkimdaButton = Button(self.girisPenceresi, text = "Hakkımda", width=20, command =self.hakkimda)
        
        aciklamaLabel.place(relx=0.01, rely=0.05)

        musteriLabel.place(relx=0.05, rely=0.3)
        self.musteriNoEntry.place(relx=0.36, rely=0.3)

        kartLabel.place(relx=0.05, rely=0.65)
        self.sifreEntry.place(relx=0.36, rely=0.65)

        onayButton.place(relx=0.62, rely=0.18)
        hakkimdaButton.place(relx=0.65, rely=0.6)

        self.girisPenceresi.mainloop()

if __name__ == "__main__":
    bnkmtk = Bankamatik()