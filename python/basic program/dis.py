#write a python program to calculate discounted price.
print("enter price")
price=float(input())
print("enter discount percentage")
disc=float(input())
final=price-(price*disc/100)
print("finalprice=",final)
