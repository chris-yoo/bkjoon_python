nums = []

for _ in range(5):
    a = int(input())
    nums.append(a)
    
nums.sort()

print(int(sum(nums)/len(nums)))
print(nums[2])