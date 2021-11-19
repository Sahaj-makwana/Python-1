# 26. Program to find whether a given number is a strong number or not.
#     e.g. n=145
#     1!+4!+5!==145

num = int(input("Enter the Number:"))  
sum = 0  
temp = num  
  
while(temp > 0):  
    fact = 1  
    rem = temp % 10  
  
    for i in range(1, rem + 1):  
        fact = fact * i  
  
    print("Factorial of %d = %d" %(rem, fact))  
    sum = sum + fact  
    temp = temp // 10  
  
print("Sum of Factorials of a Given Number %d = %d" %(num, sum))  
      
if (sum == num):  
    print("The given number is a Strong Number")  
else:  
    print("The given number is not a Strong Number")  