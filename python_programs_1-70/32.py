# 32. Print  following pattern: 
'''
1
12
123
1234
12345
123456
1234567
12345678
123456789
'''

for i in range(1,10):
    for j in range(1,i+1):
        print(j,end="")
    print()
