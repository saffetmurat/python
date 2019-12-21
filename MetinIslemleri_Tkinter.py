import tkinter as tk
from tkinter.messagebox import *

class Sifreleme():
    def __init__(self):
        pass

    def pencereYap(self):
        pencere = tk.Tk()
        pencere.title("Metni Ters Çevirme Uygulaması")
        pencere.geometry("600x380+100+100")
        pencere.resizable(width = False, height = False)

        menu1 = tk.Menu(pencere)
        pencere.config(menu = menu1)

        menuIslemler = tk.Menu(menu1, tearoff = 0)
        menu1.add_cascade(label = "İşlemler", menu = menuIslemler )

        menuCevir = tk.Menu(menuIslemler, tearoff = 0)
        menuIslemler.add_cascade(label = "Giriş Verisini Ters Çevir", menu = menuCevir)
        menuCevir.add_command(label = "Kelimelerin Yerlerini Ters Çevir", command = self.cevirKelime)
        menuCevir.add_command(label = "Her Bir Kelimenin İçeriğini Ters Çevir", command = self.cevirKelimeIcerik)
        menuCevir.add_command(label = "Cümleyi Tamamen Ters Çevir", command = self.cevirCumle)

        
        menuTemizle = tk.Menu(menuIslemler, tearoff = 0)
        menuIslemler.add_cascade(label = "Ekranı Temizle", menu = menuTemizle)
        menuTemizle.add_command(label = "Tüm Ekranı Temizle", command = self.tumEkranTemizle)
        menuTemizle.add_command(label = "Giriş Verisi Ekranını Temizle", command = self.girisEkranTemizle)
        menuTemizle.add_command(label = "Sonuç Verisi Ekranını Temizle", command = self.sonucEkranTemizle)

        menuAciklamalar = tk.Menu(menu1, tearoff = 0)
        menu1.add_cascade(label = "Açıklamalar", menu = menuAciklamalar)
        menuAciklamalar.add_command(label = "Hakkımda", command = self.hakkimda)

        girisEtiket = tk.Label(pencere, text = "\nGiriş Verisi Ekranı\n", font = "Times 13")
        self.girisMetin = tk.Text(pencere, width = 74, height = 7)

        sonucEtiket = tk.Label(pencere, text = "\nSonuç Ekranı\n", font = "Times 13")
        self.sonucMetin = tk.Text(pencere, state = 'disabled', width = 74, height = 7)
        
        girisEtiket.grid(row=1, column=1)
        self.girisMetin.grid(row=2, column=1)

        sonucEtiket.grid(row=3, column=1)
        self.sonucMetin.grid(row=4, column=1)

        pencere.mainloop()

    def hakkimda(self):
        showinfo("Hakkımda","Saffet Murat tarafından yapıldı\n(Created by: Saffet Murat)\n\n{}\n\n{}".format("https://trmsma.wordpress.com","https://github.com/saffetmurat"))

    def ortakKisimlar(self, durum = True, sonuc=""):
        if durum:
            metin = self.girisMetin.get("1.0", tk.END)

            self.sonucMetin.config(state = "normal")#Aktif hale geliyor.
            self.sonucMetin.delete("1.0", tk.END)#İçeriği temizleniyor.

            if metin == "" or metin == "\n":
                showwarning("Uyarı", "Lütfen bir metin giriniz...")     
                raise Exception

            return metin
        else:
            self.sonucMetin.insert(tk.END, sonuc)#İçerik eklenir.
            self.sonucMetin.config(state = "disabled")#Pasif hale geliyor.

    def cevirKelime(self):
        try:
            metin  = self.ortakKisimlar()
            sonuc = ""
            for indeks in range(len(metin.strip("\n").split(" "))-1, -1, -1):
                sonuc += metin.strip("\n").split(" ")[indeks] + " "

            metin  = self.ortakKisimlar(False, sonuc)
        except Exception:
            pass

    def cevirKelimeIcerik(self):
        try:
            metin  = self.ortakKisimlar()
            sonuc = araDeger = ""
            for indeks in range(len(metin.strip("\n").split(" "))):
                for harf in metin.strip("\n").split(" ")[indeks]:
                    araDeger = harf + araDeger
                sonuc += " " + araDeger
                araDeger = ""

            metin  = self.ortakKisimlar(False, sonuc)
        except Exception:
            pass

    def cevirCumle(self):
        try:
            metin  = self.ortakKisimlar()

            #metin ters çevrilir.
            sonuc = ""
            for indeks in range(len(metin)-1, -1, -1):
                sonuc += metin[indeks]
            
            metin  = self.ortakKisimlar(False, sonuc)
        except Exception:
            pass

    def tumEkranTemizle(self):
        self.girisMetin.delete("0.0", tk.END)
        self.sonucMetin.config(state = 'normal')
        self.sonucMetin.delete("0.0",tk.END)#İçerik temizlenir.
        self.sonucMetin.config(state = 'disabled')

    def girisEkranTemizle(self):
        self.girisMetin.delete("0.0", tk.END)

    def sonucEkranTemizle(self):
        self.sonucMetin.config(state = 'normal')
        self.sonucMetin.delete("0.0", tk.END)
        self.sonucMetin.config(state = 'disabled')                

if __name__ == "__main__":
    se = Sifreleme()
    se.pencereYap()