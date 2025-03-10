# N = int(input())


# def isSquareNum(n):
#     return n**0.5 == int(n**0.5)


# def numOfOne(N):
#     cnt = 0
#     for i in range(1, N + 1):
#         if isSquareNum(i):
#             cnt += 1

#     return cnt


# print(numOfOne(N))
# 시간초과 코드이다.

# N의 제곱수의 정수부분과 같다

N = int(input())


def numOfOne(N):
    return int(N**0.5)


print(numOfOne(N))
