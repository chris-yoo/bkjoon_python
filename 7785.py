T = int(input())
log = {}
current_member = []

for _ in range(T):
    name, state = input().split()
    log[name] = state

for name in log:
    if log[name] == "enter":
        current_member.append(name)
    
for name in sorted(current_member, reverse=True):
    print(name)