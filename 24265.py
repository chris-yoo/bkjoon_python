T = int(input())

def timeComplexity(n):
    cnt = [i for i in range(1,n)]
    return sum(cnt)
        

print(timeComplexity(T))
print(2)