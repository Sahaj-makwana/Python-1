# list

my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list[0])  # p

print(my_list[2])  # o

print(my_list[4]) # e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])
 
print(my_list[-1])

print(my_list[-5])

my_list = ['p','r','o','f','e','s','s','i','o','n','a','l']

# includes element at index 2, 3, 4
# excludes element at index 5
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

print(odd) 
# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)
# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])

print(["re"] * 3)
# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)

print(odd)

odd[2:2] = [5, 7]

print(odd)
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete entire list
del my_list
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

 
print(my_list)

 
print(my_list.pop(1))

 
print(my_list)

 
print(my_list.pop())

 
print(my_list)

my_list.clear()

 
print(my_list)
#Finally, we can also delete items in a list by assigning an empty list to a slice of elements.
my_list = ['p','r','o','b','l','e','m']
my_list[2:3] = []
print(my_list)
 
my_list = [3, 8, 1, 6, 0, 8, 4]

 
print(my_list.index(8))

 
print(my_list.count(8))

my_list.sort()

 
print(my_list)

my_list.reverse()
 
print(my_list)