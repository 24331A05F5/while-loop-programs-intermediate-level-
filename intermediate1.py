"""Check Palindrome Number"""
s = input("Enter a string: ")
i = 0
while i < len(s) // 2:
    if s[i] != s[len(s) - i - 1]:
        print("not a palindrome")
        break
    i += 1
else:
    print(" Palindrome")