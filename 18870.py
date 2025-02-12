import sys

input = sys.stdin.readline

T = int(input())

nums = list(map(int, input().split(" ")))

sorted_nums = sorted(list(set(nums)))
mapping_dict = {value: index for index, value in enumerate(sorted_nums)}

for num in nums:
    print(mapping_dict[num], end=" ")
    
    