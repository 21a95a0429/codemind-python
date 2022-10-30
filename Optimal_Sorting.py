T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int, input().split()))
    S=sorted(A)
    if S==A:
        print(0)
    else:
        print(max(S)-min(S))