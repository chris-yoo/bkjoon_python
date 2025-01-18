def det_triangle(lengths):
    if (sum(lengths)-max(lengths)) <= max(lengths):
        return "Invalid"
    
    if max(lengths) == min(lengths):
        return "Equilateral"
    
    if lengths.count(max(lengths)) == 2 or lengths.count(min(lengths)) == 2:
        return "Isosceles"
    
    return "Scalene"

while True:
    lengths = list(map(int, input().split()))
    if lengths[0] == 0 and lengths[1] == 0 and lengths[2] == 0:
        break
    print(det_triangle(lengths))