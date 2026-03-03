"""Sum of Digits"""
n=input("enter a number: ")
s=0
i=0
while i<len(n):
    s=s+int(n[i])
    i+=1
print("Sum of digits of",n,"is:",s)

"""n = int(input("Enter a number: "))
s = 0
while n > 0:
    digit = n % 10
    s += digit
    n //= 10
print("Sum of digits:", s)"""