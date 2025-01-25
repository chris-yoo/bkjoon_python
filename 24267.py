T = int(input())

def cal_sequence(num):
    res = [0]
    for i in range(1, num-1):
        res.append(res[-1]+i)
    return res

print(sum(cal_sequence(T)))
print(3)