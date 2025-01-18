N = int(input())
decimals = []

def divide_by_divisor(num,decimals):
    if num == 1:
        return 1
    for i in range(2,num+1):
        if num%i == 0:
            decimals.append(i)
            return num//i

while True:
    N = divide_by_divisor(N,decimals)
    if N == 1:
        break

if len(decimals) == 0:
    print()
else:
    for i in decimals:
        print(i)
