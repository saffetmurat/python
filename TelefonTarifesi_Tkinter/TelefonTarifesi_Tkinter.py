from tkinter import *
from tkinter.messagebox import *
import os

class TelefonTarifesi():
    __tarifeBilgisiAciklamasi = """
=================================================================================
                        TARİFE DETAYLARI
Tarifenin Adı                         : {}
Tarifenin Sunduğu Konuşma Süresi      : {} Dk.
Tarifenin Sunduğu Mesaj Adeti         : {} SMS
Tarifenin Sunduğu İnternet Paketi     : {} MB ({} GB)

Bu tarifede;
1) İnternet Bittiğinde Uygulanacak Ücretlendirme     Her {} MB için {} TL'dir
2) Dakikalar Bittiğinde Uygulanacak Ücretlendirme    {} Kr/Dk
3) SMS'ler Bittiğinde Uygulanacak Ücretlendirme      {} Kr/SMS
_________________________________________________________________________________
AYLIK TARİFE TUTARINIZ                 : {} TL"""

    __tarifeBilgileri = []

    def __init__(self, adres = os.getcwd() + os.sep + "tarifeDetaylari.csv"):
        self.adres = adres

    def dosyaAc(self, kip = "r"):
        if os.path.exists(self.adres):
            dosya = open(self.adres, kip)
            return dosya
        else:
            showerror("Hata", "Veritabanı bulunamıyor.")
            return False

    def tarifeBilgileriniAl(self):
        dsy = self.dosyaAc()
        icerikler = dsy.readlines()#dosyanın içeriği okundu.

        gecici = []
        for tarife in icerikler:
            for indeks in range(len(tarife.split(";"))):#her bir satırdaki ; ile ayrılmış elemanların sayısı bulunur.
                gecici.append(tarife.split(";")[indeks].strip("\n"))
            self.__tarifeBilgileri.append(gecici)
            gecici = []

        dsy.close()

    def tarifeSecimi(self):
        tarifeIndeksi = self.secimTarifeTuru.get()
        self.textAciklama.config(state = NORMAL)
        self.textAciklama.delete("0.0",END)#İçerik temizlenir.
        self.textAciklama.insert(END, self.__tarifeBilgisiAciklamasi.format(self.__tarifeBilgileri[tarifeIndeksi][0], self.__tarifeBilgileri[tarifeIndeksi][1],self.__tarifeBilgileri[tarifeIndeksi][2],self.__tarifeBilgileri[tarifeIndeksi][3],self.__tarifeBilgileri[tarifeIndeksi][4],self.__tarifeBilgileri[tarifeIndeksi][5],self.__tarifeBilgileri[tarifeIndeksi][6],self.__tarifeBilgileri[tarifeIndeksi][7],self.__tarifeBilgileri[tarifeIndeksi][8],self.__tarifeBilgileri[tarifeIndeksi][9]))
        self.textAciklama.config(state = DISABLED)

    def hakkimda(self):
        showinfo("Hakkımda","Saffet Murat tarafından yapıldı\n(Created by: Saffet Murat)\n\n{}\n\n{}".format("https://trmsma.wordpress.com","https://github.com/saffetmurat"))

    def anaPencereYapma(self):
        try:
            anaPencere = Tk()
            anaPencere.title("Tarife Sorgulama Ekranı")
            anaPencere.geometry("684x500+100+100")
            anaPencere.resizable(width = False, height = False)

            menu1 = Menu(anaPencere)
            anaPencere.config(menu = menu1)

            menuTarifeler = Menu(menu1, tearoff = 0)
            menu1.add_cascade(label = "Tarife Seçiniz", menu = menuTarifeler)

            self.tarifeBilgileriniAl()

            self.secimTarifeTuru = IntVar()

            for indeks in range(len(self.__tarifeBilgileri)):
                menuTarifeler.add_radiobutton(label = "{}".format(self.__tarifeBilgileri[indeks][0]), value=indeks, variable=self.secimTarifeTuru, command = self.tarifeSecimi)

            menuAciklamalar = Menu(menu1, tearoff = 0)
            menu1.add_cascade(label = "Açıklamalar", menu = menuAciklamalar)
            menuAciklamalar.add_command(label = "Hakkımda", command = self.hakkimda)

            self.textAciklama = Text(anaPencere, width = 83, height = 15)
            self.textAciklama.insert(END, self.__tarifeBilgisiAciklamasi.format(self.__tarifeBilgileri[0][0], self.__tarifeBilgileri[0][1],self.__tarifeBilgileri[0][2],self.__tarifeBilgileri[0][3],self.__tarifeBilgileri[0][4],self.__tarifeBilgileri[0][5],self.__tarifeBilgileri[0][6],self.__tarifeBilgileri[0][7],self.__tarifeBilgileri[0][8],self.__tarifeBilgileri[0][9]))

            self.textAciklama.config(state = DISABLED)

            etiketAciklama = Label(anaPencere, text = "Bu tarifeye göre tahmini faturanızı hesaplayalım :)", font = "Times 14")

            etiketDK = Label(anaPencere, text = "Tahmini aylık konuşma sürenizi (dakika olarak) giriniz = ", font = "Times 14")
            self.entryDK = Entry(anaPencere, font = "Times 12")

            etiketSMS = Label(anaPencere, text = "Tahmini aylık kullandığınız SMS adetini giriniz = ", font = "Times 14")
            self.entrySMS = Entry(anaPencere, font = "Times 12")
    
            etiketINTER = Label(anaPencere, text = "Tahmini aylık tükettiğiniz internet miktarını (MB olarak) giriniz = ", font = "Times 14")
            self.entryINTER = Entry(anaPencere, font = "Times 12")

            butonHesaplama = Button(anaPencere, text = "Tahmini Faturayı Hesapla", bg = "SkyBlue1", font = "Times 12", command = self.hesaplama)

            self.textAciklama.place(relx=0.01,rely=0.01)

            etiketAciklama.place(relx=0.01, rely=0.53)

            etiketDK.place(relx=0.01, rely=0.6)
            self.entryDK.place(relx=0.72, rely=0.6)

            etiketSMS.place(relx=0.01, rely=0.7)
            self.entrySMS.place(relx=0.72, rely=0.7)

            etiketINTER.place(relx=0.01, rely=0.8)
            self.entryINTER.place(relx=0.72, rely=0.8)

            butonHesaplama.place(relx=0.35, rely=0.885)

            anaPencere.mainloop()

        except:
            pass

    def kontroller(self):
        dk = self.entryDK.get()
        sms = self.entrySMS.get()
        internet = self.entryINTER.get()

        mesajlar = []
        if dk == "":
            mesajlar.append("Dakika bilgisini boş geçemezsiniz. Gerekirse 0 koyun.")
        elif not dk.isdigit():
            mesajlar.append("Lütfen Dakika bilgisini pozitif bir tamsayı olarak girin!")
        
        if sms == "":
            mesajlar.append("SMS bilgisini boş geçemezsiniz. Gerekirse 0 koyun.")
        elif not sms.isdigit():
            mesajlar.append("Lütfen SMS bilgisini pozitif bir tamsayı olarak girin!")

        if internet == "":
            mesajlar.append("İnternet bilgisini boş geçemezsiniz. Gerekirse 0 koyun.")
        elif not internet.isdigit():
            mesajlar.append("Lütfen İnternet bilgisini pozitif bir tamsayı olarak girin!")

        if mesajlar:#Doluysa if'e girer. Dolu olması hataların olduğu anlamına gelir.
            yazi = "Bulunan Hatalar =>\n"
            for indeks in range(len(mesajlar)):
                yazi += (str(indeks + 1)) + "- " + mesajlar[indeks] + "\n"

            showerror("HATA",yazi)
            return True
        else:
            return False

    def hesaplama(self):
        if self.kontroller():#True gelirse hata var demektir. Bu durumda fonksiyon çalıştırılmaz.
            return False
        
        dk = int(self.entryDK.get())
        sms = int(self.entrySMS.get())
        internet = int(self.entryINTER.get())

        tarifeIndeksi = self.secimTarifeTuru.get()

        tutarToplam = float(self.__tarifeBilgileri[tarifeIndeksi][9])
        ekUcret = 0

        aciklamalar = ""
        if dk > int(self.__tarifeBilgileri[tarifeIndeksi][1]):
            ekUcret = (dk-int(self.__tarifeBilgileri[tarifeIndeksi][1])) * (float(self.__tarifeBilgileri[tarifeIndeksi][7])/100)
            #(self.__tarifeBilgileri[tarifeIndeksi][7]//100) bu ifade ile kuruş TL'ye çevrilir.
            tutarToplam += ekUcret
            aciklamalar += "Konuşma için tarifeden aşılan süre = {} dakika\nEK ÜCRET = {} TL\n\n".format((dk-int(self.__tarifeBilgileri[tarifeIndeksi][1])), ekUcret)

        if sms > int(self.__tarifeBilgileri[tarifeIndeksi][2]):
            ekUcret = (sms-int(self.__tarifeBilgileri[tarifeIndeksi][2])) * (float(self.__tarifeBilgileri[tarifeIndeksi][8])/100)
            #(self.__tarifeBilgileri[tarifeIndeksi][8]//100) bu ifade ile kuruş TL'ye çevrilir.
            tutarToplam += ekUcret
            aciklamalar += "SMS için tarifeden aşılan adet = {} SMS\nEK ÜCRET = {} TL\n\n".format((sms-int(self.__tarifeBilgileri[tarifeIndeksi][2])), ekUcret)

        if internet > int(self.__tarifeBilgileri[tarifeIndeksi][3]):   
            ekUcret = ((internet - int(self.__tarifeBilgileri[tarifeIndeksi][3])) // float(self.__tarifeBilgileri[tarifeIndeksi][5])) * float(self.__tarifeBilgileri[tarifeIndeksi][6])
            tutarToplam += ekUcret
            aciklamalar += "İnternet için tarifeden aşılan miktar= {} MB\nEK ÜCRET = {} TL\n\n".format((internet - int(self.__tarifeBilgileri[tarifeIndeksi][3])), ekUcret)

        if tutarToplam == float(self.__tarifeBilgileri[tarifeIndeksi][9]):
            aciklamalar = "BU KULLANIMLA TARİFENİZDE HERHANGİ BİR AŞIM OLMAZ\n\n"

        aciklamalar += "TAHMİNİ TOPLAM FATURA TUTARINIZ : {} TL".format(tutarToplam)

        showinfo("Bilgilendirme", aciklamalar)

if __name__ == "__main__":
    tt = TelefonTarifesi()
    tt.anaPencereYapma()