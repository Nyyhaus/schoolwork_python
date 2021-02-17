from random import randint

print("Heitetään kolikkoa viidesti:")

i = 0

while i < 5:
	luku = randint(0,1)
	if luku == 0:
		print("Klaava!")
	else:
		print("Kruuna!")
	i += 1	
