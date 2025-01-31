N, M = map(int, input().split())

chess_arr = []
sub_chess = []
res = float('inf')

for i in range(N):
    a = input().strip()
    chess_arr.append(a)

for i in range(N - 7):
    for j in range(M - 7):
        sub = [row[j:j + 8] for row in chess_arr[i:i + 8]]
        sub_chess.append(sub)

def cal_minma(sub):
    cnt1 = 0  
    cnt2 = 0  
    
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:  
                if sub[i][j] != 'B':
                    cnt1 += 1
                if sub[i][j] != 'W':
                    cnt2 += 1
            else:  
                if sub[i][j] != 'W':
                    cnt1 += 1
                if sub[i][j] != 'B':
                    cnt2 += 1

    return min(cnt1, cnt2)

for s in sub_chess:
    res = min(res, cal_minma(s))
    
print(res)
