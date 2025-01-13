# A, B, V = map(int, input().split())
# day = 0
# D = 0
# while D < V:
#     day+=1
#     D += A
#     if D >= V:
#         break
#     D -= B

# print(day)
# 시간 초과

import math

A, B, V = map(int, input().split())
day = 0

if A>=V:
    print(1)
else:
    day = math.ceil((V-A)/(A-B)+1)
    print(day)