import math
def area (a,b,c):
    s=(a+b+c)/2
    ar=math.sqrt(s*(s-a)*(s-b)*s-c)
    print("area triangle=",ar)
area(2,3,4)


def li_as_arg(li):
    for i in li:
        print(i)

list=[1,2,3,4,7,5,6]
li_as_arg(list) 

def fact(n):
    if(n==1):
        return n
    else:
        return (n*fact(n-1))

n=5
print("factorial of {0} is {1}".format(n,fact(n)))

x = "red" 
def myfunc():
  x = "blue" 
  print("x with value {0} is local here ".format(x))

myfunc()
print("x with value {0} is global ".format(x))

x = "Sahaj"
def myfunc():
    global x   
    x = "Sahaj Makwana" 
    print("x with value {0} is also accessing global variable here ".format(x))

myfunc()
print("x with value {0} is global ".format(x))
