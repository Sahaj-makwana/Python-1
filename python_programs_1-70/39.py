#39 Write a Python program to remove the characters which have even index values of a given string.

str1 = input("Enter a string: ")
new_str = ''
for i in range(len(str1)):
    if i%2==0:
        new_str = new_str + str1[i]
        
print(new_str)        
