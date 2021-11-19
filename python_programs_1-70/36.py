#36 Write a Python program to add 'polis' at the end of a given string (length should be at least 3).
#   If the given string already ends with 'polis' then add 'polisCS' instead.
#   If the string length of the given string is less than 3, leave it unchanged. 
#  Sample String : 'abc'
#  Expected Result : 'abcpolisCS' 
#  Sample String : 'Acropolis'
#  Expected Result : 'AcropolisCS'

str = input("Enter a string : ")

if len(str)<3:
    print(str)
elif str[-5:]=='polis':
    print(str+'CS')
else:
    print(str+'polis')
