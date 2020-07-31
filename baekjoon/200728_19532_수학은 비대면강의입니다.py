a, b, c, d, e, f = map(int, input().split())

y = (c*d-f*a)//(b*d-e*a)
if a:
    x = (c - b*y)//a
else:
    x = (f - e*y)//d
print(x, y)
