def hano(n,a,b,c):
    if n == 1:
        print(a, "-->", c)
        return None
    if n == 2:
        print(a, "-->", c)
        print(a, "-->", b)
        print(b, "-->", c)
        return None

    hano(n-1, a, c, b)
    print(a, "-->", c)
    hano(n-1, b, a, c)
    print(b, "-->", c)

a = "A"
b = "B"
c = "C"

n = 5
hano(n, a, b, c)
