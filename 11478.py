s = input()

s_dict = {}

for length in range(1,len(s)+1):
    for i in range(len(s)-length+1):
        a = s[i:i+length]
        if s_dict.get(a) == None:
            s_dict[a] = 1
        else:
            s_dict[a] += 1

print(len(list(s_dict.keys())))