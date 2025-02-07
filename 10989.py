import sys

input = sys.stdin.readline

T = int(input())
cnt = [0]*10001

for i in range(T):
    a = int(input())
    cnt[a] = cnt[a]+1

for i in range(10001):
    if cnt[i]>0:
        for _ in range(cnt[i]):
            print(i)