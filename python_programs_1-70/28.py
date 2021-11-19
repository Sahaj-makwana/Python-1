# 28. Program to find whether a given number is a perfect number or not.

x = int(input("Enter any number: "))
sum1 = 0
for i in range(1, x):
    if(x % i == 0):
        sum1 = sum1 + i
if (sum1 == x):
    print("Entered number is a Perfect number")
else:
    print("Entered number is not a Perfect number")