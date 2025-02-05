import sys

input = sys.stdin.readline

T = int(input())
nums = []
for _ in range(T):
    a = int(input())
    nums.append(a)

for i in sorted(nums):
    print(i)