class Kilpailija:
	"""Kilpailija: sisältää pisteet ja värin"""
	vari = ""
	pisteet = 0
	def tilanne(self):
		print(f"Olen {self.vari} ja minulla on {self.pisteet} pistettä!")
		
	def __init__(self):
		self.vari = input("Anna minulle väri: ")


def main():
	eka = Kilpailija()
	toka = Kilpailija()
	eka.tilanne()
	toka.tilanne()
	print(eka.__doc__)
	
	
if __name__ == "__main__":
	main()
