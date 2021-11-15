#10. A shop will give discount of 50% if the cost of purchased quantity is more than 10000. 
#Ask user for quantity suppose, one unit will cost 100. Judge and print total cost for user.
q=int(input("Enter the no. of quantity"))
amt=q*100
dis=((amt*50)/100)
t=amt-dis
if amt>10000:
    print("Your Product Cost is  ",t)
else:
    print("Your Product Cost is  ",amt)