S = input()
bomb = input()
stack = []
bomb_len = len(bomb)
for c in S:
    stack.append(c)
    if "".join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

result = "".join(stack)
if len(result) == 0:
    print("FRULA")
else:
    print(result)
