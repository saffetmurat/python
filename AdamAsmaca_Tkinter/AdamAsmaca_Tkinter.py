import os
import random
from tkinter import *
from tkinter.messagebox import *

class AdamOyun():

    __kelimeler = []
    __font = "Times 15"

    __sayac=0

    __adamDurumu = ["""
       +-----+
       |        |
                |
                |
    _____  |
     |     |     |
    =========""", """
       +-----+
       |        |
      O       |
                |
    _____  |
     |     |     |
    =========""", """
       +-----+
       |        |
      O       |
       |        |
    _____  |
     |     |     |
    =========""", """
       +-----+
       |        |
      O       |
      /|        |
    _____  |
     |     |     |
    =========""", """
       +-----+
       |        |
      O       |
      /|\       |
    _____  |
     |     |     |
    =========""", """
       +-----+
       |        |
      O       |
      /|\       |
    _/___   |
     |     |     |
    =========""", """
       +-----+
       |        |
      O       |
      /|\       |
   _/_\_     |
     |     |     |
    =========""", """
       +-----+
       |        |
      O       |
      /|\       |
   _/_\_     |
     |     \     |
    =========""", """
       +-----+
       |        |
      O       |
      /|\       |
   _/_\_     |
     /     \     |
    =========""", """
       +-----+
       |        |
      O       |
      /|\       |
   _/_\      |
     /     _  |
    =========""", """
       +-----+
       |        |
      O       |
      /|\       |
    _/ \       |
     /   _ _  |
    =========""", """
       +-----+
       |        |
      O       |
      /|\       |
      / \       |
     ___     |
    =========""",]

    def __init__(self, dosyaAdi):
        
        self.dosyaAdi = dosyaAdi #Kelimelerin bulunduğu dosyanın adı alınıyor.
        self.anaPencereYap()
        self.kelimeAyarla()        
        self.anaPencereNesneleri()

        self.anaPencere.mainloop() 

    def dosyaAc(self):
        try:
            dsy = open( os.getcwd() + os.sep + self.dosyaAdi, "r" )
            return dsy
        except:
            return False

    def anaPencereYap(self):
        self.anaPencere = Tk()
        self.anaPencere.title("Tkinter Adam Asmaca Oyunu (Tkinter Hangman Game)")
        self.anaPencere.geometry("600x300+200+200")
        self.anaPencere.resizable(width=False, height=FALSE)

        dsy = self.dosyaAc()

        if dsy:#Dosya açılırsa kelimeleri dosyadan alıp listeye aktaracak
            for kelime in dsy:
                self.__kelimeler.append(kelime)
        else:
            showerror("Hata", "Kelimelerin bulunduğu {} dosyası bulunamıyor :(\n Bu yüzden oyun kapatılıyor.".format(self.dosyaAdi))
            self.anaPencere.destroy()
    
    def anaPencereNesneleri(self):

        menu1 = Menu(self.anaPencere)
        self.anaPencere.config( menu = menu1 )

        menuSecenekler = Menu(menu1, tearoff = 0)
        menu1.add_cascade(label = "Seçenekler", menu = menuSecenekler)
        menuSecenekler.add_command(label = "Ekranı Temizle", command = self.ekranTemizle)
        menuSecenekler.add_command(label = "İpucu Al", command = self.ipucuAl)
        menuSecenekler.add_command(label = "Yeni Oyun", command = self.yeniOyun)
        menuSecenekler.add_command(label = "Dosya Yükle", command = self.dosyaYukle)

        menuBilgilendirme=Menu(menu1,tearoff = 0)
        menu1.add_cascade(label="Bilgilendirme", menu = menuBilgilendirme)
        menuBilgilendirme.add_command(label= "Açıklamalar", command=self.acikla)
        menuBilgilendirme.add_command(label= "Hakkımda", command=self.hakkimda)

        self.etiketAdam = Label(self.anaPencere, text = self.__adamDurumu[self.__sayac], font = "Times 17")
        etiketAciklama = Label(self.anaPencere,text="Kelimeyi aşağıdaki\nkutucuğa yazınız", font = "Times 13")

        self.girisKullanici = Entry()

        buttonOnay = Button(self.anaPencere,text="Kararı Onayla", command = self.degerlendir, font = self.__font)

        self.listBoxDurum = Listbox(self.anaPencere, width = 47, height = 17)
        

        self.etiketAdam.place(relx=0.005,rely=0.2)

        etiketAciklama.place(relx=0.28,rely=0.05)
        self.girisKullanici.place(relx=0.28,rely=0.25)
        buttonOnay.place(relx=0.28,rely=0.35)

        self.listBoxDurum.place(relx=0.52,rely=0.05)

    def ekranTemizle(self):
        self.girisKullanici.delete(0,END)
        self.listBoxDurum.delete(0,END)

    def ipucuAl(self):
        showinfo("İpucu","Sadece bir ipucu verilebilir\n\nİlk harfi {}".format(self.__kelimeler[self.indeks].strip("\n")[0]))

    def yeniOyun(self):
        self.kelimeAyarla()
        self.ekranTemizle()
        self.__sayac=0
        self.etiketAdam["text"] = self.__adamDurumu[self.__sayac]

    def kelimeAyarla(self):
        self.indeks=random.randrange(len(self.__kelimeler))

    def hakkimda(self):
        showinfo("Hakkımda","Saffet Murat tarafından yapıldı\n(Created by: Saffet Murat)\n\n{}\n\n{}".format("https://trmsma.wordpress.com","https://github.com/saffetmurat"))

    def acikla(self):
        aciklamaMetni = """    Adam Asmaca Oyunu(Hangman Game), dosyadan aldığı kelimeler arasından rastgele bir tanesini seçer.
    Varsayılan olarak çalışma dizininde bulunan iller.csv dosyasındaki illeri alır. Yani varsayılan olarak bu oyunda illerden birini bulmanı istiyor.
    İstersen iller.csv dosyası yerine çalışma dizinine koyacağın başka bir csv türündeki dosyadan kelimeleri çekip bunlardan birini sana sorabilir.
    Bunun için dosyanın adını uzantısıyla birlikte vermen yeterlidir.
    Oyun büyük-küçük harflere karşı duyarlıdır."""
        showinfo("Açıklamalar", aciklamaMetni)

    def dosyaYukle(self):
        self.pencere = Tk()
        self.pencere.title("Adam Asmaca Oyunu(Hangman Game) Dosya Yükleme Kısmı")
        self.pencere.geometry("600x50+200+200")
        self.pencere.resizable(width=FALSE,height=FALSE)

        etiketDosyaAd = Label(self.pencere, text = "Yükleyeceğiniz Dosyanın Adını Uzantısıyla giriniz =>")
        
        self.girisDosya = Entry(self.pencere, width = 20)

        buttonYukle = Button(self.pencere, text = "Dosyayı Yükle", width = 30, command = self.dosyaAlma)

        etiketDosyaAd.pack(side = LEFT, padx=11)
        self.girisDosya.pack(side = LEFT, padx=11)
        buttonYukle.pack(side = LEFT, padx=11)

        self.pencere.mainloop()

    def dosyaAlma(self):

        geciciDosyaAdi , self.dosyaAdi = self.dosyaAdi, self.girisDosya.get()

        dsy = self.dosyaAc()

        if dsy:#Dosya açılırsa kelimeleri dosyadan alıp listeye aktaracak
            self.__kelimeler = []#Yeni kelimeler ekleneceği için değişkenin içi boşaltılıyor.
            for kelime in dsy:
                self.__kelimeler.append(kelime)
            showinfo("Bilgilendirme","Dosyadaki kelimeler başarıyla Yüklendi!\n\nOyun bu kelimelere göre ayarlandı!")
            self.yeniOyun()
        else:
            self.dosyaAdi = geciciDosyaAdi #bu şekilde ilgili dosya yüklenmemişse eski dosya adı tutulmaya devam edilecektir.
            showerror("Hata", "Yüklemeye çalıştığınız {} adlı dosya, programın çalışma dizininde bulunamadı !".format(self.girisDosya.get()))
            showwarning("Uyarı", "Lütfen\n1) Dosyanın doğru yerde olup olmadığını kontrol ediniz!\n2) Dosyanın adını doğru girdiğinizden emin olunuz! ")
            showinfo("Bilgilendirme","İlgili dosya yüklenemediği için eski verilerle oyuna devam edilecektir !")

        self.pencere.destroy()

    def degerlendir(self):
        girilen = self.girisKullanici.get()

        if girilen == "":
            showinfo("Uyarı","Herhangi bir şey girmediniz!")

        else :

            if girilen == self.__kelimeler[self.indeks].strip("\n"):
                showinfo("Tebrikler","Doğru cevap olan \'{}\' kelimesini buldunuz :)".format(girilen))
                showinfo("Bilgilendirme","Yeni oyun ayarlanıyor...")
                self.yeniOyun()
                return True

            elif girilen in self.__kelimeler[self.indeks].strip("\n"):
                self.listBoxDurum.insert(0,"Girdiğin bu \"{}\" kelimesi aranan cevabın içinde var ".format(girilen))

            else:
                self.listBoxDurum.insert(0,"En son bu kelimeyi girdin => {}".format(girilen))

            self.__sayac += 1
            self.etiketAdam["text"] = self.__adamDurumu[self.__sayac]               

        if self.__sayac == (len(self.__adamDurumu)-1):
            self.__sayac=0 
            showinfo("bilgilendirme","Bilemedin doğru cevap => {}".format(self.__kelimeler[self.indeks]))
            showinfo("Bilgilendirme","Yeni oyun ayarlanıyor")
            self.yeniOyun()


if __name__ == "__main__":
    dosyaAdi = "iller.csv"
    oyun = AdamOyun(dosyaAdi)
