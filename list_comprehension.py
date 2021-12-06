''' list comprehension examples'''

pow2 = [2 ** x for x in range(10)]
print(pow2)

print([x+y for x in ['Python ','C '] for y in ['Language','Programming']])

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

 
print('p' in my_list)
 
print('a' in my_list)
 
print('c' not in my_list)

for fruit in ['apple','banana','mango']:
    print("I like",fruit)


#  list methods *************
 
animals = ['cat', 'dog', 'rabbit']

 
wild_animals = ['tiger', 'fox']

 
animals.append(wild_animals)

print('Updated animals list: ', animals)  

currencies = ['Dollar', 'Euro', 'Pound']

# append 'Yen' to the list
currencies.append('Yen')

print(currencies)

vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')

print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')


print('The index of i:', index)

vowels = ['a', 'e', 'i', 'o', 'u']

# index of 'p' is vowels
index = vowels.index('p')

print('The index of p:', index)

# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

 
index = alphabets.index('e')    

print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)    

print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
index = alphabets.index('i', 3, 5)   

print('The index of i:', index)

# extend method

prime_numbers = [2, 3, 5]

 
numbers = [1, 4]

# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)


print('List after extend():', numbers)

# Output: List after extend(): [1, 4, 2, 3, 5]

languages = ['French']

# languages tuple
languages_tuple = ('Spanish', 'Portuguese')

# languages set
languages_set = {'Chinese', 'Japanese'}

# appending language_tuple elements to language
languages.extend(languages_tuple)


print('New Language List:', languages)

# appending language_set elements to language
languages.extend(languages_set)


print('Newer Languages List:', languages)

a = [1, 2]
b = [3, 4]

a += b     

print('a =', a)

a = [1, 2]
b = [3, 4]

a[len(a):] = b

print('a =', a)