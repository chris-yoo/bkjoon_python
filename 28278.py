import sys

input = sys.stdin.readline
T = int(input())
stack = []

for _ in range(T):
    a = list(map(int, input().split()))
    op = a[0]

    if op == 1:
        stack.append(a[1])
    elif op == 2:
        print(stack.pop() if stack else -1)
    elif op == 3:
        print(len(stack))
    elif op == 4:
        print(1 if not stack else 0)
    elif op == 5:
        print(stack[-1] if stack else -1)
