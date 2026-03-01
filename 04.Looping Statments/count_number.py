num=int(input("Enter the number:"))
count=int(input("Enter the count:"))
while num != 0:
    num=num//10
    count+=1
print(count)