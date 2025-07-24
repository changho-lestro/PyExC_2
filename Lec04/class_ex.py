class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

p1 = Person("John",36)
print(p1.name,"\n",p1.age)
p1.myfunc()

p2 = Person("Emily", 30)
p2.age = 40
p2.myfunc()


