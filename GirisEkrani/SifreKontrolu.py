class Kontroller():
    __sifre = ""

    def __init__(self):
        self.kontrol()

    def sifreAl(self):
        return self.__sifre

    def sayiKontrolu(self, metin):
        try:
            int(metin)
            return True # Bu durumda şifrenin tamamı rakamlardan OLUŞUYORdur.
            #Bu durumda self.kontrol() fonksiyonu hata vermelidir.
        except:
            return False
            #Bu durumda şifrenin tamamı rakamlardan oluşMUYORdur.

    def rakamVarmi(self, metin):
        rakamlar = "0123456789"

        for harf in metin:
            if harf in rakamlar:
                return False # Bu durumda şifrenin içinde rakam vardır.
                #Bu durumda self.kontrol() fonksiyonu hata vermelidir.
        else:
            return True# Bu durumda şifrenin içinde hiç rakam yoktur.
            #Bu durumda self.kontrol() fonksiyonu hata vermelidir.


    def kucukVarMi(self, metin):
        harfler = "qwertyuıopğüasdfghjklşizxcvbnmöç"

        for harf in metin:
            if harf in harfler:
                return False
        else:
            return True #hata var olduğunu belirtir.

    def buyukVarMi(self, metin):
        harfler = "QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ"

        for harf in metin:
            if harf in harfler:
                return False
        else:
            return True #hata var olduğunu belirtir.

    def noktalamaVarMi(self, metin):
        noktalamalar = "!^+%&/()=?-_#${[]}\*.:,;<>|@"

        for harf in metin:
            if harf in noktalamalar:
                return False
        else:
            return True #hata var olduğunu belirtir.      

    def uzunlukKontrolu(self, metin):
        if len(metin) < 12:
            return True #hata var olduğunu belirtir.
        else:
            return False

    def kontrol(self):
        sifre = ""

        while True:
            try:
                hataMesaji = "Kabul edilebilir bir şifre için aşağıdaki HATALARA UYMAYAN bir şifre belirleyin =>\n"
                sayac = 0
                sifre = input("Şifre Giriniz : ")
                if self.uzunlukKontrolu(sifre):
                    sayac += 1
                    hataMesaji += "{}) Girilen şifre en az 12 karakterden oluşmalıdır.\n".format(sayac)

                if self.kucukVarMi(sifre):
                    sayac += 1
                    hataMesaji += "{}) Girilen şifre en az 1 küçük harften oluşmalıdır.\n".format(sayac)

                if self.buyukVarMi(sifre):
                    sayac += 1
                    hataMesaji += "{}) Girilen şifre en az 1 büyük harften oluşmalıdır.\n".format(sayac)

                if self.noktalamaVarMi(sifre):
                    sayac += 1
                    hataMesaji += "{}) Girilen şifrede en az 1 tane noktalama işareti olmalıdır.\n".format(sayac)

                if self.sayiKontrolu(sifre):
                    sayac += 1
                    hataMesaji += "{}) Girilen şifrenin tamamı rakamlardan oluşamaz.\n".format(sayac)

                if self.rakamVarmi(sifre):
                    sayac += 1
                    hataMesaji += "{}) Girilen şifrede en az 1 tane rakam olmalıdır.\n".format(sayac)

                if sayac > 0:
                    raise Exception (hataMesaji)

            except Exception as hata:
                print("HATA! ", hata)

            else:
                self.__sifre = sifre
                break

if __name__ == "__main__":
    sk = Kontroller()
