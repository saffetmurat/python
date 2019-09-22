import datetime
import time

class Saat():

	def __init__(self):
		self.zamanAl()	
		
	def zamanAl(self):
		zaman = datetime.datetime.now()
		
		self.yil = zaman.year
		self.ay = zaman.month	
		self.gun = zaman.day
		self.saat = zaman.hour
		self.dakika = zaman.minute
		self.saniye = zaman.second	
	
	def yazdir(self):

		while True:
			print("\rTarih => {}/{}/{} --- Saat => {}:{}:{} ".format(self.gun, self.ay, self.yil, self.saat, self.dakika, self.saniye),end="")
			time.sleep(1)
			self.zamanAl()

if __name__ == "__main__":
	s = Saat()
	s.yazdir()

	