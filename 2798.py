from itertools import combinations
T, target = map(int, input().split())
num_list = list(map(int, input().split()))
combination_sets = combinations(num_list, 3)
large = 0

for set in combination_sets:
    a = sum(set)
    if a<=target and a>=large:
        large = a

print(large)