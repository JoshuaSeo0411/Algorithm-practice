N = int(input())
ls = list(map(int, input().split()))
v = int(input())
count = 0

for i in range(N):
    if ls[i] == v:
        count += 1
print(count)