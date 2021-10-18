'''LAMBDA FUNCTION'''

#Program to find cube of number

cube = lambda x: x **3
print("Cube :- ",cube(20))


#Program to print table

table = [lambda x=x: x * 13 for x in range(1, 11)]
for t in table:
    print(t())


#Program to find smallest number

Min = lambda a,b: y if (a > b) else a
print("Minimum number is :- ",Min(1131,1461))


# Program to find even number using  filter() with lambda()

List = [29, 11, 35, 61 65, 74, 83, 129, 146, 177]
FL = list(filter(lambda x: (x % 2 == 0), List))
print("List of even number :- ",FL)


# Program to filter marks greater then 80

marks = [55, 48, 80, 88, 85, 75, 95, 72, 90 ]
M = list(filter(lambda mk: mk >= 80, marks))
print("Marks greater then 80 are :- ",M)


# Program to get double of a Number using map() with lambda() .

l = [7, 6, 42, 87, 64, 52, 67, 33, 63, 31]
dl = list(map(lambda x: x * 2, l))
print("List of double of a Number",dl)
