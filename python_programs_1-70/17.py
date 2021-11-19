# 17. Calculate income tax for the given income by adhering to the below rules
#     Taxable Income        Rate (in %)
#     First Rs.10,0000         0
#     Next Rs. 10,0000        10
#     The remaining           20

income=int(input("Enter your income"))
if income<=10000:
    print("Your tax is 0")
elif 10000<income<=20000:
    tax=(income-10000)*0.1
    print("Your tax is ",tax)
elif income>=20000:
    tax=(income-10000)*0.1 +(income-20000)*0.2
    print("Your tax is ",tax)