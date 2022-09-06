N=int(input())
i=1
c=0
while i<N:
    if N%i==0:
        c+=i
    i+=1
if c>N:
    print('True')
else:
    print('False')
        