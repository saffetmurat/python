baslik="Basamak sayısını bulan program"
print("-"*len(baslik),baslik,"-"*len(baslik),sep="\n",end="\n\n")

try:
    sayi = int(input("Bir tam sayı giriniz :"))
    basamaklar=[]

    for s in str(sayi):
        basamaklar.append(s)

    if sayi < 0:
        print(sayi, "negatif sayısının sahip olduğu basamaklardaki rakamlar =>", basamaklar[1:],"\nToplam basamak sayısı",len(basamaklar)-1)
    else:
        print(sayi, "pozitif sayısının sahip olduğu basamaklardaki rakamlar =>", basamaklar,"\nToplam basamak sayısı",len(basamaklar))


except:
    print("{} bir tam sayı değil!".format(sayi))
