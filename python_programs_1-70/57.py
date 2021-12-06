#57.Write a Python function  to check whether the given integer is a prime number or not.
num = 13
flag = False
def prime(n):
  flag1=False
  if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag1 = True
            break
  return flag1

flag=prime(num)
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")