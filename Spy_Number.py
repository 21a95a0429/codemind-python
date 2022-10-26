n=int(input())
sum=0
pro=1
while n>0:
    s=n%10
    sum+=s
    pro*=s
    n=n//10
if sum==pro:
    print("Spy Number")
else:
    print("Not Spy Number")