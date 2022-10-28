x=int(input())
for i in range(0,x):
    N, A, B, K=map(int,input().split())
    L=0
    if(A%B==0):
        l=A
    elif(B%A==0):
        l=B
    else:
        l=A*B
    f=N//l
    c=N//A
    d=N//B
    c=c-f
    d=d-f
    if c+d>=K:
        print('Win')
    else:
        print('Lose')