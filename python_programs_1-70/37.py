#37. Write a Python program to count the number of characters (character frequency) in a string. 
#  Sample String : google.com'
#  Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

str1 = input("Enter a string :")
freq = {}
for i in str1:
    if i in freq:
        freq[i]+= 1
    else:
        freq[i] = 1

print(str(freq))            

