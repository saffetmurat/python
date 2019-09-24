from tkinter import *
from tkinter.messagebox import *
import os

islemDeger=""
sonuc=0
girisAdres=""
gecmisVerileri=[]

#rakamlar
def sayilariEkle(param="0"):
   global islemDeger
   gecici = listEkran.get(ACTIVE)

   if islemDeger == "":
      listEkran.delete(0,END)
      gecici = gecici + param
      listEkran.insert(END,gecici)
   elif "=" in gecici:
      islemDeger=""
      listEkran.delete(0,END)
      listEkran.insert(END,param)
   else:
      listEkran.delete(0,END)
      gecici = gecici + param
      listEkran.insert(END,gecici)

def sayıYaz1():
   sayilariEkle("1")

def sayıYaz2():
   sayilariEkle("2")

def sayıYaz3():
   sayilariEkle("3")

def sayıYaz4():
   sayilariEkle("4")

def sayıYaz5():
   sayilariEkle("5")

def sayıYaz6():
   sayilariEkle("6")

def sayıYaz7():
   sayilariEkle("7")

def sayıYaz8():
   sayilariEkle("8")

def sayıYaz9():
   sayilariEkle("9")

def sayıYaz0():
   sayilariEkle("0")

#işaretler
def islemIsaretDegistir():
   gecici = listEkran.get(ACTIVE)

   if len(gecici)==0:
      pass
   elif islemDeger=="":
      sayi1 = (-1.0) * float(gecici)
      listEkran.delete(0,END)
      listEkran.insert(END,str(sayi1))

      listeGecmis.insert(END,str(sayi1))
      gecmisVerileri.append(str(sayi1)+"\n")

def islemTopla():
   global islemDeger
   gecici = listEkran.get(ACTIVE)

   if len(gecici)==0:
      pass
   elif islemDeger=="":
      islemDeger="+"
      listEkran.delete(0,END)
      gecici = gecici+ islemDeger
      listEkran.insert(END,gecici)
   elif len(gecici.split(islemDeger)) == 2:
      sayi1=gecici.split(islemDeger)[0]
      sayi2=gecici.split(islemDeger)[1]
      islemDeger="+"
      gecici = sayi1 + islemDeger + sayi2
      listEkran.delete(0,END)
      listEkran.insert(END,gecici)

def islemCikar():
   global islemDeger
   gecici = listEkran.get(ACTIVE)

   if len(gecici)==0:
      pass
   elif islemDeger=="":
      islemDeger="-"
      listEkran.delete(0,END)
      gecici = gecici+ islemDeger
      listEkran.insert(END,gecici)
   elif len(gecici.split(islemDeger)) == 2:
      sayi1=gecici.split(islemDeger)[0]
      sayi2=gecici.split(islemDeger)[1]
      islemDeger="-"
      gecici = sayi1 + islemDeger + sayi2
      listEkran.delete(0,END)
      listEkran.insert(END,gecici)

def islemCarp():
   global islemDeger
   gecici = listEkran.get(ACTIVE)

   if len(gecici)==0:
      pass
   elif islemDeger=="":
      islemDeger="*"
      listEkran.delete(0,END)
      gecici = gecici+ islemDeger
      listEkran.insert(END,gecici)
   elif len(gecici.split(islemDeger)) == 2:
      sayi1=gecici.split(islemDeger)[0]
      sayi2=gecici.split(islemDeger)[1]
      islemDeger="*"
      gecici = sayi1 + islemDeger + sayi2
      listEkran.delete(0,END)
      listEkran.insert(END,gecici)

def islemOndalıklıBol():
   global islemDeger
   gecici = listEkran.get(ACTIVE)

   if len(gecici)==0:
      pass
   elif islemDeger=="":
      islemDeger="/"
      listEkran.delete(0,END)
      gecici = gecici+ islemDeger
      listEkran.insert(END,gecici)
   elif len(gecici.split(islemDeger)) == 2:
      sayi1=gecici.split(islemDeger)[0]
      sayi2=gecici.split(islemDeger)[1]
      islemDeger="/"
      gecici = sayi1 + islemDeger + sayi2
      listEkran.delete(0,END)
      listEkran.insert(END,gecici)

