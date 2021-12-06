54.Write a program to create a recursive function to calculate the product of numbers from 10 to 100.

def recur(n):
   if n == 10:
       return n
   else:
       return n*recur(n-1)

print("the product of numbers from 10 to 100 : " "is", recur(100))