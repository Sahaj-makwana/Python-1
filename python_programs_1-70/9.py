#9. Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum
x=int(input("Enter 1st no."))
y=int(input("Enter 2nd no."))
z=int(input("Enter 3rd no."))
sum=x+y+z
pro=sum*3
if x==y==z:
    print(pro)
else:
    print(sum)
