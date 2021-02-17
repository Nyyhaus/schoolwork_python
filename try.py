def otaluku():
	luku = input("Anna luku: ")
	return luku

def main():
	luku1 = otaluku()
	try:
		tulos = int(luku1)
	
	except Exception:
		print("Virheellinen syöte!")
	
	else:
		print("Syöte oli kelvollinen.")

if __name__ == "__main__":
	main()
