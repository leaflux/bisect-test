def inc(x):
    return x + 1

def otherfunc(a, b):
    c = inc(a)
    return b == c

def somefunc(x, y):
    otherfunc(x, y)
