class Demo:
    # classmethod can be called by class or object
    @classmethod
    def show(cls):
        print("Hi")
# Calling by class
Demo.show()
# Creating object
d = Demo()
# Calling by object
d.show()