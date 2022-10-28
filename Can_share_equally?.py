X, Y=map(int, input().split())
g=X*1
s=Y*2
r=g+s
if r%2==0  and (X>0 or Y%2==0):
    print('YES')
else:
    print('NO')