#59. Program to return a function from another function.

def B():
	print("Inside the method B.")
	
def A():
	print("Inside the method A.")
	return B

returned_function = A()

returned_function()