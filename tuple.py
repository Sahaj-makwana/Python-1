
# Creating tuple

tupl = ('Sahaj', 'Makwana')
print (tupl)



# printing the length of a tuple

print("\nLength of tuple is ",len(tupl))



# concatenating 2 tuples
tupl1 = ('CI',1)
tupl2 = tupl+tupl1
print("\nConcatenated Tuple :- ", tupl2)



# creating nested tuples

tupl3 = (tupl, tupl1)
print("\nNested tuple:- ",tupl3)


# Slicing in Tuples

print(tupl2[1:])
print(tupl2[::-1])
print(tupl2[2:4])



# Code for converting a list and a string into a tuple

List = ['CI','CS','EC','CO','IT']
print(tuple(List))
print(tuple('Sahaj'))
