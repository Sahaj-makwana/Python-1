#13. Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% :  Grade F
''' 
a=int(input("Enter marks of Physics"))
b=int(input("Enter marks of Chemistry"))
c=int(input("Enter marks of Biology"))
d=int(input("Enter marks of Mathematics"))
e=int(input("Enter marks of Computer"))
total=a+b+c+d+e
avg=total/5
if avg>=90:
    print("Grade A")
elif avg>=80:
    print("Grade B")
elif avg>=70:
    print("Grade C")
elif avg>=60:
    print("Grade D")
elif avg>=40:
    print("Grade E")
else:
    print("Grade F")
