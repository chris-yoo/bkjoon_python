def isPrimeNum(n):
    if n < 2:
        return False
    bound = int(n**0.5)
    for i in range(2, bound + 1):
        if n % i == 0:
            return False
    return True


M, N = map(int, input().split())

for i in range(M, N + 1):
    if isPrimeNum(i):
        print(i)
