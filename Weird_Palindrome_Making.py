T=int(input())
for i in range(T):
    G=0
    N=int(input())
    A=list(map(int,input().split()))
    S=len(A)
    for j in range(0,S):
        if A[j]%2!=0:
            G+=1
    print(G//2)