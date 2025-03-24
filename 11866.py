from collections import deque

N, K = map(int, input().split())

queue = deque([i for i in range(1, N + 1)])
print("<", end="")
while len(queue) > 0:
    for _ in range(K - 1):
        a = queue.popleft()
        queue.append(a)
    if len(queue) == 1:
        print(f"{queue.popleft()}", end="")
    else:
        print(f"{queue.popleft()}, ", end="")
print(">")
