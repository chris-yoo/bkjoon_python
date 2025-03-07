# 시간초과 코드
# def isPrimeNum(n):
#     if n < 2:
#         return False

#     n_sqrt = int(n**0.5)

#     for i in range(2, n_sqrt + 1):
#         if n % i == 0:
#             return False
#     return True


# def findNumberOfPrimeNum(n):
#     cnt = 0
#     for i in range(n + 1, 2 * n + 1):
#         if isPrimeNum(i):
#             cnt += 1
#     return cnt


def findNumberOfPrimeNum(n):
    sieve = [True] * (2 * n + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int((2 * n) ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, 2 * n + 1, i):
                sieve[j] = False

    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if sieve[i]:
            cnt += 1

    return cnt


while True:
    n = int(input())
    if n == 0:
        break
    print(findNumberOfPrimeNum(n))
