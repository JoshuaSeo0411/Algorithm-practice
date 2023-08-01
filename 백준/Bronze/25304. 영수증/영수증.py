X = int(input())
N = int(input())
ls1 = []
ls2 = []
result = 0
for i in range(N):
    a, b = map(int, input().split())
    ls1.append(a)
    ls2.append(b)
    y = ls1[i] * ls2[i]
    result = result + y
if result == X:
    print("Yes")
else:
    print("No")