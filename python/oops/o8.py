class Demo:
    def show(self):
        print("instance show method")

    @classmethod
    def look(cls):
        print("class look method")

    @staticmethod
    def disp():
        print("disp static method")


d = Demo()

Demo().show()   # calling instance method using object
d.show()        # calling instance method using object reference

d.look()        # class method using object
d.disp()        # static method using object

# Demo.show()  # error (instance method needs object)

Demo.look()     # class method using class
Demo.disp()     # static method using class  