a, b = map(int, input().split())

def GCD(a,b):
    remainder = a%b
    if remainder == 0:
        return b
    else:
        return GCD(b,remainder)
    
def LCM(a,b):
    return (a*b)//GCD(a,b)

print(LCM(a,b))