def islemTamSayiBol():
   global islemDeger
   gecici = listEkran.get(ACTIVE)

   if len(gecici)==0:
      pass
   elif islemDeger=="":
      islemDeger="//"
      listEkran.delete(0,END)
      gecici = gecici+ islemDeger
      listEkran.insert(END,gecici)
   elif len(gecici.split(islemDeger)) == 2:
      sayi1=gecici.split(islemDeger)[0]
      sayi2=gecici.split(islemDeger)[1]
      islemDeger="//"
      gecici = sayi1 + islemDeger + sayi2
      listEkran.delete(0,END)
      listEkran.insert(END,gecici)

def islemMod():
   global islemDeger
   gecici = listEkran.get(ACTIVE)

   if len(gecici)==0:
      pass
   elif islemDeger=="":
      islemDeger="%"
      listEkran.delete(0,END)
      gecici = gecici+ islemDeger
      listEkran.insert(END,gecici)
   elif len(gecici.split(islemDeger)) == 2:
      sayi1=gecici.split(islemDeger)[0]
      sayi2=gecici.split(islemDeger)[1]
      islemDeger="%"
      gecici = sayi1 + islemDeger + sayi2
      listEkran.delete(0,END)
      listEkran.insert(END,gecici)

def islemUsAl():
   global islemDeger
   gecici = listEkran.get(ACTIVE)

   if len(gecici)==0:
      pass
   elif islemDeger=="":
      islemDeger="^"
      listEkran.delete(0,END)
      gecici = gecici+ islemDeger
      listEkran.insert(END,gecici)
   elif len(gecici.split(islemDeger)) == 2:
      sayi1=gecici.split(islemDeger)[0]
      sayi2=gecici.split(islemDeger)[1]
      islemDeger="^"
      gecici = sayi1 + islemDeger + sayi2
      listEkran.delete(0,END)
      listEkran.insert(END,gecici)

def islemEsit():
   global islemDeger, sonuc
   gecici = listEkran.get(ACTIVE)

   if islemDeger != "" and gecici.split(islemDeger)[1] != "":
      if "=" in gecici.split(islemDeger)[1]:
         indeks = gecici.find("=")
         gecici = gecici[0:indeks]

      if islemDeger == "+":
         sonuc=float(gecici.split(islemDeger)[0]) + float(gecici.split(islemDeger)[1])
      elif islemDeger == "-":
         if gecici == "-":
            sonuc = ((-1)*float(gecici[1:].split(islemDeger)[0])) - float(gecici.split(islemDeger)[1])
         else:
            sonuc=float(gecici.split(islemDeger)[0]) - float(gecici.split(islemDeger)[1])
      elif islemDeger == "*":
         sonuc=float(gecici.split(islemDeger)[0]) * float(gecici.split(islemDeger)[1])
      elif islemDeger == "/":
         if float(gecici.split(islemDeger)[1]) == 0.0:
            sonuc = 0.0
         else:
            sonuc=float(gecici.split(islemDeger)[0]) / float(gecici.split(islemDeger)[1])
      elif islemDeger == "//":
         if float(gecici.split(islemDeger)[1]) == 0.0:
            sonuc = 0.0
         else:
            sonuc=float(gecici.split(islemDeger)[0]) // float(gecici.split(islemDeger)[1])
      elif islemDeger == "%":
         if float(gecici.split(islemDeger)[1]) == 0.0:
            sonuc=0.0
         else:
            sonuc=float(gecici.split(islemDeger)[0]) % float(gecici.split(islemDeger)[1])
      elif islemDeger == "^":
         sonuc=float(gecici.split(islemDeger)[0]) ** float(gecici.split(islemDeger)[1])

      listEkran.delete(0,END)
      listEkran.insert(END,(gecici+"="+str(sonuc)))

      listeGecmis.insert(END,(gecici+"="+str(sonuc)))
      gecmisVerileri.append(gecici+"="+str(sonuc)+"\n")


