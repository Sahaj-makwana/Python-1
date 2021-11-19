# 21. Print the following pattern
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''

for i in range(1,6):
    for j in range(1,i+1):
        print("*" , end=" ")
    print()

for i in range(6, 1, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")