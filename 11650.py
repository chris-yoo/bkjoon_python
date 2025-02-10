import sys

input = sys.stdin.readline

nums = []

T = int(input())

for _ in range(T):
    a, b = map(int, input().split(" "))
    nums.append((a,b))

key_x = sorted(nums, key = lambda x: (x[0],x[1]))

for num in key_x:
    print(f"{num[0]} {num[1]}")