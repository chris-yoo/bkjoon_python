T = int(input())

num_list = []
prime_num_list = []

for _ in range(T):
    a = int(input())
    num_list.append(a)


def isPrimeNum(n):
    if n < 2:
        return False
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False

    return True


def find_next_prime(n):
    while not isPrimeNum(n):
        n += 1
    return n


for i in num_list:
    print(find_next_prime(i))
