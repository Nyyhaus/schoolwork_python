class Emo:
	arvo = 0
	tila = "Toiminnassa"
	def nimi(self):
		print("Minä olen emoluokka.")


class Lapsi(Emo):
	def nimi(self):
		print("Minä olen lapsiluokka.")
		
def main():
	eka = Emo()
	print(eka.tila)
	eka.nimi()
	toka = Lapsi()
	print(toka.tila)
	toka.nimi()
	
if __name__ == "__main__":
	main()
