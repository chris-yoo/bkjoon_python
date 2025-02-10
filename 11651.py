import sys
input = sys.stdin.readline

T = int(input())
nums = []

for _ in range(T):
    x,y  = map(int, input().split(" "))
    nums.append((x,y))

new_nums = sorted(nums, key = lambda x: (x[1], x[0]))

for num in new_nums:
    print(f"{num[0]} {num[1]}")