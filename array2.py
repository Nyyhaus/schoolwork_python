lista = []

while True:
	print("Haluatko")
	print("(1)Lisätä listaan")
	print("(2)Poistaa listalta vai ")
	z = int(input("(3)Lopettaa?: "))
	if z == 1:
		lisaa = input("Mitä lisätään?: ")
		lista.append(lisaa)
		continue
	if z == 2:
		montako = len(lista)
		print(f"Listalla on {montako} alkiota.")
		poista = int(input("Monesko niistä poistetaan?: "))
		try:
			lista.pop(poista)
			
		except Exception:
			print("Virheellinen valinta.")
		
		continue
	if z == 3:
		print("Listalla oli tuotteet:")
		for i in lista:
			print(i)
		break
	else:
		print("Virheellinen valinta.")
