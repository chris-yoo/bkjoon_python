a, b = map(int, input().split())
c, d = map(int, input().split())


def GCD(a, b):
    remainder = a % b
    if remainder == 0:
        return b
    else:
        return GCD(b, remainder)


def devided_by_GCD(a, b):
    gcd = GCD(a, b)
    return a // gcd, b // gcd


def cal_fraction(a, b, c, d):
    return a * d + b * c, b * d


res_1, res_2 = cal_fraction(a, b, c, d)
res_1, res_2 = devided_by_GCD(res_1, res_2)

print(f"{res_1} {res_2}")
