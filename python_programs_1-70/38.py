#38 Write a Python program to change a given string to a new string where the second and last chars have been exchanged.

str1 = input("Enter a string :")
new_str = str1[0] + str1[-2] + str1[2:-2] + str1[1] + str1[-1]
print(new_str)