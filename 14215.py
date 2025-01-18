lengths = list(map(int, input().split()))

if sum(lengths)-max(lengths) > max(lengths):
    print(sum(lengths))
else:
    rescaled = sum(lengths)-max(lengths)-1
    print(sum(lengths)-max(lengths)+rescaled)