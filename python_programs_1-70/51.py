#51. Write a function that returns the middle value among three integers. (Hint: make use of min() and max()). Write code to test this function with different inputs.

def middleOfThree(x, y, z) :
	if x > y :
		if (y > z):
			return y
		elif (x > z) :
			return z
		else :
			return x
	else:
		if (x > z) :
			return x
		elif (y > z) :
			return z
		else :
			return y

x = 20
y = 45
z = 40
print( middleOfThree(x, y, z) )