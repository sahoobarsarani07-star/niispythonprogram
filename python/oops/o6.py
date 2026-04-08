class Demo:
    # staticmethod it call by class name
    @staticmethod
    def show():
        print("hi")
Demo.show()   # call by class name
d = Demo()
d.show()      # call by object