from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import datetime
import time
import locale
import pytz

class Zaman():

    #değişkenler
    __anaPencere = ""
    __dilAyari = "" #boş olması sistemin yerel dilini al demektir.
                    #kullanılan dili göstermektedir
    __gosterimSekli = "%d %B %Y %A %X"#zamanın gösterim şekli belirleniyor.
                      #gösterim şekli standart olarak belirlendi.
    __hafizaZaman = datetime.timedelta(days=0, weeks=0, hours=0, minutes=0, seconds= 0)
                    #sitemin çalışmasından itibaren geçerli olan toplam zaman farkını tutacak
    __kullanilanUTC = "Sistemin yerel UTC'ini kullan"
    __degistirilenUTC = "Sistemin yerel UTC'ini kullan"
    __dosya = open("TkinterTimeApplication_ErrorFile.txt","w+")

    def __init__(self):
        try:
            #Saat için dil belirlenir.
            locale.setlocale(locale.LC_ALL, self.__dilAyari)

            self.anaPencereYap()
            self.anaPencereNesneleri()
            self.calistir()
          
            self.__anaPencere.mainloop()

        except Exception as hata:
            print("Sistem yerel zamanına göre => {} => {}".format(datetime.datetime.now(),hata), file = self.__dosya)

    #Pencere oluşturup başlangıç özelliklerini belirliyor.
    def anaPencereYap(self):

        self.__anaPencere = Tk()
        self.__anaPencere.title("Tkinter Zaman Uygulaması (Tkinter Time Application)")
        self.__anaPencere.geometry("600x90+200+300")
        self.__anaPencere.resizable(width=FALSE,height=FALSE)


    #pencere üzerine koyulacaklar belirleniyor.
    def anaPencereNesneleri(self):

        #zamanı gösteren Label
        self.etiketZaman = Label(self.__anaPencere, font = "Times 15")

        menu1 = Menu(self.__anaPencere)
        self.__anaPencere.config( menu = menu1 )
        
        menuAyarlar = Menu(menu1,tearoff = 0)
        menu1.add_cascade(label = "Ayarlar", menu = menuAyarlar)
        menuAyarlar.add_command(label = "Dil Ayarı", command = self.dilAyari)
        menuAyarlar.add_command(label = "Zaman Ayarı", command = self.zamanAyari)
        menuAyarlar.add_command(label = "Gösterim Ayarı", command = self.gosterimAyari)
        menuAyarlar.add_command(label = "Standart Ayarlara Dön", command = self.standartAyarlar)

        menuYardim = Menu(menu1,tearoff = 0)
        menu1.add_cascade(label = "Yardım", menu = menuYardim)
        menuYardim.add_command(label = "Hakkımda", command = self.hakkimda)
        menuYardim.add_command(label = "Açıklamalar", command = self.acikla)

        self.etiketZaman.place(relx=0.3,rely=0.30)

    def hakkimda(self):
        showinfo("Hakkımda","Saffet Murat tarafından yapıldı\n(Created by: Saffet Murat)\n\n{}\n\n{}".format("https://trmsma.wordpress.com","https://github.com/saffetmurat"))

    def acikla(self):
        aciklamaMetni = """    Tercih ettiğin dilde tercih ettiğin gösterimde,
zamanı gösteren bir uygulamadır. Ayrıca zamanı ayarlama özelliği de bulunmaktadır.
    Karşılaşılan hataları, oluşturacağı TkinterTimeApplication_ErrorFile.txt dosyasına yazmaktadır."""
        showinfo("Açıklamalar", aciklamaMetni)

    def standartAyarlar(self):

        self.__dilAyari = ""
        locale.setlocale(locale.LC_ALL, self.__dilAyari)
        self.__gosterimSekli = "%d %B %Y %A %X"
        self.__hafizaZaman = datetime.timedelta(days=0, weeks=0, hours=0, minutes=0, seconds= 0)
        self.__kullanilanUTC = "Sistemin yerel UTC'ini kullan"
        self.__degistirilenUTC = "Sistemin yerel UTC'ini kullan"

        showinfo("Bilgilendirme",'Standart Ayarlara Dönüldü!')
  
    def dilAyari(self):

        #yeni bir pencere oluşturulur.
        self.pencere = Tk()
        self.pencere.title("Uygulamanın Dil Ayar Penceresi")
        self.pencere.geometry("375x50+200+215")
        self.pencere.resizable(width=FALSE,height=FALSE)

        etiketDil = Label(self.pencere, text = "Bir dil seçiniz =>")

        self.seceneklerDil={
            "Sistem Dili" : "",
            "Türkçe" : "turkish",
            "İtalyanca" : "italian",
            "İngilizce" : "english",
            "Fransızca" : "french",
            "Almanca" : "german",
            "İspanyolca" : "spanish"
        }

        self.comboDiller=ttk.Combobox(self.pencere, state = 'readonly', values = [*self.seceneklerDil.keys()])
        ######################################################
        #kullanılan seçeneğin aktif olarak gösterilmesi için
        indeks = 0
        for anahtar, deger in self.seceneklerDil.items():
            if deger == self.__dilAyari:
                self.comboDiller.current(indeks)
                break
            indeks += 1
        ######################################################

        #Onaylarsa Zamanın dil ayarı değiştirilecek
        buttonOnay = Button(self.pencere, text = "Değişiklikleri Onayla",command = self.dilUygula)
        
        etiketDil.grid(row=0, column=0, pady=12, padx=2 )
        self.comboDiller.grid(row=0, column=1, pady=12, padx=2 )
        buttonOnay.grid(row=0, column=2, pady=12, padx=5 )

        self.pencere.mainloop()

    def dilUygula(self):

        #__dilAyari sözlüğün değerini tutacak. Ör: turkish
        self.__dilAyari = self.seceneklerDil[self.comboDiller.get()]
        locale.setlocale(locale.LC_ALL, self.__dilAyari)
        showinfo("Bilgilendirme","Saatin dil ayarı \'{}\' olarak değiştirildi !".format(self.comboDiller.get()))

        self.pencere.destroy()

    def gosterimAyari(self):

        #yeni bir pencere oluşturulur.
        self.pencere1 = Tk()
        self.pencere1.title("Uygulamanın Zaman Gösterme Ayar Penceresi")
        self.pencere1.geometry("465x50+200+215")
        self.pencere1.resizable(width=FALSE,height=FALSE)

        etiketGosterim = Label(self.pencere1, text = "Bir gösterim şekli seçiniz =>")

        self.seceneklerGosterim= {
            datetime.datetime.strftime(self.an,"%c") : "%c",# tam tarih, saat ve zaman bilgisi gösterilecektir.
                                                            # 19.10.2019 21:15:38 şeklinde (gün.ay.yıl saat:dakika:saniye)
            datetime.datetime.strftime(self.an,"%x") : "%x", # tam tarih bilgisi gösterilecektir. 
                                                            #19.10.2019 şeklinde (gün.ay.yıl)
            datetime.datetime.strftime(self.an,"%X") : "%X", # tam saat bilgisi gösterilecektir. 
                                                            #10:15:13 şeklinde (saat:dakika:saniye)
            datetime.datetime.strftime(self.an,"%d %B %Y") : "%d %B %Y", # tam tarih bilisi gösterilecektir.
                                                                        #19 Kasım 2019 şeklinde (gün ay yıl)
            datetime.datetime.strftime(self.an,"%d %B %Y %X") : "%d %B %Y %X",# tam tarih, saat ve zaman bilgisi gösterilecektir.
                                                                            # 19 Kasım 2019 21:15:38 şeklinde (gün ay yıl saat:dakika:saniye)            
            datetime.datetime.strftime(self.an,"%d %b %Y") : "%d %b %Y", # tam tarih bilisi gösterilecektir.
                                                                        #19 Kas 2019 şeklinde (gün ay yıl)
            datetime.datetime.strftime(self.an,"%d %b %Y %X") : "%d %b %Y %X",# tam tarih, saat ve zaman bilgisi gösterilecektir.
                                                                            # 19 Kas 2019 21:15:38 şeklinde (gün ay yıl gün saat:dakika:saniye)            
            datetime.datetime.strftime(self.an,"%d %B %Y %A") : "%d %B %Y %A", # tam tarih bilisi gösterilecektir.
                                                                        #19 Kasım 2019 Salı şeklinde (gün ay yıl gün)
            datetime.datetime.strftime(self.an,"%d %B %Y %A %X") : "%d %B %Y %A %X",# tam tarih, saat ve zaman bilgisi gösterilecektir.
                                                                            # 19 Kasım 2019 Salı 21:15:38 şeklinde (gün ay yıl gün saat:dakika:saniye)            
            datetime.datetime.strftime(self.an,"%d %b %Y %A") : "%d %b %Y %A", # tam tarih bilisi gösterilecektir.
                                                                        #19 Kas 2019 Salı şeklinde (gün ay yıl gün)
            datetime.datetime.strftime(self.an,"%d %b %Y %A %X") : "%d %b %Y %A %X",# tam tarih, saat ve zaman bilgisi gösterilecektir.
                                                                            # 19 Kas 2019 Salı 21:15:38 şeklinde (gün ay yıl gün saat:dakika:saniye)            
            datetime.datetime.strftime(self.an,"%d %B %A") : "%d %B %A", # tam tarih bilisi gösterilecektir.
                                                                        #19 Kasım Salı şeklinde (gün ay gün)
            datetime.datetime.strftime(self.an,"%d %B %A %X") : "%d %B %A %X",# tam tarih, saat ve zaman bilgisi gösterilecektir.
                                                                            # 19 Kasım Salı 21:15:38 şeklinde (gün ay gün saat:dakika:saniye)            
            datetime.datetime.strftime(self.an,"%x %H:%M") : "%x %H:%M",  # tam tarih, saat ve dakika bilgisi gösterilecektir.
                                                                    # 19.10.2019 21:15 şeklinde (gün.ay.yıl saat:dakika)            
            datetime.datetime.strftime(self.an,"%x %A %X") : "%x %A %X"  # tam tarih, gün, saat ve dakika bilgisi gösterilecektir.
                                                                    # 19.10.2019 Salı 21:15 şeklinde (gün.ay.yıl gün saat:dakika:saniye)              
        }

        self.comboSekiller=ttk.Combobox(self.pencere1, state='readonly', values=[*self.seceneklerGosterim.keys()])

        ######################################################
        #kullanılan seçeneğin aktif olarak gösterilmesi için
        indeks = 0
        for anahtar, deger in self.seceneklerGosterim.items():
            if deger == self.__gosterimSekli:
                self.comboSekiller.current(indeks)
                break
            indeks += 1
        ######################################################

        buttonOnay = Button(self.pencere1, text = "Değişiklikleri Onayla",command = self.gosterimUygula)
        
        etiketGosterim.grid(row=0, column=0, pady=12, padx=5 )
        self.comboSekiller.grid(row=0, column=1, pady=12, ipadx=12 )
        buttonOnay.grid(row=0, column=2, pady=12, padx=8 )

        self.pencere1.mainloop()

    def gosterimUygula(self):

        #__gosterimSekli sözlüğün değerini tutacak. Ör: "%c"
        self.__gosterimSekli = self.seceneklerGosterim[self.comboSekiller.get()]
        self.etiketZaman.config(text=self.__gosterimSekli)
        showinfo("Bilgilendirme","Zaman gösterimi \"{}\" olarak değiştirildi !".format(self.comboSekiller.get()))

        self.pencere1.destroy()

    def zamanAyari(self):

        aciklamaMetni = """Açıklamalar=>
    Burada çeşitli seçenekler seçilerek zamanın değişmesi sağlanabilir.
Örneğin 2 gün 3 saat ileri, 15 dakika geri gidildiğinde oluşan zamanın
üzerinden zaman gösterilmektedir.
    Ayrıca seçilen UTC tipine göre de zaman değişmektedir.
        """
        self.pencere2 = Tk()
        self.pencere2.title("Uygulamanın Zaman Ayar Penceresi")
        self.pencere2.geometry("465x400+200+215")
        self.pencere2.resizable(width=FALSE,height=FALSE)

        
        etiketZaman = Label(self.pencere2,text = "Zamanı =>", font = "Times 15")
        etiketHafta = Label(self.pencere2, text = " hafta kadar  ", font = " 12")
        etiketGun = Label(self.pencere2,text=" gün kadar ", font = " 12")
        etiketSaat = Label(self.pencere2, text = " saat kadar ", font = " 12")
        etiketDakika = Label(self.pencere2, text = " dakika kadar ", font = " 12")
        etiketSaniye = Label(self.pencere2, text = " saniye kadar ", font = " 12")
        etiketAciklama = Label(self.pencere2, text = aciklamaMetni, justify=LEFT)

        self.secenekZaman=[]
        self.secenekZaman.append( [i for i in range(0,53)] )#hafta eklenir.
        self.secenekZaman.append( [i for i in range(0,366)] )#gün eklenir.
        self.secenekZaman.append( [i for i in range(0,25)] )#saat eklenir.
        self.secenekZaman.append( [i for i in range(0,61)] )#dakika eklenir.
        self.secenekZaman.append( [i for i in range(0,61)] )#saniye eklenir.

        durum=['ileri al','geri al']

        self.comboHafta = ttk.Combobox(self.pencere2, state='readonly', values = self.secenekZaman[0])
        self.comboHafta.current(0)#burada her zaman 0.indeks seçili olacak

        self.comboHaftaDurum = ttk.Combobox(self.pencere2, state='readonly', values=durum)
        self.comboHaftaDurum.current(0)

        self.comboGun = ttk.Combobox(self.pencere2, state='readonly', values=self.secenekZaman[1])
        self.comboGun.current(0)

        self.comboGunDurum = ttk.Combobox(self.pencere2, state='readonly', values=durum)
        self.comboGunDurum.current(0)

        self.comboSaat = ttk.Combobox(self.pencere2, state='readonly', values=self.secenekZaman[2])
        self.comboSaat.current(0)

        self.comboSaatDurum = ttk.Combobox(self.pencere2, state='readonly', values=durum)
        self.comboSaatDurum.current(0)

        self.comboDakika = ttk.Combobox(self.pencere2, state='readonly', values=self.secenekZaman[3])
        self.comboDakika.current(0)

        self.comboDakikaDurum = ttk.Combobox(self.pencere2, state='readonly', values=durum)
        self.comboDakikaDurum.current(0)

        self.comboSaniye = ttk.Combobox(self.pencere2, state='readonly', values=self.secenekZaman[4])
        self.comboSaniye.current(0)

        self.comboSaniyeDurum=ttk.Combobox(self.pencere2, state='readonly', values=durum)
        self.comboSaniyeDurum.current(0)
    
        UTCler = ["Sistemin yerel UTC'ini kullan"]
        for utc in pytz.all_timezones:
            UTCler.append(utc)
    
        etiketUTC = Label(self.pencere2, text="İstediğiniz UTC tipini seçiniz =>")
        self.comboUtc=ttk.Combobox(self.pencere2, state='readonly', values=UTCler)

        #kullanılan seçeneğin aktif olarak gösterilmesi için
        for deger in UTCler:
            if deger == self.__kullanilanUTC:
                self.comboUtc.current(UTCler.index(deger))
                break
        ######################################################

        buttonOnay = Button(self.pencere2, text = "Değişiklikleri Onayla",font = "10", command = self.zamanAyarUygula)
        
        etiketZaman.place(relx=0.005, rely=0.005)

        self.comboHafta.place(relx=0.05, rely=0.09)
        etiketHafta.place(relx=0.38, rely=0.085)
        self.comboHaftaDurum.place(relx=0.6, rely=0.09)
    

        self.comboGun.place(relx=0.05, rely=0.19)
        etiketGun.place(relx=0.38, rely=0.185)
        self.comboGunDurum.place(relx=0.6, rely=0.19)

        self.comboSaat.place(relx=0.05, rely=0.29)
        etiketSaat.place(relx=0.38, rely=0.285)
        self.comboSaatDurum.place(relx=0.6, rely=0.29)

        self.comboDakika.place(relx=0.05, rely=0.39)        
        etiketDakika.place(relx=0.37, rely=0.385)
        self.comboDakikaDurum.place(relx=0.6, rely=0.39)

        self.comboSaniye.place(relx=0.05, rely=0.49)     
        etiketSaniye.place(relx=0.37, rely=0.485)
        self.comboSaniyeDurum.place(relx=0.6, rely=0.49)

        etiketUTC.place(relx=0.039, rely=0.59)
        self.comboUtc.place(relx=0.419, rely=0.588, width=230)

        buttonOnay.place(relx=0.32, rely=0.69)

        etiketAciklama.place(relx=0.039, rely=0.78)

        self.pencere2.mainloop()

    def zamanAyarUygula(self):

        seceneklerI={
            "days": 0,
            "weeks": 0,
            "hours": 0,
            "minutes": 0,
            "seconds": 0
        }
        seceneklerG={
            "days": 0,
            "weeks": 0,
            "hours": 0,
            "minutes": 0,
            "seconds": 0
        }

        if self.comboHaftaDurum.get() == 'ileri al':
            seceneklerI[ "weeks"] = int(self.comboHafta.get())
        else:
            seceneklerG[ "weeks"] = int(self.comboHafta.get())

        if self.comboGunDurum.get() == 'ileri al':
            seceneklerI[ "days"] = int(self.comboGun.get())
        else:
            seceneklerG[ "days"] = int(self.comboGun.get())  

        if self.comboSaatDurum.get() == 'ileri al':
            seceneklerI[ "hours"] = int(self.comboSaat.get())
        else:
            seceneklerG[ "hours"] = int(self.comboSaat.get())

        if self.comboDakikaDurum.get() == 'ileri al':
            seceneklerI[ "minutes"] = int(self.comboDakika.get())
        else:
            seceneklerG[ "minutes"] = int(self.comboDakika.get())

        if self.comboSaniyeDurum.get() == 'ileri al':
            seceneklerI[ "seconds"] = int(self.comboSaniye.get())
        else:
            seceneklerG[ "seconds"] = int(self.comboSaniye.get())



        yeniZamanIleri=datetime.timedelta(days=seceneklerI[ "days"], weeks=seceneklerI[ "weeks"], hours=seceneklerI[ "hours"], minutes=seceneklerI[ "minutes"], seconds= seceneklerI[ "seconds"])
        yeniZamanGeri = datetime.timedelta(days=seceneklerG[ "days"], weeks=seceneklerG[ "weeks"], hours=seceneklerG[ "hours"], minutes=seceneklerG[ "minutes"], seconds= seceneklerG[ "seconds"])

        self.__hafizaZaman = self.__hafizaZaman + (yeniZamanIleri - yeniZamanGeri)

        self.__degistirilenUTC = self.comboUtc.get()

        #showinfo("Bilgilendirme","Yaptığınız Zaman ayarlamaları sisteme uygulandı !")

        self.pencere2.destroy()

    ##########################################################################################################

    def calistir(self):

        self.an= datetime.datetime.now()

        if self.__degistirilenUTC == "Sistemin yerel UTC'ini kullan":
            self.__kullanilanUTC = self.__degistirilenUTC

        elif self.__kullanilanUTC != self.__degistirilenUTC:
            self.__kullanilanUTC = self.__degistirilenUTC
            utc = self.an.astimezone(pytz.timezone(self.__kullanilanUTC))
            self.an=utc

        else:
            utc = self.an.astimezone(pytz.timezone(self.__kullanilanUTC))
            self.an=utc

        self.an = self.an + self.__hafizaZaman

        zaman=datetime.datetime.strftime(self.an,self.__gosterimSekli)

        self.etiketZaman.config(text=zaman)
        self.etiketZaman.after(60,self.calistir)#her bir saniyede değişkeni calistir fonksiyonuyla güncelletiyoruz. 60 burada milisaniyeyi temsil eder.


if __name__ == "__main__":
    zmn = Zaman()