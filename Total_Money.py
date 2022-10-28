T=int(input())
for k in range(T):
    D,d,p,Q=map(int,input().split())
    n=D//d
    n2=D%d
    s=0
    for i in range(n):
        s+=(p+i*Q)*d
    s+=(p+n*Q)*n2
    print(s)