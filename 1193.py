a = int(input())
num = 0
cnt = 1

while num<a:
    num+=cnt
    cnt+=1

layer = cnt
a_th = num-a+1

if layer%2 == 1:
    print(f"{layer-a_th}/{a_th}")
else:
    print(f"{a_th}/{layer-a_th}")



