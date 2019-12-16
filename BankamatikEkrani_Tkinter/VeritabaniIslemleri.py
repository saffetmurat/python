import sqlite3 as s3
import os
from tkinter.messagebox import *

class VeritabaniIslemleri():
    def __init__(self, adres = os.getcwd() + os.sep + "bankamatikEkrani.db"):
        self.adres=adres
        
    def baglanti(self):
        if os.path.exists(self.adres):
            self.veritabani=s3.connect(self.adres)
            self.imlec=self.veritabani.cursor()
        else:
            raise Exception

    def musteriBilgisiAl(self, musteriNo):
        try:
            self.baglanti()

            sorgu = "SELECT * FROM MUSTERI WHERE MUSTERI_NO='{}'".format(musteriNo)
            sonuc = self.imlec.execute(sorgu)
            liste = sonuc.fetchall()
            
            self.veritabani.close()
            return liste
        except:
            showwarning("Uyarı", "Veritabanı Bulunamıyor.")
            return False

    def hesapBilgisiAl(self, musteriID):
        try:
            self.baglanti()

            sorgu = "SELECT * FROM HESAP WHERE HESAP_MUSTERI_ID='{}'".format(musteriID)
            sonuc = self.imlec.execute(sorgu)
            liste = sonuc.fetchall()
            
            self.veritabani.close()
            return liste
        except:
            showwarning("Uyarı", "Veritabanı Bulunamıyor.")
            return False

    def hesapBilgisiTutarGuncelle(self, hesapId, hesapTutar):
        try:
            self.baglanti()

            sorgu = "UPDATE HESAP SET HESAP_TUTAR = '{}' WHERE HESAP_ID = '{}';".format(hesapTutar, hesapId)
            sonuc = self.imlec.execute(sorgu)
            self.veritabani.commit()
            
            self.veritabani.close()
            
            return True
        except:
            showwarning("Uyarı", "Veritabanı Bulunamıyor.")
            return False

    def kurBilgisiAl(self,kuradi):
        try:
            self.baglanti()

            sorgu = "SELECT KUR_ORAN FROM KUR WHERE KUR_AD = '{}';".format(kuradi)
            sonuc = self.imlec.execute(sorgu)
            liste = sonuc.fetchall()
            
            self.veritabani.close()

            return liste
        except:
            showwarning("Uyarı", "Veritabanı Bulunamıyor.")
            return False

    def yeniHesapAc(self, musteriId, hesapNo, hesapTur):
        try:
            self.baglanti()
            sorgu = """INSERT INTO HESAP ( HESAP_NUMARASI, HESAP_TUTAR, HESAP_TURU, HESAP_MUSTERI_ID)
                    VALUES ( '{}', '{}', '{}', '{}');""".format(hesapNo,0,hesapTur,musteriId)

            sonuc = self.imlec.execute(sorgu)
            self.veritabani.commit()
            
            self.veritabani.close()

            return True
        except:
            showwarning("Uyarı", "Veritabanı Bulunamıyor.")
            return False

    def hesapSil(self,hesapId):
        try:
            self.baglanti()
            sorgu = "DELETE FROM HESAP WHERE HESAP_ID = '{}'".format(hesapId)

            sonuc = self.imlec.execute(sorgu)
            self.veritabani.commit()
            
            self.veritabani.close()

            return True
        except:
            showwarning("Uyarı", "Veritabanı Bulunamıyor.")
            return False

    def kurumAdlari(self,kurumTur):
        try:
            self.baglanti()
            sorgu = "SELECT KURUM_ID, KURUM_AD FROM KURUM WHERE KURUM_TUR = '{}'".format(kurumTur)

            sonuc = self.imlec.execute(sorgu)
            liste = sonuc.fetchall()
            
            self.veritabani.close()

            return liste
        except:
            showwarning("Uyarı", "Veritabanı Bulunamıyor.")
            return False

            
if __name__ == "__main__":
    vti = VeritabaniIslemleri()
    print(vti.musteriBilgisiAl("123789456"))
    print(vti.hesapBilgisiAl("2"))