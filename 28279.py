import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
deck = deque()

for _ in range(N):
    a = list(map(int, input().split()))
    if len(a) > 1:
        if a[0] == 1:
            deck.appendleft(a[1])
        else:
            deck.append(a[1])
    else:
        if a[0] == 3:
            if len(deck) == 0:
                print(-1)
            else:
                print(deck.popleft())

        if a[0] == 4:
            if len(deck) == 0:
                print(-1)
            else:
                print(deck.pop())

        if a[0] == 5:
            print(len(deck))

        if a[0] == 6:
            if len(deck) == 0:
                print(1)
            else:
                print(0)

        if a[0] == 7:
            if len(deck) == 0:
                print(-1)
            else:
                print(deck[0])

        if a[0] == 8:
            if len(deck) == 0:
                print(-1)
            else:
                print(deck[-1])
