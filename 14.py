#14. Take input of age of 3 people by user and determine oldest and youngest among them.
person1 = int(input("Enter age of person 1 : "))
person2 = int(input("Enter age of person 2 : "))
person3 = int(input("Enter age of person 3 : "))

# check oldest
if person1 > person2 and person1 > person3:
    print("Person 1 is oldest")
elif person2 > person1 and person2 > person3:
    print("Person 2 is oldest")
elif person3 > person1 and person3 > person2:
    print("Person 3 is oldest")

# check youngest
if person1 < person2 and person1 < person3:
    print("Person 1 is youngest")
elif person2 < person1 and person2 < person3:
    print("Person 2 is youngest")
elif person3 < person1 and person3 < person2:
    print("Person 3 is youngest")