import time
import random as rastgele

class TahminOyunu():
	___aciklama = """
Kullanıcı pozitif bir tamsayı girer.
Girdiği sayının rakamlarından kaç tanesinin yerleri ve rakamların değerleri doğruysa o kadar + işareti koyulur.
Girdiği sayının rakamlarından kaç tanesinin yerleri farklı ancak rakamların değerleri doğruysa o kadar - işareti koyulur. 

Örnek sayı 7234 olsun. Kullanıcı 7548 girsin.
Çıktı => 1 +, 1 - olur. 1 + demek rakamlardan birinin yerinin ve değerinin doğru olduğunu
1 - ise geri kalan rakamlardan bir tanesinin değerinin doğru ancak yerinin farklı olduğunu belirtir.   
	"""

	def __init__(self):
		self.giris()
	
	def rastgeleSayıUretme(self,alt,ust):
		return rastgele.randrange(alt,ust)

	def tahminOyunu(self):

		ras = str(self.rastgeleSayıUretme(1000,10000))
		tah = []
		ra = []
		miktar=0

		while True:
			try:
				miktar += 1
				tahmin = input("4 Basamaklı Bir Tahmin Sayısı Giriniz : ")

				tah.clear()
				ra.clear()

				Kumarti = Kumeksi = 0

				if int(tahmin) < 0:
					print("Pozitif bir tam sayı giriniz!")
				elif len(tahmin) != 4:
					print("{} basamakli bir sayı girdiniz.\n".format(len(tahmin)))
				elif tahmin == ras:
					print("Tebrikler {}. tahmininde doğru sayıyı buldun\n".format(miktar))
					break
				else:

					for i in ras:
						ra.append(i)

					for i in tahmin:
						tah.append(i)

					#Birebir aynı konumda ve aynı değerde olanları bulmaya çalışıyor. 
					#Bulursa bir daha incelenmemesi için diziden çıkarılıyor.
					for s in range(len(ras)-1, -1, -1):
						if tahmin[s] == ras[s]:
							ra.pop(s)
							tah.pop(s)
							Kumarti += 1

					#Konumları farklı, değerleri aynı olan rakamlar bulunuyor. 
					for s in range(len(ra)-1, -1, -1):
						for m in range(len(tah)-1, -1, -1):
							if tah[m] == ra[s] and m != s:
								ra.pop(s)
								tah.pop(m)
								Kumeksi += 1
								break

					print("{} +, {} - Tekrardan\n".format(Kumarti, Kumeksi))
			except:
				print("Bir tam sayı giriniz!\n")

	def giris(self):
		baslik = "4 Basamaklı Sayı Tahmin Oyunu"
		print("     SAYI TAHMİN OYUNU")
		print("-"*len(baslik), baslik, "-"*len(baslik),sep="\n",end="\n\n")
		
		while True:
			tercih = input("Oyuna girmek için 1'e, Oyun açıklaması için 2'ye, Çıkış için 3'e basınız :")
			if tercih == "1":
				self.tahminOyunu()
			elif tercih == "2":
				print(self.___aciklama)
			elif tercih == "3":
				break
			else:
				print("Geçersiz bir tuşa bastınız.\nTekrar deneyin.\n")

########################################################################################################################

if __name__ == "__main__":
	to = TahminOyunu()
    print("Program Kapatılıyor. Bekleyiniz...")
    time.sleep(1)




