"""Reverse a Number"""
n=int(input("enter a number:"))
c=n
a=0
while n>0:
    digit=n%10
    a=a*10+digit
    n=n//10
print("before reversing is ",c)
print("after reversing",c,"is",a)