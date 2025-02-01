T = int(input())
cnt = 0
num = 666

def is666Num(a):
    if len(a) == 1 and len(a)==2:
        return False
    cnt = 0
    for i in range(len(a)-2):
        if a[i:i+3] == "666":
            cnt +=1
    if cnt > 0:
        return True

while True:
    if is666Num(str(num)):
        cnt += 1
        
    if cnt == T:
        print(num)
        break
    
    num += 1
        