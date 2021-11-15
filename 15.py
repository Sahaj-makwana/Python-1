15. Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill
'''
unit=int(input("Enter total units consumed: "));
if(unit <= 50):
    amt = unit * 0.50
elif(unit <= 150):
    amt = 25 + ((unit-50) * 0.75)    
elif(unit <= 250):
    amt = 100 + ((unit-150) * 1.20)
else:
    amt = 220 + ((unit-250) * 1.50)
    
sur_charge = amt * 0.20
total_amt  = amt + sur_charge

print("Electricity Bill ", total_amt)