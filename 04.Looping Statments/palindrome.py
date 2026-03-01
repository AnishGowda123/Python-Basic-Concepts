num=int(input("Enter the number:"))
temp=num
rev=0
while num !=0:
    r=num%10
    rev=rev*10+r
    num=num//10
if temp==rev:
    print("yes its a palindrome")
else:
    print("not a palindrome")