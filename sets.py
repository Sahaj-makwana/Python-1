#1
my_set={1,2,3}
print(my_set)
{1, 2, 3}

#2
my_set={8.021620362654,"Apple",(10,20,30)}#Set can have only float int tuple string values as set's elements are immutable 
#but set itself is mutable
print(my_set)
{8.021620362654, 'Apple', (10, 20, 30)}
#3
my_set={1.123,"python",[1,2,3] }
#This code will give error as we know that the element of set is immutable and list is mutable
#so [1,2,3] can't be a element in set
my_set=([1,2,3]) #Here {} is not used so that why it is considered as list
print(my_set)
type(my_set)
#4
a={} #here empty {} will define dictionary to define set we have to use set function
print(a)
type(a)
{}
dict
#5
a=set()
print(a)
type(a)
set()
set
#6
my=set([1,2,3]) #Here it is accepting list but treating the each element of list as the element of set
print(my)
type(my)
{1, 2, 3}
set
#7
my=set()
my.add(2)
print(my)
{2}
#8
my.add(2) #set does not have duplicate value
print(my)
{2}
#9
my.update([1,2,3])
print(my)
{1, 2, 3}
#10
my.update({1,2,3}, {1,6,8})
print(my)
{1, 2, 3, 6, 8}
#11
my=set([1,2,3])
my.discard(3)
print(my)
{1, 2}
#12
my=set([1,2,3])
print(my)
my.pop()
{1, 2, 3}
1
#13
my=set("HelloWorld")
print(my)
{'W', 'd', 'r', 'H', 'e', 'l', 'o'}
#14
my=set([1,2,3])
my.clear()
print(my)
set()
#15
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A|B) # | is for union
{1, 2, 3, 4, 5, 6, 7, 8}
#16
A={1,2,3,4,5}
B={4,5,6,7,8}
A.union(B)
{1, 2, 3, 4, 5, 6, 7, 8}
#17
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A&B) # & is for intersection
{4, 5}
#18
A={1,2,3,4,5}
B={4,5,6,7,8}
A.intersection(B)
{4, 5}
#19
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A-B) # - is for difference
{1, 2, 3}
#20
A={1,2,3,4,5}
B={4,5,6,7,8}
A.difference(B)
{1, 2, 3}
#21
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A^B) # ^ is for symmetric difference
{1, 2, 3, 6, 7, 8}
#22
A={1,2,3,4,5}
B={4,5,6,7,8}
A.symmetric_difference(B)
{1, 2, 3, 6, 7, 8}
#23
A={1,2,3,4,5}
B={4,5,6,7,8}
print(1 in A) #This shows that sets are iterable
True
#24
my=set("Acropolis")
for letter in my:
  print(letter)
s
i
p
A
r
c
l
o
#25
my=set("banana")
for letter in my:
  print(letter)
b
n
a