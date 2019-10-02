import time

baslik="Basamak sayısını bulan program"
print("-"*len(baslik),baslik,"-"*len(baslik),sep="\n",end="\n\n")

try:
    sayi = input("Bir tam sayı giriniz :")
    #sayi = int(input("Bir tam sayı giriniz :")) şeklinde olursa 
    #except kısmında sayi değişkeni tanımlanmadı deyip hata veriyor.
    #Hata alınmadan önce sayi değişkeni oluşturulyor.
    #Ardından dönüşüm yapılıyor. Dönüşümde hata olunca bu sefer sayi değişkeni önceden tanımlandığı
    #için except kısmında sıkıntı çıkmıyor.
    sayi = int(sayi)
    basamaklar=[]

    for s in str(sayi):
        basamaklar.append(s)

    if sayi < 0:
        print(sayi, "negatif sayısının sahip olduğu basamaklardaki rakamlar =>", basamaklar[1:],"\nToplam basamak sayısı",len(basamaklar)-1)

    else:
        print(sayi, "pozitif sayısının sahip olduğu basamaklardaki rakamlar =>", basamaklar,"\nToplam basamak sayısı",len(basamaklar))

except:
    print("\"{}\" bir tam sayı değil!".format(sayi))

finally:
    sayac = 20
    while sayac>0:
        print("\rProgram Kapatılıyor. Son {} sn..".format(sayac),end="")
        time.sleep(1)
        sayac -= 1
