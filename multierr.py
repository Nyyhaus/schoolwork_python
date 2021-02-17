def otaTiedosto():
	tiedosto = input("Anna tiedoston nimi: ")
	return tiedosto

def main():
	tiedosto1 = otaTiedosto()
	try:
		sisalto = open(tiedosto1, "r")
		sisalto = sisalto.read()
		tulos = int(sisalto)
		tulos += 313
	
	except (TypeError, ValueError):
		print("Tiedoston sisältö virheellinen!")

	except (TypeError, IOError):
		print("Virheellinen tiedostonnimi")

	else:
		print(f"Saatiin tulos {tulos}")

if __name__ == "__main__":
	main()
