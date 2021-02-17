import time

while True:
	print("(1) Lue muistikirjaa")
	print("(2) Lisää merkintä")
	print("(3) Tyhjennä muistikirja")
	print("(4) Lopeta")
	z = int(input("Mitä haluat tehdä?:"))
	if z == 1:
		muistikirja = open("muistio.txt", "r")
		print(muistikirja.read())
		muistikirja.close()
		continue
	if z == 2:
		muistikirja = open("muistio.txt", "a")
		sisalto = input("Kirjoita uusi merkintä:")
		sisalto += ":::" + time.strftime("%X %x")
		muistikirja.write(sisalto)
		muistikirja.close()
		continue
	if z == 3:
		muistikirja = open("muistio.txt", "w")
		muistikirja.close()
		print("Muistio tyhjennetty.")
		continue
	if z == 4:
		print("Lopetetaan.")
		break

	
