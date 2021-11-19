#35 Write a Python program to get a single string from two given strings, separated by a space and swap the first characters of each string.
#  Sample String : 'abc', 'xyz' 
#  Expected Result : 'xbc ayz'

str1 = input("Enter 1st string :")
str2 = input("Enter 2nd string :") 
new_str1 = str2[0] + str1[1: ]
new_str2 = str1[0] + str2[1: ]
print(new_str1 + " " + new_str2)