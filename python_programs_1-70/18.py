# 18. Program to find digital sum of a given Number
#     ex: n=123  Digital sum----->1+2+3=6

n=int(input("Ente a no."))
f=n//100
m=n%100//10
l=n%10
sum=f+m+l
print("Digital Sum of entered no. is ",sum)