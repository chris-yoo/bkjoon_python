# 6 = 1 + 2 + 3
# 12 is NOT perfect.
# 28 = 1 + 2 + 4 + 7 + 14

def calCompleteNum(N):
    res = []
    for i in range(1,N+1):
        if N % i == 0 and N != i:
            res.append(i)
        
    if len(res) == 0 or sum(res) != N:
        print(f"{N} is NOT perfect.")
        
    else:
        print(f"{sum(res)} =", end = " ")
        for i in range(len(res)-1):
            print(f"{res[i]} +", end=" ")
        print(res[i+1])

while True:
    N = int(input())
    if N == -1:
        break
    calCompleteNum(N)
    