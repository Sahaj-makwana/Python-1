# 29. Program to find whether a given number is a prime number or not.

x = int(input("Enter any number: "))
flag=0
for i in range(2,x):
    if x % i == 0:
        flag=1
        break
    
if(flag==1):
    print("Entered number is a not prime number")
else:
    print("Entered number is a prime number")