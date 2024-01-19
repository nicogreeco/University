
z = complex(input())

def polar_coord(x):
    import cmath
    o = cmath.phase(x)
    r = abs(x)
    return o,r

o, r = polar_coord(z)

print(r)
print(o)