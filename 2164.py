from collections import deque

N = int(input())
q = deque([i for i in range(1, N + 1)])

while len(q) > 0:
    if len(q) == 1:
        print(q[0])
        break

    q.popleft()
    if len(q) == 1:
        print(q[0])
        break

    a = q.popleft()
    q.append(a)
