# factor
# multiple
# neither

# 8 16
# 32 4
# 17 5
# 0 0

import sys

def determine_factor(A,B):
    if A==0 or B==0:
        return "neither"
    else:
        if B%A == 0:
            return "factor"

        elif A%B == 0:
            return "multiple"
        
        else:
            return "neither"

for line in sys.stdin:
    A, B = map(int, line.split())
    if A == 0 and B == 0:
        break
    print(determine_factor(A,B))


