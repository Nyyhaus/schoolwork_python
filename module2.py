def testaa(testattava):
	if len(testattava) < 6 or testattava.isalpha() == True or testattava.isdigit() == True:
		return False
	else:
		return True
