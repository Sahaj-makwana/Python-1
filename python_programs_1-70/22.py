# 22. Program to reverse a given Number.    ex: n=123   Reversed no is 321

num = int(input("enter a no."))
rev = 0

while num != 0:
    digit = num % 10
    rev= rev*10 + digit
    num //= 10

print("Reversed Number: "+ str(rev))