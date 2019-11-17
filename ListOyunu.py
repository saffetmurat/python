import time

class ListOyunu():
    def __init__(self):
        self.giris()
        
    def giris(self):
        baslik="Basit Firma Yönetim Oyunu"
        print("*"*len(baslik),baslik,"*"*len(baslik),sep="\n",end="\n\n")

        while True:
            print("")
            tercih = input("Oyuna başlamak için 1'e\nAçıklamaları görmek için 2'ye\nHakkımda kısmını görmek için 3'e basınız..")
            if tercih == "1":
                self.listOyunuKismi()
                break
            elif tercih == "2":
                self.aciklamalar()
            elif tercih == "3":
                self.hakkimda()
            else:
                print("Benim için anlamsız bir tuşa bastınız... Tekrar deneyiniz...")

    def aciklamalar(self):
        aciklama ="""AÇIKLAMALAR=>
        Bu uygulamanın amacı list türünün fonksiyonlarından olan append, insert, remove, pop, count, clear fonksiyonlarını kullanarak bir uygulama yapmaktır.
        Uygulama basit bir oyun olarak tasarlanmıştır. 
        """
        print(aciklama)

    def hakkimda(self):
        hakkimda = "\nHAKKIMDA=>\nSaffet Murat tarafından yapıldı\n(Created by: Saffet Murat)\n\nhttps://trmsma.wordpress.com\n\nhttps://github.com/saffetmurat"
        print(hakkimda,end="\n\n")

    def listOyunuKismi(self):
            print("\nBir Firmanın Sahibisiniz.\nFirmanızla ilgili birkaç işlem yapmak istiyorsunuz.",end="\n\n")

            il=["Ankara","İstanbul", "Sinop"]

            while True:
                print("Şubelerinizin bulunduğu iller öncelik sırasına göre aşağıdaki gibidir:","NOT: Soldan sağa doğru öncelik azalır.",il, sep="\n",end="\n\n")

                #append() metodu kullanımı
                ad=input("Hangi ilde şube açmak istersiniz? İlin adı :").capitalize()
                il.append(ad)
                print("Açıldı. :)")
                print("Son durum =>", il, sep="\n", end="\n\n")

                print("-"*60, end="\n\n")

                ##################################################################################
                #insert() metodu kullanımı
                print("Hangi ile öncelik vererek bir şube açamak istersiniz? :")
                try:
                    numara = int(input("İlin öncelik numarasını verin (1 En öncelikli) :"))
                except:
                    print("Bir tamsayı girilmedi. Bu işlem yapılmıyor.")
                else:
                    ad = input("İlin adını girin :").capitalize()
                    il.insert(numara-1, ad)
                    print("Eklendi. :)")
                finally:
                    print("Son durum =>", il, sep="\n", end="\n\n")

                print("-"*60, end="\n\n")

                ##################################################################################
                #remove() metodu kullanımı
                ad = input("Hangi ildeki şubeyi silmek istersiniz? İlin adı :").capitalize()
                if il.count(ad)>0:
                    il.remove(ad)
                    print("Silindi. :(")
                else:
                    print(ad, "adında bir ilde zaten şubeniz yok.\nBu yüzden silme işlemi yapılamaz")
                print("Son durum =>", il, sep="\n", end="\n\n")

                print("-"*60, end="\n\n")

                ##################################################################################
                #pop() metodu kullanımı
                print("Hangi öncelikteki ili silmek istersiniz?(1 En öncelikli) :")
                try:
                    numara = int(input("İlin öncelik numarasını verin :"))
                except:
                    print("Bir tamsayı girilmedi. Bu işlem yapılmıyor.")                    
                else:
                    if len(il)<numara:
                        print("Girdiğiniz öncelik değerine sahip bir İL yok")
                    else:
                        il.pop(numara-1)
                        print("Kaldırıldı. :(")
                finally:
                    print("Son durum =>", il, sep="\n", end="\n\n")

                print("-"*60, end="\n\n")

                ##################################################################################
                #count() metodu kullanılacak
                ad=input("""Gireceğiniz ilde kaç tane şubeniz olduğunu öğrenmek için ilin adını giriniz :""").capitalize()
                print(ad, "ilinde toplam", il.count(ad),"tane şubeniz var.")
                print("Son durum =>", il, sep="\n", end="\n\n")

                print("-"*60, end="\n\n")

                ##################################################################################
                #clear() metodu kullanılacak
                cevap=input("Şubelerin hepsini kapatmak ister misiniz?(H): ")
                if cevap.upper()!="H":
                    il.clear()
                    print("Şubelerin tamamı kapatıldı :(")
                    print("Son durum =>", il, sep="\n", end="\n\n")
                else:
                    print("Şubelerinize dokunulmadı. :) Şubelerinizin bulunduğu iller =>", il, sep="\n", end="\n\n")

                print("-"*60, end="\n\n")

                ##################################################################################
                cevap = input("Oyundan çıkmak ister misiniz?(H): ")
                if cevap.lower() != "h":
                    print("Oyun kapatılıyor :( \nYİNE OYNA :)", end="\n\n")
                    time.sleep(1)
                    break
                else:
                    print("Oyuna devam :) ", end="\n\n")

if __name__ == "__main__":
    lo = ListOyunu()