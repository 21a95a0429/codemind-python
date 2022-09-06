n=int(input())
m=int(input())
c=0
C=0
for g in range(1,n):
    if n%g==0:
        c+=g
    g+=1
for s in range(1,m):
    if m%s==0:
        C+=s
    s+=1
if n==C and m==c:
    print('Amicable')
else:
    print('Not Amicable')
        
        