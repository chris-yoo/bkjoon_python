from collections import deque

N = int(input())
nums = list(map(int, input().split()))
balloons = deque((i + 1, num) for i, num in enumerate(nums))

result = []

while balloons:
    idx, move = balloons.popleft()
    result.append(idx)

    if not balloons:
        break

    if move > 0:
        balloons.rotate(-(move - 1))
    else:
        balloons.rotate(-move)

print(*result)
