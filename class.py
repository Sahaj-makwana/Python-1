class bio:
    pass
class person:
    age=20
    def greet(self):
        print("Hello")
obj=person()
print(obj.age)
obj.greet()

class bio_data:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name ="+ self.name)
        print("age =" , self.age)
obj1=pk("Sahaj",20)
obj1.show()

class MyClass:
  x = 3
p1 = MyClass()
print(p1.x)
