N = int(input())
T = len(str(N))

for i in range(max(1, N-9*len(str(N))),N+1):
    t_str = list(map(int, str(i)))
    target = i + sum(t_str)
    if target == N:
        print(i)
        break

else:
    print(0)