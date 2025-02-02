N = int(input())

max_3 = N//3
max_5 = N//5
min_bag = float("inf")
res = float("inf")

for i in range(max_3+1):
    for j in range(max_5+1):
        if 3*i+5*j == N:
            if i+j <= res:
                res = i+j

if res == float("inf"):
    print(-1)
else:
    print(res)