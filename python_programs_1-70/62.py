#62.Python program to display the sum of input (n) numbers using a list.

list1 = [41, 15, 7, 38, 13]
total=0
for i in range(0, len(list1)):
    total = total + list1[i]
 
print("Sum of all elements in given list: ", total)