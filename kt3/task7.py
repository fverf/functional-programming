#функция comp
from functools import partial

def mult(x, y):
    return x * y
def increment(x):
    return x + 1

multby2 = partial(mult, y=2)
comp = lambda f, g: lambda x: f(g(x))
combined = comp(multby2, increment)
print(combined(3))