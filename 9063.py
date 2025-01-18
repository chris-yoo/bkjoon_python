T = int(input())
X = []
Y = []
for i in range(T):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

max_x = max(X)
min_x = min(X)

max_y = max(Y)
min_y = min(Y)

if max_x == min_x or max_y == min_y:
    print(0)
else:
    print((max_x-min_x)*(max_y-min_y))