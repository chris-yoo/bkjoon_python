T = int(input())
nums = []
for i in range(T):
    a = int(input())
    nums.append(a)

nums.sort()

for i in nums:
    print(i)
