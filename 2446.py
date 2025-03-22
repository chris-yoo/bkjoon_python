T = int(input())

for i in range(T):
    print(" " * i, end="")
    print("*" * (2 * (T - i) - 1))

for i in range(1, T):
    print(" " * (T - i - 1), end="")
    print("*" * (2 * i + 1))
