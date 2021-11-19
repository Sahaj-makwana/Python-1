# 33. Print following pattern: 
'''
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH
'''

for i in range(65,73):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()