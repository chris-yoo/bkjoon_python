A, N = map(int, input().split())
res = []
for i in range(1,A+1):
    if A%i==0:
        res.append(i)

if len(res)<N:
    print(0)
else:
    print(res[N-1])