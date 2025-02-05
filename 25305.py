T,K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
print(nums[K-1])