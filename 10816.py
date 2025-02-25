N = int(input())
N_list = map(int, input().split())
M = int(input())
M_list = map(int, input().split())

N_dict = {}

for n in N_list:
    if N_dict.get(n) == None:
        N_dict[n] = 1
    else:
        N_dict[n] += 1
        
for m in M_list:
    if N_dict.get(m) == None:
        print(0, end =" ")
    else:
        print(N_dict[m], end = " ")