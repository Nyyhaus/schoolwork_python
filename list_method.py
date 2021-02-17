tiedosto = open("sanoja.txt", "r")

sisalto = tiedosto.readlines()

lista = []
for i in sisalto:
	i = i[:-1]
	lista.append(i)
lista.sort()
print("Sanat laitettuna aakkosjärjestykseen:")
for i in lista:
	print(i)
