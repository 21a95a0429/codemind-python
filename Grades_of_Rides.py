H, S, s=map(int, input().split())
if H>50 and S>60 and s>100:
    print('10')
elif H>50 and S>60:
    print('9')
elif S>60 and s>100:
    print('8')
elif H>50 and s>100:
    print('7')
elif H>50 or S>60 or s>100:
    print('6')
else:
    print('5')
    