class Person:
    def f1(self):
        print(" sita is Person class")

class Student:
    def f2(self):
        print("sita is Student class")

class EngineeringStudent(Person, Student):
    def f3(self):
        print("sita is Engineering Student class")

obj = EngineeringStudent()

obj.f1()
obj.f2()
obj.f3()