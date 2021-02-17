import math

def otaLuku():
	while True:
		luku1 = input("Anna ensimmäinen luku: ")
		luku2 = input("Anna toinen luku: ")
		try:
			tulos1 = int(luku1)
			tulos2 = int(luku2)

		except (TypeError, ValueError):
			print("Virheellinen syöte!")

		else:
			return tulos1, tulos2

def otaLuku2():
	while True:
		luku1 = input("Anna uusi ensimmäinen luku: ")
		luku2 = input("Anna uusi toinen luku: ")
		try:
			tulos1 = int(luku1)
			tulos2 = int(luku2)

		except (TypeError, ValueError):
			print("Virheellinen syöte!")

		else:
			return tulos1, tulos2
	

def main():
	x, y = otaLuku()
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
			print("Tulos on:", math.sin(x / y))
			continue
		if (z == 6):
			print("Tulos on:", math.cos(x / y))
			continue
		if (z == 7):
			x, y = otaLuku2()
			continue
		if (z == 8):
			break
		else:
			continue
	return

if __name__ == "__main__":
	main()
