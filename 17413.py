s = input().strip()

is_reverse = True
blank_cnt = 0
words = []
for c in s:
    if c == " ":
        print("".join(words[::-1]), end="")
        print(" ", end="")
        words = []
    elif c == "<":
        if words:
            print("".join(words[::-1]), end="")
            words = []
        is_reverse = False
        print("<", end="")
    elif c == ">":
        is_reverse = True
        print(">", end="")
    else:
        if is_reverse == False:
            print(c, end="")
        else:
            words.append(c)
if words:
    print("".join(words[::-1]), end="")
