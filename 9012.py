T = int(input())


def isVPS(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


for _ in range(T):
    s = input()
    print(isVPS(s))
