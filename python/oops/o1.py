class Student:
    def __init__(self, n, r, m):
        self.name = n
        self.roll = r
        self.mark = m

    def show(self):
        print("My name =", self.name)
        print("My rollno =", self.roll)
        print("My mark =", self.mark)

s1 = Student("muna", 1, 90)
s2 = Student("kuna", 2, 80)

s1.show()
s2.show()