def islemSil():
   global islemDeger
   gecici = listEkran.get(ACTIVE)

   if gecici and gecici[-1] in ["+", "-", "*", "/", "//", "%", "^"]:
      if islemDeger == "//":
         islemDeger="/"
      else:
         islemDeger=""

   gecici = gecici[:len(gecici)-1]
   listEkran.delete(0,END)
   listEkran.insert(END,gecici)

def dosyaKaydet():
   import datetime
   global girisAdres
   
   kayitYeri = girisAdres.get()

   # try:
   if kayitYeri=="":
      showwarning("Uyarı","Lütfen Kayıt yeri ve dosya adını giriniz.")
   elif os.path.exists((kayitYeri +".txt")):
      showerror("Hata","Bu adreste aynı ada sahip başka bir dosya var. Bu yüzden başka bir dosya adı giriniz.")
   else:
      #dosya açılıyor.
      dosya = open((kayitYeri +".txt"),"w")

      #Tarih bilgisi ekleniyor.
      gecici=datetime.datetime.now()
      tarih = "{}.{}.{} tarihinde {}:{} saatinde dosyaya eklenenler =>\n\n".format(gecici.day,gecici.month,gecici.year,gecici.hour,gecici.minute)
      dosya.write(tarih)

      #işlemler ekleniyor.
      dosya.writelines(gecmisVerileri)

      #dosya kapanıyor.
      dosya.close()
      showinfo("Bilgilendirme","Dosya oluşturularak geçmiş bilgileri kaydedildi.")
   # except:
   #    showerror("Hata","Anlaşılamayan bir hata oluştu")

def dosyaAc():
   global girisAdres

   kayitYeri=girisAdres.get()
   try:
      if kayitYeri=="":
         showwarning("Uyarı","Lütfen Kayıt yeri ve dosya adını giriniz.")
      elif os.path.exists((kayitYeri +".txt")):
         os.system("notepad " + (kayitYeri+".txt") )
      else:
         showerror("Hata","Bu adreste dosya bulunamadı.")
   except:
      showerror("Hata","Anlaşılamayan bir hata oluştu")

def islemCiktiAl():# ikinci bir pencere oluşturuluyor.
   try:
      global girisAdres

      pencere = Toplevel()
      pencere.geometry("420x140+500+100")
      pencere.resizable(width=FALSE, height=FALSE)

      etiketAdres=Label(pencere, text="""Aşağıdaki alana geçmiş işlemlerin kaydedilmesi istenen yeri giriniz.
         Örneğin; C:\Klasör\cıktı.
         Burada C:\Klasör\ dosyanın kaydedileceği konum cıktı ise dosyanın adıdır.""")

      girisAdres=Entry(pencere,width=68)

      butDosyaKaydet = Button(pencere, text = "Kaydet", command=dosyaKaydet)
      butDosyaAc = Button(pencere, text = "Dosyayı Aç", command=dosyaAc)

      etiketAdres.place(relx=0.0,rely=0.01)
      butDosyaKaydet.place(relx=0.1,rely=0.78)
      butDosyaAc.place(relx=0.7,rely=0.78)
      girisAdres.place(relx=0.01,rely=0.6)

      pencere.mainloop()
   except:
      showerror("Hata","Anlaşılamayan bir hata oluştu")      

def islemGecmisTablosuSil():
   listeGecmis.delete(0,END)

def islemGecmisiSil():
   global gecmisVerileri 
   gecmisVerileri= []

def islemGecmisTablIslemAktar():
   global islemDeger
   gecici_islem=listeGecmis.get(ACTIVE)

   if "=" not in gecici_islem:
      islemDeger=""
      listEkran.delete(0,END)
      listEkran.insert(END,gecici_islem)
   else:
      for i in gecici_islem[1:]:
         if i in ["+", "-", "*", "/", "//", "%", "^"]:
            islemDeger=i
            listEkran.delete(0,END)
            listEkran.insert(END,gecici_islem.split("=")[0])
            break

