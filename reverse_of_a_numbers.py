n=int(input())
s=0
m=n
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
print(s)