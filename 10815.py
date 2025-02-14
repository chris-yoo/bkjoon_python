N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

union_set = set(n_list)&set(m_list)

for m in m_list:
    if m in union_set:
        print(1,end=" ")
    else:
        print(0,end=" ")