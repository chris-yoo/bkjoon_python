A, B = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_B_intersect = set(A_list) & set(B_list)

print(len(A_list)+len(B_list)-len(A_B_intersect)*2)