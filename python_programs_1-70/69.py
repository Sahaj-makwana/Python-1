#69)Write a Python program to find all the values in a list are greater than a given number.
list1 = [520, 330, 400]
list2 = [24, 37, 11]
print(all(x >= 200 for x in list1))
print(all(x >= 15 for x in list2))