def islemTamSil():
   global islemDeger

   listEkran.delete(0,END)
   islemDeger=""

def aktar(gecici_islemEkran,gecici_islemGecmis):

   if "=" not in gecici_islemGecmis:
         listEkran.delete(0,END)
         listEkran.insert(END, gecici_islemEkran + gecici_islemGecmis)
   else:
         listEkran.delete(0,END)
         listEkran.insert(END, gecici_islemEkran + gecici_islemGecmis.split("=")[1])

def islemGecmisTablSonucAktar():
   global islemDeger

   gecici_islemGecmis = listeGecmis.get(ACTIVE)
   gecici_islemEkran = listEkran.get(ACTIVE)

   if gecici_islemEkran == "":
      aktar(gecici_islemEkran,gecici_islemGecmis)
   elif islemDeger == "":
      gecici_islemEkran=""
      aktar(gecici_islemEkran,gecici_islemGecmis)
   elif "=" not in gecici_islemEkran:
      if gecici_islemEkran[0] != "-":
         gecici_islemEkran = gecici_islemEkran.split(islemDeger)[0] + islemDeger
         aktar(gecici_islemEkran,gecici_islemGecmis)
      else:
         gecici_islemEkran = "-" + gecici_islemEkran[1:].split(islemDeger)[0] + islemDeger
         aktar(gecici_islemEkran,gecici_islemGecmis)
   else:
      pass


##############################################################################################################
#Tasarım Kısmı
##############################################################################################################
anaPencere = Tk()
anaPencere.title("Görsel Basit Hesap Makinesi")
anaPencere.geometry("400x600+100+100")
anaPencere.resizable(width=FALSE,height=FALSE)


listEkran = Listbox(anaPencere, width=35,height=2,font="Times 16 bold")

listeGecmis = Listbox(anaPencere,width=35, height=4, bg = "yellow", font="Times 16 bold")

etiketGecmis = Label(anaPencere, text="Geçmiş Tablosu", font="Times 20")

#Sayılar
but1=Button(anaPencere,text="1",width=2,height=2, bg="lightblue", font="Times 20", command=sayıYaz1)
but2=Button(anaPencere,text="2",width=2,height=2, bg="lightblue", font="Times 20", command=sayıYaz2)
but3=Button(anaPencere,text="3",width=2,height=2, bg="lightblue", font="Times 20", command=sayıYaz3)
but4=Button(anaPencere,text="4",width=2,height=2, bg="lightblue", font="Times 20", command=sayıYaz4)
but5=Button(anaPencere,text="5",width=2,height=2, bg="lightblue", font="Times 20", command=sayıYaz5)
but6=Button(anaPencere,text="6",width=2,height=2, bg="lightblue", font="Times 20", command=sayıYaz6)
but7=Button(anaPencere,text="7",width=2,height=2, bg="lightblue", font="Times 20", command=sayıYaz7)
but8=Button(anaPencere,text="8",width=2,height=2, bg="lightblue", font="Times 20", command=sayıYaz8)
but9=Button(anaPencere,text="9",width=2,height=2, bg="lightblue", font="Times 20", command=sayıYaz9)
but0=Button(anaPencere,text="0",width=2,height=2, bg="lightblue", font="Times 20", command=sayıYaz0)

