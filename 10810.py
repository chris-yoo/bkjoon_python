N, M = map(int, input().split())
range_lists = []
bag = [0] * N
for _ in range(M):
    a = map(int, input().split())
    range_lists.append(a)

for l in range_lists:
    a, b, num = l
    for i in range(a - 1, b):
        bag[i] = num

for i in bag:
    print(i, end=" ")
