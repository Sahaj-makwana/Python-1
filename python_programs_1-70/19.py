# 19. Program to find the digital product of a given number
#     ex: n=43   Digital product ----->4*3=12

n=int(input("Ente a no."))
f=n//10
l=n%10
pro=f*l
print("Digital product of entered no. is ",pro)