#İslemler
butTopla=Button(anaPencere,text="+",width=2,height=2, bg="lightgreen", font="Times 20", command=islemTopla)
butCikar=Button(anaPencere,text="-",width=2,height=2, bg="lightgreen", font="Times 20", command=islemCikar)
butGecmisTablosuSil=Button(anaPencere, text="Geçmiş Tablosunu Temizle",width=18,height=1, bg="PeachPuff2", fg="gray1", font="Times 12", command=islemGecmisTablosuSil)
butGecmisiSil=Button(anaPencere, text="Geçmiş Bilgilerini Temizle",width=18,height=1, bg="PeachPuff3", fg="black", font="Times 12", command=islemGecmisiSil)
butCarp=Button(anaPencere,text="*",width=2,height=2, bg="lightgreen", font="Times 20", command=islemCarp)
butOndalıklıBol=Button(anaPencere,text="/",width=2,height=2, bg="lightgreen", font="Times 20", command=islemOndalıklıBol)
butTamSayiBol=Button(anaPencere,text="//",width=2,height=2, bg="lightgreen", font="Times 20", command=islemTamSayiBol)
butGecmisTablIslemAktar=Button(anaPencere,text="Geçmiş Tablosundan\nİşlem Aktar",width=16,height=3, bg="PeachPuff2", fg="gray1", font="Times 14", command=islemGecmisTablIslemAktar)
butGecmisTablSonucAktar=Button(anaPencere,text="Geçmiş Tablosundan\nSonuç Aktar",width=16,height=3, bg="PeachPuff2", fg="gray1", font="Times 14", command=islemGecmisTablSonucAktar)
butMod=Button(anaPencere,text="%",width=2,height=2, bg="lightgreen", font="Times 20", command=islemMod)
butIsaretDegistir=Button(anaPencere,text="+/-",width=2,height=2, bg="lightgreen", font="Times 20", command=islemIsaretDegistir)
butUsAl=Button(anaPencere,text="^",width=2,height=2, bg="lightgreen", font="Times 20", command=islemUsAl)
butSil=Button(anaPencere,text="<-",width=2, height=1, bg="black", fg="white", font="Times 15", command=islemSil)
butTamSil=Button(anaPencere,text="SİL",width=2, height=1, bg="white", fg="black", font="Times 15", command=islemTamSil)
butEsit=Button(anaPencere,text="=",width=2,height=2, bg="darkorange", font="Times 20", command=islemEsit)
butGecmisCikti=Button(anaPencere,text="Geçmiş Bilgilerin\nÇıktısını Al",width=13,height=3, bg="PeachPuff2", fg="gray1", font="Times 16", command=islemCiktiAl)


#Ekrana Koyma
but1.place(relx=0.01, rely=0.11)
but2.place(relx=0.12, rely=0.11)
but3.place(relx=0.23, rely=0.11)
but4.place(relx=0.01, rely=0.26)
but5.place(relx=0.12, rely=0.26)
but6.place(relx=0.23, rely=0.26)
but7.place(relx=0.01, rely=0.41)
but8.place(relx=0.12, rely=0.41)
but9.place(relx=0.23, rely=0.41)
but0.place(relx=0.01, rely=0.56)


butTopla.place(relx=0.34, rely=0.11)
butCikar.place(relx=0.45, rely=0.11)
butGecmisiSil.place(relx=0.56, rely=0.11)
butGecmisTablosuSil.place(relx=0.56, rely=0.18)
butCarp.place(relx=0.34, rely=0.26)
butOndalıklıBol.place(relx=0.45, rely=0.26)
butGecmisTablIslemAktar.place(relx=0.56, rely=0.26)
butTamSayiBol.place(relx=0.34, rely=0.41)
butGecmisTablSonucAktar.place(relx=0.56, rely=0.41)
butMod.place(relx=0.45, rely=0.41)
butIsaretDegistir.place(relx=0.12, rely=0.56)
butUsAl.place(relx=0.23, rely=0.56)
butSil.place(relx=0.35, rely=0.56)
butEsit.place(relx=0.45, rely=0.56)
butGecmisCikti.place(relx=0.57, rely=0.56)
butTamSil.place(relx=0.35, rely=0.63)

listEkran.place(relx=0.01,rely=0.01)
listeGecmis.place(relx=0.01,rely=0.81)

etiketGecmis.place(relx=0.01, rely=0.74)

###################################################################################
anaPencere.mainloop()

