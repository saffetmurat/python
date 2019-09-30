baslik="Basit hesap Makinesi"
print("+"*len(baslik),baslik.upper(),"+"*len(baslik))

tur=("+","-","*","/","^","%")
islem=""
while True:
    try:
        while tur.count(islem)==0:#veya while islem not in tur: ifadesi de kullanılabilir.
            islem = input("İşlem türü giriniz(+,-,/,*,^,%(mod)) :")

        Silk = int(input("İlk Sayıyı giriniz :"))
        Sikinci = int(input("İkinci Sayıyı giriniz :"))
        if islem == "+":
            son = Silk + Sikinci
        elif islem == "-":
            son = Silk - Sikinci
        elif islem == "/":
            son = Silk / Sikinci
        elif islem == "*":
            son = Silk * Sikinci
        elif islem == "^":
            son = Silk ** Sikinci
        elif islem == "%":
            son = Silk % Sikinci

        print(Silk,islem,Sikinci,"=",son,end="\n\n")

        cık=input("Programdan çıkmak isterseniz E tuşuna basın :")
        islem=""
        if cık.upper()=="E":
            break
    except:
        print("Sayıları kontrol edin bir hata oluştu")
        islem=""