T = int(input())

n_list = []

for _ in range(T):
    a,b = map(int, input().split())
    n_list.append((a,b))

def GCD(a,b):
    remainder = a%b
    if remainder == 0:
        return b
    else :
        return GCD(b,remainder)
    
def LCM(a,b):
    g = GCD(a,b)
    return (a*b)//g

for a,b in n_list:
    print(LCM(a,b))