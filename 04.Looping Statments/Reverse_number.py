a=1234
rev=0
temp=a
while a!=0:
    r=a%10
    rev=rev*10+r
    a=a//10
print(rev)
if temp==rev:
    print("yes its a palindrome")
else:
    print("not a palindrome")