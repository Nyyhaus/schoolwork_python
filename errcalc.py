def otaLuku():
	while True:
		luku1 = input("Anna luku: ")
		try:
			tulos1 = int(luku1)

		except (TypeError, ValueError):
			print("Virheellinen syöte!")

		else:
			return tulos1
	

def main():
	x = otaLuku()
	y = otaLuku()
	while True:
		print("(1) +")
		print("(2) -")
		print("(3) *")
		print("(4) /")
		print("(5)sin(luku1/luku2)")
		print("(6)cos(luku1/luku2)")
		print("(7)Vaihda luvut")
		print("(8)Lopeta")
		print("Valitut luvut:", x, y)
		z = int(input("Tee valinta (1-8):"))
		if (z == 1):
			print("Tulos on:", x + y)
			continue
		if (z == 2):
			print("Tulos on:", x - y)
			continue
		if (z == 3):
			print("Tulos on:", x * y)
			continue
		if (z == 4):
			print("Tulos on:", x / y)
			continue
		if (z == 5):
			print("Tulos on:", sin(x / y))
			continue
		if (z == 6):
			print("Tulos on:", cos(x / y))
			continue
		if (z == 7):
			x = otaLuku()
			y = otaLuku()
			continue
		if (z == 8):
			break
		else:
			continue
	return

if __name__ == "__main__":
	main()
