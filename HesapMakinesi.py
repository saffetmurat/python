import time

baslık="Bu bir örnek hesap makinesi uygulamasıdır."
giriş="""
(1) topla işlemi
(2) fark işlemi
(3) çarpım işlemi
(4) bölme işlemi
(5) karesini hesaplama işlemi
(6) kare kök hesaplama işlemi
Çıkış için bu rakamlardan farklı bir tuşa basın!
"""

yazilar = {
	"1":"Toplama-Toplanacak değerlerin ilkini girin:",
	"11":"Toplanacak değerlerin ikincisini girin:",
	"2":"Fark-Çıkarılacak değerlerin ilkini girin:",
	"22":"Çıkarılacak değerlerin ikincisini girin:",
	"3":"Çarpım-Çarpılacak değerlerin ilkini girin:",
	"33":"Çarpılacak değerlerin ikincisini girin:",
	"4":"Bölme-Bölünen değeri girin:",
	"44":"Bölen değeri girin:",
	"5":"Kare Alma-Karesi alınacak değeri girin:",
	"6":"Kare Kök Alm-Kare kökü alınacak değeri girin:"
}

print(baslık,giriş,sep="\n")


while True:

	islem=input("Yapmak istediğiniz işlemin numarasını giriniz : ")
	
	try:
		if islem in ["1","2","3","4","5","6"]:
			sayi1=int(input("{}".format(yazilar[islem].split("-")[1])))
			if (islem+islem) in yazilar:
				sayi2=int(input("{}".format(yazilar.get(islem+islem))))#get yerine [] kullansaydık islemislem olmadığında hata alırdık. Şimdi hata almayacağız
				#Sadece null değeri geri dönecek
	except:
		print("Bir tamsayı girilmedi. Tekrar deneyin!\n")
		continue
		
	if islem=="1":
		sonuc=sayi1+sayi2
	elif islem=="2":
		sonuc=sayi1-sayi2
	elif islem=="3":
		sonuc=sayi1*sayi2
	elif islem=="4":
		sonuc=sayi1/sayi2
	elif islem=="5":
		sonuc=sayi1**2
	elif islem=="6":
		sonuc=sayi1**0.5
	else:
		print("Kabul edilen bir işlem numarası girmediniz! Program kapatılıyor :(")
		time.sleep(5)
		break

	print("{} işleminin sonucu olarak {} değeri bulunmuştur.\n".format(yazilar[islem].split("-")[0],sonuc))