# 27. Program to find whether a given number is a unique number.
#     For example, 20, 56, 9863, 145, etc. are the unique numbers while 33, 121, 900, 1010, etc. are not unique numbers

x= list(map(int,input("Enter a number: ").split()))
x1=[]
for i in x:
    if i not in x1:
        x1.append(i)
if len(x)==len(x1):
    print("Entered number is Unique Number")
else:
    print("Entered number is not Unique Number")