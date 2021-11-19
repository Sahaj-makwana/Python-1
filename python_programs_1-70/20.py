# 20. Find the sum of the series 3 +33 + 333 + 3333 + .. n terms


x=int(input("Enter the no. of which you want series "))
y=int(input("Enter the no. till which you want series "))
change = x
s = 0    #  initializing sum(s) to 0
for i in range(y):
   s += change  # adding change to s
   change = change * 10 + x   # updating the value of change
print(s)