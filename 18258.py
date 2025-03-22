from collections import deque
import sys

input = sys.stdin.readline

queue = deque()
T = int(input())

for _ in range(T):
    a = list(input().split())
    if len(a) == 2:
        queue.append(int(a[1]))
    else:
        if a[0] == "pop":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())
        if a[0] == "size":
            print(len(queue))
        if a[0] == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        if a[0] == "front":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        if a[0] == "back":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])
