a_1, a_0 = map(int, input().split())
c = int(input())
n_0 = int(input())

def is_big_o (a_1,a_0,c,n_0):
    f = a_1*n_0+a_0
    g = c*n_0
    
    if a_1 > c:
        return 0
    
    if f<=g:
        return 1
    else:
        return 0

print(is_big_o (a_1,a_0,c,n_0))