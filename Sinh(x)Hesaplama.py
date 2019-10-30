import time

baslik="""Klavyeden girilen x sayısının sinh(x) değerini,
yine klavyeden girilecek olan N terim sayısına
kadar seriye açarak hesaplayan program"""

print("-"*48,baslik,"-"*48,sep="\n",end="\n\n")

while True:
    sinhx=0
    while True:
        sayi=input("x sayısını girin :")
        terim=input("N terim sayısını girin :")

        if not sayi.isdigit() or not terim.isdigit():
            print("Bu bir sayı değil",end="\n\n")
        else:
            print("Uygun bir sayı girildi.")
            break

    for s in range(1, int(terim) * 2 + 1, 2):
        alt=1
        for a in range(1,s+1):
            alt *= a

        sinhx+=(int(sayi)**s)/alt

    print(int(sayi), "sayısının",int(terim),"terime kadar sinh(x) sonucu =",sinhx)

    tercih = input("Çıkış için E/e tuşuna basınız : ")
    if tercih in ["E","e"]:
        print("Çıkış isteğiniz alındı. Program kapatılıyor....")
        time.sleep(2)#2 saniye bekleyecek
        break


