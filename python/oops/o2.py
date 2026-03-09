class Simple:
    def __init__(self, p, rate, time):
        self.p = p
        self.rate = rate
        self.time = time

    def show(self):
        print("principal =", self.p)
        print("rate =", self.rate)
        print("time =", self.time)

    def sical(self):
        return self.p * self.rate * self.time / 100


i1 = Simple(1000, 10, 2)

i1.show()

print("Simple interest =", i1.sical())