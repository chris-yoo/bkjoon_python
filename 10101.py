angles = []
for i in range(3):
    a = int(input())
    angles.append(a)

if sum(angles) != 180:
    print("Error")

elif max(angles) == 60:
    print("Equilateral")

elif angles.count(min(angles))==2 or angles.count(max(angles))==2:
    print("Isosceles")

else:
    print("Scalene")