def isBalance(a):
    stack = []
    for c in a:
        if c == "[":
            stack.append(c)
        elif c == "(":
            stack.append(c)
        elif c == "]":
            if len(stack) == 0:
                return "no"
            if stack[-1] == "[":
                stack.pop()
            else:
                return "no"
        elif c == ")":
            if len(stack) == 0:
                return "no"
            if stack[-1] == "(":
                stack.pop()
            else:
                return "no"
        else:
            continue

    if len(stack) != 0:
        return "no"
    else:
        return "yes"


while True:
    a = input()
    if a == ".":
        break
    else:
        print(isBalance(a))
