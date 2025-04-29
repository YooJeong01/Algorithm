a, b, c, d, e, f = map(int, input().split())

y = (a*f-d*c)//(a*e-b*d)
x = (c*e-b*f)//(a*e-b*d)

print(x,y)