a, b, c, d, e, f = map(float, input().split())

x = (c*e - b*f)//(e*a - b*d)
y = (c*d - a*f)//(b*d - a*e)


print(f"{int(x)} {int(y)}")
