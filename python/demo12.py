a=10
b=float
print(id(a),id(b))
print(a,b)
a=10
print(id(a),a)
a=20
print(id(a),a)

a=10
print(id(a))
print(a)
b=10
print(id(b))
print(b)

a=10
print(id(b),b)
b=10
print(id(b),b)

a=10
b=20
print("before swapping a=",a,"b=",b)
t=a
a=b
b=t
print("after swapping a=",a,"b=",b)

a=10
b=2.5
c="hi"
print (a,b,c)

a=10
b=20
c=30
print("before swapping:")
print("a =",a)
print("b =",b)
print("c =",c)
temp=float
a=b
b=c
c=temp
print("\nAfter swapping (left to right):")
print("a=",a)
print("b=",b)
print("c=",c)

print(3==4)
print(2<3==5<<7)

print("e" in "hell0")
print("x" in "hello")
print("x" not in "hello")
print(10 in [10,20,30,10])

a=10
b=10
c=20
print(a is b)
print(a is c)
print(a is not c)

a=[10]
b=[10]
c=[20]
print(a is b)
print(a is c)
print(a is not c)
print(a==b)








