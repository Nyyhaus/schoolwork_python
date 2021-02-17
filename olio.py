class Kilpailija:
	"""Luokka määrittelee tilanteen ja maalit"""
	vari = ""
	pisteet = ""
	def tilanne(self):
		print(f"Olen {self.vari} ja minulla on {self.pisteet} pistettä!")
	def maali(self):
		self.pisteet =+ 1
	
eka = Kilpailija()
eka.pisteet = 10
eka.vari = "sininen"

def main():
	eka = Kilpailija()
	eka.vari = "sininen"
	eka.maali()
	eka.tilanne()

if __name__ == "__main__":
	main()
