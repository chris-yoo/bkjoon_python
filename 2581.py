N = int(input())
M = int(input())

decimals = []

def is_decimal(num):
    res = []
    for i in range(1, num+1):
        if num%i == 0 :
            res.append(i)
    
    if len(res) == 2:
        return True
    else:
        return False
    
for i in range(N,M+1):
    if is_decimal(i):
        decimals.append(i)
    
if len(decimals) == 0:
    print(-1)
else:
    print(sum(decimals))
    print(min(decimals))