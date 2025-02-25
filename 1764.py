N,M = map(int, input().split())
N_list = []
M_list = []

for _ in range(N):
    a = input()
    N_list.append(a)
    
for _ in range(M):
    a = input()
    M_list.append(a)
    
N_M_list = sorted(list(set(N_list) & set(M_list)))

print(len(N_M_list))

for n in N_M_list:
    print(n)