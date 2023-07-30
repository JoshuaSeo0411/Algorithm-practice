A, B, C = map(int, input().split())
ls = [A, B, C]

if A == B == C:
    print(10000+A*1000)
elif A == B or B == C:
    print(1000+B*100)
elif A == C:
    print(1000+A*100)
elif A != B != C:
    print(max(ls)*100)