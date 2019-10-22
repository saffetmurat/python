import random
import time


class Agac():

    def __init__(self):
        self.basla()

    def basla(self):
        try:
            print("Ağaç Çizme Programı")
            yas=int(input("Girilen yaşta bir ağaç çizilecektir :"))

            tur=random.randrange(2)

            if tur == 1:#Çam ağacı çizecek
                #yapraklar 2/3 büyüklüğünde olacak
                yaprak=round((yas/3)*2)
                for s in range(0,yaprak):
                    print(" "*(yaprak-s),"*"*((s*2)+1)," "*(yaprak-s))

                #govde 1/3 büyüklüğünde olacak
                govde=round(yas/3)

                for i in range(govde):
                    print(" "*(govde*2-1),"||"," "*(govde*2-1))

            else:#dikdörtgen şeklinde ağaç çizecek
                #yapraklar 2/3 büyüklüğünde olacak
                yapraklar1=[]
                yapraklar2=[]
                yapraklar3=[]
                yaprak=(yas//3)*2
                for s in range(yaprak,0,-1):
                    yapraklar2.append(" "*s + "*"*(yaprak-s) +  "*"*(yaprak-s) +" "*s )

                for s in range(1,yaprak):
                    yapraklar1.append(" "*s + "*"*(yaprak-s) + "*"*(yaprak-s) +" "*s )

                yapraklar3=yapraklar2 + yapraklar1
                print(*yapraklar3,sep="\n")

                #govde 1/3 büyüklüğünde olacak
                govde=yas//3

                for i in range(govde):
                    print(" "*(govde*2-2),"||"," "*(govde*2-1))
        except:
            print("Bir hatayla karşılaşıldı !")

if __name__ == "__main__":
    agac = Agac()

    print("")
    say = 20
    while say:
        print("\rProgram Kapatılıyor. Son {} saniye ...".format(say),end="")
        say -= 1
        time.sleep(1)