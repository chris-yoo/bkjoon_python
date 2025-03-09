import sys

input = sys.stdin.readline

sieve = [True for _ in range(1000001)]
for i in range(2, 1000001):
    if sieve[i] == True:
        for j in range(i * 2, 1000001, i):
            sieve[j] = False


def solve_goldbach(n, sieve):
    count = 0
    for i in range(2, n // 2 + 1):
        if sieve[i] and sieve[n - i]:
            count += 1

    return count


T = int(input())
for _ in range(T):
    n = int(input())
    print(solve_goldbach(n, sieve))
