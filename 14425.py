N, M = map(int, input().split())
n_list = []
m_list = []
cnt = 0

for _ in range(N):
    a= input()
    n_list.append(a)
    
for _ in range(M):
    a= input()
    m_list.append(a)
    
for m in m_list:
    if m in set(n_list):
        cnt += 1
        
print(cnt)