class Simple:
    def __init__(self, p, rate, time):
        self.p = p
        self.rate = rate
        self.time = time

    def show(self):
        print("priniple =", self.p)
        print("rate =", self.rate)
        print("time =", self.time)

    def sical(self):
        return self.p * self.rate * self.time / 100
print("enter priniple rate and time")
#i1=Simple(float(input()),float(input()),float(input()))
pr=float(input())
r=float(input())
t=float(input())
i1=Simple(pr,r,t)
i1.show()
print("Simple interest =", i1.sical())