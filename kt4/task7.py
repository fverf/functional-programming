#comp и partial

from functools import reduce, partial

def comp(*funcs):
    return lambda x: reduce(lambda v, f: f(v), funcs[::-1], x)
def add(x):
    return x + 1
def mult(x):
    return x * 2

composed = comp(add, mult)
print(composed(3))